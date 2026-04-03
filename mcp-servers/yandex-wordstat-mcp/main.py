"""Yandex Wordstat MCP Server - keyword frequency data from Yandex."""

import os
import json
import asyncio
from typing import Optional

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

load_dotenv()

YANDEX_API_KEY = os.getenv("YANDEX_WORDSTAT_API_KEY", "")
YANDEX_FOLDER_ID = os.getenv("YANDEX_FOLDER_ID", "")
BASE_URL = "https://searchapi.api.cloud.yandex.net/v2/wordstat"

mcp = FastMCP("yandex-wordstat")

http_client: Optional[httpx.AsyncClient] = None


def get_client() -> httpx.AsyncClient:
    global http_client
    if http_client is None or http_client.is_closed:
        http_client = httpx.AsyncClient(
            timeout=30.0,
            headers={
                "Authorization": f"Api-key {YANDEX_API_KEY}",
                "Content-Type": "application/json",
            },
        )
    return http_client


async def _request(endpoint: str, payload: dict) -> dict:
    """Make a request to Yandex Wordstat API."""
    if not YANDEX_API_KEY:
        return {"error": "YANDEX_WORDSTAT_API_KEY not set in environment"}
    if not YANDEX_FOLDER_ID:
        return {"error": "YANDEX_FOLDER_ID not set in environment"}

    payload["folderId"] = YANDEX_FOLDER_ID
    client = get_client()

    try:
        resp = await client.post(f"{BASE_URL}/{endpoint}", json=payload)
        resp.raise_for_status()
        return resp.json()
    except httpx.HTTPStatusError as e:
        return {
            "error": f"HTTP {e.response.status_code}",
            "detail": e.response.text,
        }
    except httpx.RequestError as e:
        return {"error": f"Request failed: {str(e)}"}


@mcp.tool(
    annotations=ToolAnnotations(
        title="Wordstat Top Requests",
        readOnlyHint=True,
        openWorldHint=True,
    )
)
async def wordstat_top(
    phrase: str,
    num_phrases: int = 100,
    regions: Optional[str] = None,
    device: str = "DEVICE_ALL",
) -> str:
    """Get top keyword frequencies from Yandex Wordstat.

    Returns popular search queries containing the phrase + associated queries.

    Args:
        phrase: Keyword or phrase to check (supports Wordstat operators: +, [], "", !)
        num_phrases: Number of results to return (max 2000, default 100)
        regions: Comma-separated region codes (e.g. "213" for Moscow, "2" for St.Petersburg). Empty = all Russia.
        device: Device filter: DEVICE_ALL, DEVICE_DESKTOP, DEVICE_PHONE, DEVICE_TABLET
    """
    payload = {
        "phrase": phrase,
        "numPhrases": min(num_phrases, 2000),
        "devices": [device],
    }
    if regions:
        payload["regions"] = [r.strip() for r in regions.split(",")]

    result = await _request("topRequests", payload)
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Wordstat Dynamics",
        readOnlyHint=True,
        openWorldHint=True,
    )
)
async def wordstat_dynamics(
    phrase: str,
    from_date: str,
    to_date: str,
    period: str = "PERIOD_MONTHLY",
    regions: Optional[str] = None,
    device: str = "DEVICE_ALL",
) -> str:
    """Get keyword frequency dynamics over time from Yandex Wordstat.

    Args:
        phrase: Keyword or phrase to check
        from_date: Start date in YYYY-MM-DD format (e.g. "2025-01-01")
        to_date: End date in YYYY-MM-DD format (e.g. "2026-03-01")
        period: Aggregation: PERIOD_DAILY, PERIOD_WEEKLY, PERIOD_MONTHLY
        regions: Comma-separated region codes. Empty = all Russia.
        device: Device filter: DEVICE_ALL, DEVICE_DESKTOP, DEVICE_PHONE, DEVICE_TABLET
    """
    payload = {
        "phrase": phrase,
        "fromDate": f"{from_date}T00:00:00Z",
        "toDate": f"{to_date}T00:00:00Z",
        "period": period,
        "devices": [device],
    }
    if regions:
        payload["regions"] = [r.strip() for r in regions.split(",")]

    result = await _request("dynamics", payload)
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Wordstat Regions",
        readOnlyHint=True,
        openWorldHint=True,
    )
)
async def wordstat_regions(
    phrase: str,
    group_by: str = "GROUP_BY_REGION",
    device: str = "DEVICE_ALL",
) -> str:
    """Get regional distribution of keyword frequency from Yandex Wordstat.

    Args:
        phrase: Keyword or phrase to check
        group_by: Grouping: GROUP_BY_REGION, GROUP_BY_CITY, GROUP_BY_ALL
        device: Device filter: DEVICE_ALL, DEVICE_DESKTOP, DEVICE_PHONE, DEVICE_TABLET
    """
    payload = {
        "phrase": phrase,
        "groupBy": group_by,
        "devices": [device],
    }

    result = await _request("regions", payload)
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Wordstat Regions Tree",
        readOnlyHint=True,
        openWorldHint=True,
    )
)
async def wordstat_regions_tree() -> str:
    """Get the full tree of Yandex region codes.

    Use this to find region IDs for filtering other Wordstat tools.
    Common: 213 = Moscow, 2 = St.Petersburg, 225 = Russia.
    """
    client = get_client()

    if not YANDEX_API_KEY:
        return json.dumps({"error": "YANDEX_WORDSTAT_API_KEY not set"})

    try:
        resp = await client.get(
            f"{BASE_URL}/regions",
            params={"folderId": YANDEX_FOLDER_ID},
        )
        resp.raise_for_status()
        return json.dumps(resp.json(), ensure_ascii=False, indent=2)
    except httpx.HTTPStatusError as e:
        return json.dumps({"error": f"HTTP {e.response.status_code}", "detail": e.response.text})
    except httpx.RequestError as e:
        return json.dumps({"error": f"Request failed: {str(e)}"})


async def _main():
    await mcp.run_stdio_async()


if __name__ == "__main__":
    asyncio.run(_main())
