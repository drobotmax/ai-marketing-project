"""Yandex Direct MCP Server - ad campaign data from Yandex Direct API v5."""

import os
import json
import asyncio
from typing import Optional

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

load_dotenv()

YANDEX_DIRECT_TOKEN = os.getenv("YANDEX_DIRECT_TOKEN", "")
USE_SANDBOX = os.getenv("YANDEX_DIRECT_SANDBOX", "false").lower() == "true"

BASE_URL = (
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
                "Content-Type": "application/json; charset=utf-8",
                "Accept-Language": "ru",
            },
        )
    return http_client


async def _request(service: str, method: str, params: dict) -> dict:
    """Make a request to Yandex Direct API v5."""
    if not YANDEX_DIRECT_TOKEN:
        return {"error": "YANDEX_DIRECT_TOKEN not set in environment"}

    client = get_client()
    payload = {"method": method, "params": params}

    try:
        resp = await client.post(f"{BASE_URL}/{service}", json=payload)
        resp.raise_for_status()
        data = resp.json()
        if "error" in data:
            return {
                "error": data["error"].get("error_string", "Unknown error"),
                "detail": data["error"].get("error_detail", ""),
                "code": data["error"].get("error_code"),
            }
        return data.get("result", data)
    except httpx.HTTPStatusError as e:
        return {"error": f"HTTP {e.response.status_code}", "detail": e.response.text}
    except httpx.RequestError as e:
        return {"error": f"Request failed: {str(e)}"}


@mcp.tool(
    annotations=ToolAnnotations(
        title="Get Campaigns",
        readOnlyHint=True,
        openWorldHint=True,
    )
)
async def get_campaigns(
    states: Optional[str] = None,
    limit: int = 100,
) -> str:
    """Get list of advertising campaigns from Yandex Direct.

    Args:
        states: Comma-separated campaign states filter: ON, OFF, SUSPENDED, ENDED, CONVERTED, ARCHIVED. Empty = all.
        limit: Max campaigns to return (default 100, max 10000)
    """
    params = {
        "SelectionCriteria": {},
        "FieldNames": [
            "Id", "Name", "State", "Status", "Type",
            "DailyBudget", "StartDate", "EndDate",
            "Statistics",
        ],
        "Page": {"Limit": min(limit, 10000)},
    }
    if states:
        params["SelectionCriteria"]["States"] = [
            s.strip().upper() for s in states.split(",")
        ]

    result = await _request("campaigns", "get", params)
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Get Ad Groups",
        readOnlyHint=True,
        openWorldHint=True,
    )
)
async def get_ad_groups(
    campaign_ids: str,
    limit: int = 200,
) -> str:
    """Get ad groups for specified campaigns.

    Args:
        campaign_ids: Comma-separated campaign IDs (e.g. "123,456")
        limit: Max groups to return (default 200, max 10000)
    """
    ids = [int(i.strip()) for i in campaign_ids.split(",")]
    params = {
        "SelectionCriteria": {"CampaignIds": ids},
        "FieldNames": [
            "Id", "Name", "CampaignId", "Status", "Type",
            "RegionIds", "NegativeKeywords",
        ],
        "Page": {"Limit": min(limit, 10000)},
    }

    result = await _request("adgroups", "get", params)
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Get Ads",
        readOnlyHint=True,
        openWorldHint=True,
    )
)
async def get_ads(
    campaign_ids: Optional[str] = None,
    ad_group_ids: Optional[str] = None,
    limit: int = 200,
) -> str:
    """Get ads for specified campaigns or ad groups.

    Args:
        campaign_ids: Comma-separated campaign IDs
        ad_group_ids: Comma-separated ad group IDs (takes priority over campaign_ids)
        limit: Max ads to return (default 200, max 10000)
    """
    criteria = {}
    if ad_group_ids:
        criteria["AdGroupIds"] = [int(i.strip()) for i in ad_group_ids.split(",")]
    elif campaign_ids:
        criteria["CampaignIds"] = [int(i.strip()) for i in campaign_ids.split(",")]
    else:
        return json.dumps({"error": "Provide campaign_ids or ad_group_ids"})

    params = {
        "SelectionCriteria": criteria,
        "FieldNames": ["Id", "AdGroupId", "CampaignId", "State", "Status", "Type"],
        "TextAdFieldNames": [
            "Title", "Title2", "Text", "Href", "DisplayDomain",
            "SitelinkSetId", "AdExtensionIds",
        ],
        "Page": {"Limit": min(limit, 10000)},
    }

    result = await _request("ads", "get", params)
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Get Keywords",
        readOnlyHint=True,
        openWorldHint=True,
    )
)
async def get_keywords(
    campaign_ids: Optional[str] = None,
    ad_group_ids: Optional[str] = None,
    limit: int = 500,
) -> str:
    """Get keywords for specified campaigns or ad groups.

    Args:
        campaign_ids: Comma-separated campaign IDs
        ad_group_ids: Comma-separated ad group IDs (takes priority)
        limit: Max keywords to return (default 500, max 10000)
    """
    criteria = {}
    if ad_group_ids:
        criteria["AdGroupIds"] = [int(i.strip()) for i in ad_group_ids.split(",")]
    elif campaign_ids:
        criteria["CampaignIds"] = [int(i.strip()) for i in campaign_ids.split(",")]
    else:
        return json.dumps({"error": "Provide campaign_ids or ad_group_ids"})

    params = {
        "SelectionCriteria": criteria,
        "FieldNames": [
            "Id", "Keyword", "AdGroupId", "CampaignId",
            "State", "Status", "Bid", "ContextBid",
            "StrategyPriority", "StatisticsSearch", "StatisticsNetwork",
        ],
        "Page": {"Limit": min(limit, 10000)},
    }

    result = await _request("keywords", "get", params)
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Get Campaign Stats",
        readOnlyHint=True,
        openWorldHint=True,
    )
)
async def get_stats(
    date_from: str,
    date_to: str,
    report_type: str = "CAMPAIGN_PERFORMANCE_REPORT",
    group_by: str = "CAMPAIGN",
    campaign_ids: Optional[str] = None,
) -> str:
    """Get performance statistics from Yandex Direct Reports API.

    Returns impressions, clicks, cost, conversions grouped by campaign/date.

    Args:
        date_from: Start date YYYY-MM-DD
        date_to: End date YYYY-MM-DD
        report_type: CAMPAIGN_PERFORMANCE_REPORT, AD_PERFORMANCE_REPORT, SEARCH_QUERY_PERFORMANCE_REPORT, CUSTOM_REPORT
        group_by: Grouping: CAMPAIGN, AD_GROUP, AD, KEYWORD, SEARCH_QUERY
        campaign_ids: Optional comma-separated campaign IDs to filter
    """
    fields = ["CampaignName", "CampaignId"]

    if group_by == "AD_GROUP":
        fields.extend(["AdGroupName", "AdGroupId"])
    elif group_by == "AD":
        fields.extend(["AdGroupName", "AdId"])
    elif group_by == "KEYWORD":
        fields.extend(["AdGroupName", "Criterion"])
    elif group_by == "SEARCH_QUERY":
        fields.extend(["Query", "Criterion"])

    fields.extend([
        "Impressions", "Clicks", "Ctr", "AvgCpc",
        "Cost", "AvgImpressionPosition", "AvgClickPosition",
        "Conversions", "CostPerConversion", "ConversionRate",
    ])

    selection = {
        "DateFrom": date_from,
        "DateTo": date_to,
    }
    if campaign_ids:
        selection["Filter"] = [{
            "Field": "CampaignId",
            "Operator": "IN",
            "Values": [i.strip() for i in campaign_ids.split(",")],
        }]

    body = {
        "params": {
            "SelectionCriteria": selection,
            "FieldNames": fields,
            "ReportName": f"kubrik-{report_type}-{date_from}",
            "ReportType": report_type,
            "DateRangeType": "CUSTOM_DATE",
            "Format": "TSV",
            "IncludeVAT": "YES",
            "IncludeDiscount": "NO",
        }
    }

    client = get_client()
    reports_url = BASE_URL.replace("/json/v5", "/json/v5/../v5/reports")
    actual_url = (
        "https://api-sandbox.direct.yandex.com/v5/reports"
        if USE_SANDBOX
        else "https://api.direct.yandex.com/v5/reports"
    )

    try:
        headers = dict(client.headers)
        headers["processingMode"] = "auto"
        headers["returnMoneyInMicros"] = "false"
        headers["skipReportHeader"] = "true"
        headers["skipReportSummary"] = "true"

        resp = await client.post(actual_url, json=body, headers=headers)

        if resp.status_code == 201:
            await asyncio.sleep(5)
            resp = await client.post(actual_url, json=body, headers=headers)

        if resp.status_code == 202:
            return json.dumps({
                "status": "processing",
                "message": "Report is being generated. Try again in 10-30 seconds.",
                "retryIn": int(resp.headers.get("retryIn", 30)),
            })

        resp.raise_for_status()

        lines = resp.text.strip().split("\n")
        if len(lines) < 2:
            return json.dumps({"data": [], "message": "No data for this period"})

        headers_row = lines[0].split("\t")
        rows = []
        for line in lines[1:]:
            values = line.split("\t")
            row = dict(zip(headers_row, values))
            rows.append(row)

        return json.dumps({
            "data": rows,
            "total_rows": len(rows),
            "period": f"{date_from} to {date_to}",
        }, ensure_ascii=False, indent=2)

    except httpx.HTTPStatusError as e:
        return json.dumps({
            "error": f"HTTP {e.response.status_code}",
            "detail": e.response.text[:500],
        })
    except httpx.RequestError as e:
        return json.dumps({"error": f"Request failed: {str(e)}"})


@mcp.tool(
    annotations=ToolAnnotations(
        title="Get Account Info",
        readOnlyHint=True,
        openWorldHint=True,
    )
)
async def get_account_info() -> str:
    """Get Yandex Direct account information: balance, currency, agency status."""
    client = get_client()

    try:
        resp = await client.get(
            BASE_URL.replace("/json/v5", "/json/v5/../live/v4/json/"),
            params={
                "method": "AccountManagement",
                "param": json.dumps({"Action": "Get", "SelectionCriteria": {}}),
            },
        )
        resp.raise_for_status()
        return json.dumps(resp.json(), ensure_ascii=False, indent=2)
    except Exception:
        pass

    params = {
        "FieldNames": [
            "AccountQuality", "Archived", "ClientId", "ClientInfo",
            "CountryId", "CreatedAt", "Currency", "Login",
            "Notification", "Phone", "Representatives",
            "Restrictions", "Settings", "Type",
        ],
    }
    result = await _request("clients", "get", params)
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Get Negative Keywords",
        readOnlyHint=True,
        openWorldHint=True,
    )
)
async def get_negative_keywords(campaign_ids: str) -> str:
    """Get negative keyword lists associated with campaigns.

    Useful for audit: checks coverage and conflicts with active keywords.

    Args:
        campaign_ids: Comma-separated campaign IDs
    """
    ids = [int(i.strip()) for i in campaign_ids.split(",")]

    params = {
        "SelectionCriteria": {"CampaignIds": ids},
        "FieldNames": [
            "Id", "Name", "State", "Status", "NegativeKeywords",
        ],
        "Page": {"Limit": 100},
    }

    result = await _request("campaigns", "get", params)

    if isinstance(result, dict) and "Campaigns" in result:
        campaigns = result["Campaigns"]
        summary = []
        for c in campaigns:
            neg_kw = c.get("NegativeKeywords", {}).get("Items", [])
            summary.append({
                "campaign_id": c.get("Id"),
                "campaign_name": c.get("Name"),
                "negative_keywords_count": len(neg_kw),
                "negative_keywords": neg_kw[:50],
            })
        return json.dumps(summary, ensure_ascii=False, indent=2)

    return json.dumps(result, ensure_ascii=False, indent=2)


async def _main():
    await mcp.run_stdio_async()


if __name__ == "__main__":
    asyncio.run(_main())
