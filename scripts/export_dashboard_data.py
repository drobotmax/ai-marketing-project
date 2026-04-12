"""Export Yandex Direct data to JSON for the KUBRIK dashboard.

Usage:
    python export_dashboard_data.py [--days 7] [--output ../dashboard/data.json]

Requires YANDEX_DIRECT_TOKEN env var.
"""

import os
import sys
import json
import asyncio
import argparse
from datetime import date, timedelta

import httpx
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "../mcp-servers/yandex-direct-mcp/.env"))

TOKEN = os.getenv("YANDEX_DIRECT_TOKEN", "")
USE_SANDBOX = os.getenv("YANDEX_DIRECT_SANDBOX", "false").lower() == "true"
API_URL = (
    "https://api-sandbox.direct.yandex.com/json/v5"
    if USE_SANDBOX
    else "https://api.direct.yandex.com/json/v5"
)


async def api_request(client: httpx.AsyncClient, service: str, method: str, params: dict) -> dict:
    url = f"{API_URL}/{service}"
    body = {"method": method, "params": params}
    resp = await client.post(url, json=body)
    resp.raise_for_status()
    data = resp.json()
    if "error" in data:
        raise Exception(f"API error: {data['error']}")
    return data.get("result", data)


async def report_request(client: httpx.AsyncClient, report_def: dict) -> list[dict]:
    url = f"{API_URL}/reports"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "Accept-Language": "ru",
        "processingMode": "auto",
        "returnMoneyInMicros": "false",
        "skipReportHeader": "true",
        "skipReportSummary": "true",
    }
    body = {"params": report_def}
    delay = 2

    for _ in range(10):
        resp = await client.post(url, json=body, headers=headers)
        if resp.status_code == 200:
            lines = resp.text.strip().split("\n")
            if len(lines) < 2:
                return []
            hdrs = lines[0].split("\t")
            return [dict(zip(hdrs, line.split("\t"))) for line in lines[1:]]
        elif resp.status_code in (201, 202):
            retry_in = int(resp.headers.get("retryIn", delay))
            await asyncio.sleep(retry_in)
            delay = min(delay * 2, 30)
        else:
            raise Exception(f"Report error HTTP {resp.status_code}: {resp.text}")

    raise Exception("Report timed out")


async def export(days: int, output_path: str):
    if not TOKEN:
        print("ERROR: YANDEX_DIRECT_TOKEN not set", file=sys.stderr)
        sys.exit(1)

    date_from = (date.today() - timedelta(days=days)).isoformat()
    date_to = (date.today() - timedelta(days=1)).isoformat()

    async with httpx.AsyncClient(
        timeout=60.0,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "Accept-Language": "ru",
        },
    ) as client:

        # 1. Get campaigns
        print("Fetching campaigns...")
        campaigns_raw = await api_request(client, "campaigns", "get", {
            "SelectionCriteria": {},
            "FieldNames": ["Id", "Name", "Status", "State", "Type", "DailyBudget", "StartDate"],
        })
        campaigns = campaigns_raw.get("Campaigns", [])

        # 2. Get daily stats
        print(f"Fetching stats {date_from} to {date_to}...")
        daily_stats = await report_request(client, {
            "SelectionCriteria": {"DateFrom": date_from, "DateTo": date_to},
            "FieldNames": ["Date", "CampaignName", "CampaignId", "Impressions", "Clicks", "Ctr", "AvgCpc", "Cost", "Conversions"],
            "ReportName": f"kubrik-export-daily-{date_from}",
            "ReportType": "CAMPAIGN_PERFORMANCE_REPORT",
            "DateRangeType": "CUSTOM_DATE",
            "Format": "TSV",
            "IncludeVAT": "YES",
        })

        # 3. Get keyword stats
        print("Fetching keyword stats...")
        keyword_stats = await report_request(client, {
            "SelectionCriteria": {"DateFrom": date_from, "DateTo": date_to},
            "FieldNames": ["CriteriaId", "Criteria", "CampaignName", "Impressions", "Clicks", "Ctr", "AvgCpc", "Cost"],
            "ReportName": f"kubrik-export-kw-{date_from}",
            "ReportType": "CRITERIA_PERFORMANCE_REPORT",
            "DateRangeType": "CUSTOM_DATE",
            "Format": "TSV",
            "IncludeVAT": "YES",
        })

        # 4. Aggregate
        total_cost = sum(float(r.get("Cost", 0)) for r in daily_stats)
        total_clicks = sum(int(r.get("Clicks", 0)) for r in daily_stats)
        total_impressions = sum(int(r.get("Impressions", 0)) for r in daily_stats)
        total_conversions = sum(int(r.get("Conversions", 0)) for r in daily_stats)
        avg_ctr = (total_clicks / total_impressions * 100) if total_impressions > 0 else 0
        avg_cpc = (total_cost / total_clicks) if total_clicks > 0 else 0

        # Daily spend chart data
        daily_spend = {}
        for r in daily_stats:
            d = r.get("Date", "")
            daily_spend[d] = daily_spend.get(d, 0) + float(r.get("Cost", 0))

        # Campaign summary
        campaign_summary = {}
        for r in daily_stats:
            cid = r.get("CampaignId", "")
            if cid not in campaign_summary:
                campaign_summary[cid] = {
                    "id": cid,
                    "name": r.get("CampaignName", ""),
                    "impressions": 0, "clicks": 0, "cost": 0, "conversions": 0,
                }
            s = campaign_summary[cid]
            s["impressions"] += int(r.get("Impressions", 0))
            s["clicks"] += int(r.get("Clicks", 0))
            s["cost"] += float(r.get("Cost", 0))
            s["conversions"] += int(r.get("Conversions", 0))

        for s in campaign_summary.values():
            s["ctr"] = round(s["clicks"] / s["impressions"] * 100, 2) if s["impressions"] > 0 else 0
            s["avg_cpc"] = round(s["cost"] / s["clicks"], 2) if s["clicks"] > 0 else 0

        # Top keywords by clicks
        kw_sorted = sorted(keyword_stats, key=lambda x: int(x.get("Clicks", 0)), reverse=True)[:20]

        # Alerts
        alerts = []
        active_count = sum(1 for c in campaigns if c.get("State") == "ON")
        for c in campaigns:
            if c.get("Status") in ("SUSPENDED", "OFF") and c.get("State") != "ARCHIVED":
                alerts.append({"type": "warning", "message": f"Campaign '{c.get('Name')}' is {c.get('Status')}"})

        for s in campaign_summary.values():
            if s["ctr"] < 1.0 and s["impressions"] > 100:
                alerts.append({"type": "low_ctr", "message": f"Low CTR ({s['ctr']}%) for '{s['name']}'"})

        dashboard_data = {
            "exported_at": date.today().isoformat(),
            "period": {"from": date_from, "to": date_to},
            "overview": {
                "campaigns_total": len(campaigns),
                "campaigns_active": active_count,
                "total_cost": round(total_cost, 2),
                "total_clicks": total_clicks,
                "total_impressions": total_impressions,
                "total_conversions": total_conversions,
                "avg_ctr": round(avg_ctr, 2),
                "avg_cpc": round(avg_cpc, 2),
            },
            "campaigns": list(campaign_summary.values()),
            "daily_spend": [{"date": d, "cost": round(v, 2)} for d, v in sorted(daily_spend.items())],
            "top_keywords": kw_sorted,
            "alerts": alerts,
        }

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(dashboard_data, f, ensure_ascii=False, indent=2)

    print(f"Exported to {output_path}")
    print(f"  Period: {date_from} to {date_to}")
    print(f"  Campaigns: {len(campaigns)} ({active_count} active)")
    print(f"  Total spend: {total_cost:.2f} RUB")
    print(f"  Clicks: {total_clicks}, Impressions: {total_impressions}")


def main():
    parser = argparse.ArgumentParser(description="Export Yandex Direct data for KUBRIK dashboard")
    parser.add_argument("--days", type=int, default=7, help="Number of days to export (default: 7)")
    parser.add_argument("--output", default=os.path.join(os.path.dirname(__file__), "../dashboard/data.json"), help="Output JSON path")
    args = parser.parse_args()
    asyncio.run(export(args.days, args.output))


if __name__ == "__main__":
    main()
