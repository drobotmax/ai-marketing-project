#!/usr/bin/env bash
# Fetch and parse a single RSS/Atom feed
# Usage: bash scripts/fetch_rss.sh --url "https://..." --platform google --period 7
# Output: TSV to stdout (date, platform, title, url, summary)

set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
. "$SCRIPT_DIR/common.sh"

load_config
ensure_dirs

URL=""
FEED_PLATFORM=""
FEED_NAME=""
PERIOD_DAYS="7"

while [ $# -gt 0 ]; do
    case "$1" in
        --url)       URL="$2"; shift 2 ;;
        --platform)  FEED_PLATFORM="$2"; shift 2 ;;
        --name)      FEED_NAME="$2"; shift 2 ;;
        --period)    PERIOD_DAYS="$2"; shift 2 ;;
        *)           shift ;;
    esac
done

if [ -z "$URL" ]; then
    echo "Error: --url required" >&2
    exit 1
fi

CUTOFF_DATE=$(days_ago_iso "$PERIOD_DAYS")

# Fetch RSS
FEED_CACHE="$CACHE_DIR/rss_$(portable_sha256 "$URL" 12).xml"
web_fetch "$URL" > "$FEED_CACHE"

if [ ! -s "$FEED_CACHE" ]; then
    echo "Error: empty response from $URL" >&2
    exit 1
fi

# The RSS XML is on one long line - split tags onto separate lines first
split_xml_tags "$FEED_CACHE" > "$FEED_CACHE.split"

# Parse with awk
awk -v platform="$FEED_PLATFORM" -v cutoff="$CUTOFF_DATE" \
    -f "$SCRIPT_DIR/parse_rss.awk" "$FEED_CACHE.split"
