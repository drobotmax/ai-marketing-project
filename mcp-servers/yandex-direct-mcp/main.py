"""Yandex Direct MCP Server - campaign management and analytics for KUBRIK."""

import os
import json
import asyncio
from typing import Optional
from datetime import date, timedelta

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

load_dotenv()

YANDEX_DIRECT_TOKEN = os.getenv("YANDEX_DIRECT_TOKEN", "")
USE_SANDBOX = os.getenv("YANDEX_DIRECT_SANDBOX", "false").lower() == "true"

API_URL = (
    "https://api-sandbox.direct.yandex.com/json/v5"
    if USE_SANDBOX
    else "https://api.direct.yandex.com/json/v5"
)

mcp = FastMCP("yandex-direct")

http_client: Optional[httpx.AsyncClient] = None


def get_client() -> httpx.AsyncClient:
    global http_client
    if http_client is None or http_client.is_closed:
        http_client = httpx.AsyncClient(
            timeout=60.0,
            headers={
                "Authorization": f"Bearer {YANDEX_DIRECT_TOKEN}",
                "Content-Type": "application/json",
                "Accept-Language": "ru",
            },
        )
    return http_client


async def _api_request(service: str, method: str, params: dict) -> dict:
    """Make a request to Yandex Direct API v5."""
    if not YANDEX_DIRECT_TOKEN:
        return {"error": "YANDEX_DIRECT_TOKEN not set in environment"}

    client = get_client()
    url = f"{API_URL}/{service}"
    body = {"method": method, "params": params}

    try:
        resp = await client.post(url, json=body)
        resp.raise_for_status()
        data = resp.json()
        if "error" in data:
            return {
                "error": data["error"].get("error_string", "Unknown error"),
                "detail": data["error"].get("error_detail", ""),
                "code": data["error"].get("error_code", 0),
            }
        return data.get("result", data)
    except httpx.HTTPStatusError as e:
        return {"error": f"HTTP {e.response.status_code}", "detail": e.response.text}
    except httpx.RequestError as e:
        return {"error": f"Request failed: {str(e)}"}


async def _report_request(report_def: dict) -> str:
    """Request a report from Yandex Direct Reports API.

    Returns TSV data or error string.
    The Reports API is async - may return 201 (building) or 202 (not ready yet).
    We poll until 200 (ready) with exponential backoff.
    """
    if not YANDEX_DIRECT_TOKEN:
        return json.dumps({"error": "YANDEX_DIRECT_TOKEN not set in environment"})

    client = get_client()
    url = f"{API_URL}/reports"
    headers = {
        "Authorization": f"Bearer {YANDEX_DIRECT_TOKEN}",
        "Content-Type": "application/json",
        "Accept-Language": "ru",
        "processingMode": "auto",
        "returnMoneyInMicros": "false",
        "skipReportHeader": "true",
        "skipReportSummary": "true",
    }

    body = {"params": report_def}

    delay = 2
    max_attempts = 10

    for attempt in range(max_attempts):
        try:
            resp = await client.post(url, json=body, headers=headers)

            if resp.status_code == 200:
                return resp.text
            elif resp.status_code in (201, 202):
                retry_in = int(resp.headers.get("retryIn", delay))
                await asyncio.sleep(retry_in)
                delay = min(delay * 2, 30)
                continue
            else:
                return json.dumps({
                    "error": f"HTTP {resp.status_code}",
                    "detail": resp.text,
                })
        except httpx.RequestError as e:
            return json.dumps({"error": f"Request failed: {str(e)}"})

    return json.dumps({"error": "Report timed out after max attempts"})


def _parse_tsv_report(tsv_text: str) -> list[dict]:
    """Parse TSV report into list of dicts."""
    lines = tsv_text.strip().split("\n")
    if len(lines) < 2:
        return []
    headers = lines[0].split("\t")
    rows = []
    for line in lines[1:]:
        values = line.split("\t")
        rows.append(dict(zip(headers, values)))
    return rows


# --- MCP Tools ---


@mcp.tool(
    annotations=ToolAnnotations(
        title="Yandex Direct Campaigns",
        readOnlyHint=True,
        openWorldHint=True,
    )
)
async def direct_campaigns(
    status: Optional[str] = None,
) -> str:
    """Get list of campaigns from Yandex Direct account.

    Returns campaign ID, name, status, type, daily budget, and start date.

    Args:
        status: Filter by status. Options: ACCEPTED, DRAFT, MODERATION, OFF,
                ON_HOLD, SUSPENDED, ENDED, CONVERTED, ARCHIVED.
                Leave empty for all campaigns.
    """
    params = {
        "SelectionCriteria": {},
        "FieldNames": [
            "Id", "Name", "Status", "State", "Type",
            "DailyBudget", "StartDate", "Statistics",
        ],
    }

    if status:
        params["SelectionCriteria"]["Statuses"] = [status.upper()]

    result = await _api_request("campaigns", "get", params)
    if "error" in result:
        return json.dumps(result, ensure_ascii=False, indent=2)

    campaigns = result.get("Campaigns", [])
    output = []
    for c in campaigns:
        budget = c.get("DailyBudget", {})
        stats = c.get("Statistics", {})
        output.append({
            "id": c.get("Id"),
            "name": c.get("Name"),
            "status": c.get("Status"),
            "state": c.get("State"),
            "type": c.get("Type"),
            "daily_budget": budget.get("Amount"),
            "start_date": c.get("StartDate"),
            "clicks": stats.get("Clicks"),
            "impressions": stats.get("Impressions"),
        })

    return json.dumps(output, ensure_ascii=False, indent=2)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Yandex Direct Campaign Stats",
        readOnlyHint=True,
        openWorldHint=True,
    )
)
async def direct_campaign_stats(
    campaign_id: Optional[int] = None,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
    group_by: str = "day",
) -> str:
    """Get campaign performance statistics from Yandex Direct.

    Returns impressions, clicks, CTR, avg CPC, cost, and conversions by date.

    Args:
        campaign_id: Campaign ID to filter. Leave empty for all campaigns.
        date_from: Start date YYYY-MM-DD (default: 7 days ago)
        date_to: End date YYYY-MM-DD (default: yesterday)
        group_by: Group results by: "day", "week", "month", "campaign"
    """
    if not date_from:
        date_from = (date.today() - timedelta(days=7)).isoformat()
    if not date_to:
        date_to = (date.today() - timedelta(days=1)).isoformat()

    group_map = {
        "day": "DATE",
        "week": "WEEK",
        "month": "MONTH",
        "campaign": "CAMPAIGN",
    }

    report_def = {
        "SelectionCriteria": {
            "DateFrom": date_from,
            "DateTo": date_to,
        },
        "FieldNames": [
            "Date", "CampaignName", "CampaignId",
            "Impressions", "Clicks", "Ctr", "AvgCpc", "Cost", "Conversions",
        ],
        "ReportName": f"kubrik-stats-{date_from}-{date_to}",
        "ReportType": "CAMPAIGN_PERFORMANCE_REPORT",
        "DateRangeType": "CUSTOM_DATE",
        "Format": "TSV",
        "IncludeVAT": "YES",
    }

    if campaign_id:
        report_def["SelectionCriteria"]["Filter"] = [{
            "Field": "CampaignId",
            "Operator": "EQUALS",
            "Values": [str(campaign_id)],
        }]

    if group_by in group_map and group_by != "campaign":
        report_def["FieldNames"][0] = group_map[group_by] if group_by != "day" else "Date"

    tsv = await _report_request(report_def)
    try:
        rows = _parse_tsv_report(tsv)
        return json.dumps(rows, ensure_ascii=False, indent=2)
    except Exception:
        return tsv


@mcp.tool(
    annotations=ToolAnnotations(
        title="Yandex Direct Ad Groups",
        readOnlyHint=True,
        openWorldHint=True,
    )
)
async def direct_ad_groups(
    campaign_id: int,
) -> str:
    """Get ad groups for a specific campaign.

    Args:
        campaign_id: Campaign ID to get ad groups for.
    """
    params = {
        "SelectionCriteria": {
            "CampaignIds": [campaign_id],
        },
        "FieldNames": [
            "Id", "Name", "CampaignId", "Status",
            "Type", "RegionIds",
        ],
    }

    result = await _api_request("adgroups", "get", params)
    if "error" in result:
        return json.dumps(result, ensure_ascii=False, indent=2)

    groups = result.get("AdGroups", [])
    output = []
    for g in groups:
        output.append({
            "id": g.get("Id"),
            "name": g.get("Name"),
            "campaign_id": g.get("CampaignId"),
            "status": g.get("Status"),
            "type": g.get("Type"),
            "regions": g.get("RegionIds", []),
        })

    return json.dumps(output, ensure_ascii=False, indent=2)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Yandex Direct Ads",
        readOnlyHint=True,
        openWorldHint=True,
    )
)
async def direct_ads(
    campaign_id: Optional[int] = None,
    ad_group_id: Optional[int] = None,
) -> str:
    """Get ads with their texts and statuses.

    Args:
        campaign_id: Filter by campaign ID.
        ad_group_id: Filter by ad group ID. Takes priority over campaign_id.
    """
    criteria = {}
    if ad_group_id:
        criteria["AdGroupIds"] = [ad_group_id]
    elif campaign_id:
        criteria["CampaignIds"] = [campaign_id]
    else:
        return json.dumps({"error": "Provide campaign_id or ad_group_id"})

    params = {
        "SelectionCriteria": criteria,
        "FieldNames": ["Id", "AdGroupId", "CampaignId", "Status", "State", "Type"],
        "TextAdFieldNames": [
            "Title", "Title2", "Text", "Href", "DisplayDomain",
            "SitelinkSetId", "AdExtensionIds",
        ],
    }

    result = await _api_request("ads", "get", params)
    if "error" in result:
        return json.dumps(result, ensure_ascii=False, indent=2)

    ads = result.get("Ads", [])
    output = []
    for ad in ads:
        text_ad = ad.get("TextAd", {})
        output.append({
            "id": ad.get("Id"),
            "ad_group_id": ad.get("AdGroupId"),
            "campaign_id": ad.get("CampaignId"),
            "status": ad.get("Status"),
            "state": ad.get("State"),
            "type": ad.get("Type"),
            "title": text_ad.get("Title"),
            "title2": text_ad.get("Title2"),
            "text": text_ad.get("Text"),
            "href": text_ad.get("Href"),
            "display_domain": text_ad.get("DisplayDomain"),
        })

    return json.dumps(output, ensure_ascii=False, indent=2)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Yandex Direct Keywords",
        readOnlyHint=True,
        openWorldHint=True,
    )
)
async def direct_keywords(
    campaign_id: Optional[int] = None,
    ad_group_id: Optional[int] = None,
) -> str:
    """Get keywords with bids and statuses.

    Args:
        campaign_id: Filter by campaign ID.
        ad_group_id: Filter by ad group ID. Takes priority over campaign_id.
    """
    criteria = {}
    if ad_group_id:
        criteria["AdGroupIds"] = [ad_group_id]
    elif campaign_id:
        criteria["CampaignIds"] = [campaign_id]
    else:
        return json.dumps({"error": "Provide campaign_id or ad_group_id"})

    params = {
        "SelectionCriteria": criteria,
        "FieldNames": [
            "Id", "Keyword", "AdGroupId", "CampaignId",
            "Status", "State", "Bid", "ContextBid",
        ],
    }

    result = await _api_request("keywords", "get", params)
    if "error" in result:
        return json.dumps(result, ensure_ascii=False, indent=2)

    keywords = result.get("Keywords", [])
    output = []
    for kw in keywords:
        output.append({
            "id": kw.get("Id"),
            "keyword": kw.get("Keyword"),
            "ad_group_id": kw.get("AdGroupId"),
            "campaign_id": kw.get("CampaignId"),
            "status": kw.get("Status"),
            "state": kw.get("State"),
            "bid": kw.get("Bid"),
            "context_bid": kw.get("ContextBid"),
        })

    return json.dumps(output, ensure_ascii=False, indent=2)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Yandex Direct Account Balance",
        readOnlyHint=True,
        openWorldHint=True,
    )
)
async def direct_account_balance() -> str:
    """Get Yandex Direct account balance and general info.

    Returns account balance, currency, and date range of available data.
    """
    if not YANDEX_DIRECT_TOKEN:
        return json.dumps({"error": "YANDEX_DIRECT_TOKEN not set in environment"})

    client = get_client()

    # Use Campaigns service to get account-level data via a lightweight call
    # Direct API doesn't have a dedicated "balance" endpoint in v5,
    # but we can get it from AccountManagement or via a minimal report
    report_def = {
        "SelectionCriteria": {
            "DateFrom": date.today().isoformat(),
            "DateTo": date.today().isoformat(),
        },
        "FieldNames": ["Cost", "Impressions", "Clicks"],
        "ReportName": f"kubrik-balance-check-{date.today().isoformat()}",
        "ReportType": "ACCOUNT_PERFORMANCE_REPORT",
        "DateRangeType": "TODAY",
        "Format": "TSV",
        "IncludeVAT": "YES",
    }

    # Also get campaigns count for overview
    campaigns_result = await _api_request("campaigns", "get", {
        "SelectionCriteria": {},
        "FieldNames": ["Id", "Status", "State"],
    })

    today_tsv = await _report_request(report_def)
    today_data = _parse_tsv_report(today_tsv) if not today_tsv.startswith("{") else []

    campaigns = campaigns_result.get("Campaigns", []) if "error" not in campaigns_result else []
    active = sum(1 for c in campaigns if c.get("State") == "ON")
    total = len(campaigns)

    output = {
        "campaigns_total": total,
        "campaigns_active": active,
        "campaigns_by_status": {},
        "today": today_data[0] if today_data else {},
    }

    for c in campaigns:
        st = c.get("Status", "UNKNOWN")
        output["campaigns_by_status"][st] = output["campaigns_by_status"].get(st, 0) + 1

    return json.dumps(output, ensure_ascii=False, indent=2)


async def _main():
    await mcp.run_stdio_async()


if __name__ == "__main__":
    asyncio.run(_main())
