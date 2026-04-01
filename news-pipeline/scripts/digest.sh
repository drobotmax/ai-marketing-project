#!/usr/bin/env bash
# Build a complete news digest: RSS blogs + TG channels
# Usage: bash scripts/digest.sh [--period 7] [--platform google] [--no-dedup]
# Output: Markdown digest to stdout + saved to data/digests/

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
. "$SCRIPT_DIR/common.sh"

load_config
ensure_dirs
ensure_seen
parse_common_params "$@"

TODAY=$(date +%Y-%m-%d)
DIGEST_FILE="$DATA_DIR/digests/digest_${TODAY}.md"

echo "=== KUBRIK News Digest ($TODAY, last $PERIOD days) ===" >&2

# ---- Step 1: Fetch RSS blogs ----
echo "Step 1/3: Fetching RSS blogs..." >&2
BLOGS_TSV="$CACHE_DIR/blogs_latest.tsv"

_blog_args="--period $PERIOD"
if [ -n "$PLATFORM" ]; then
    _blog_args="$_blog_args --platform $PLATFORM"
fi

bash "$SCRIPT_DIR/fetch_blogs.sh" $_blog_args > "$BLOGS_TSV" 2>/dev/null || true

# ---- Step 2: Fetch TG channels ----
echo "Step 2/3: Fetching Telegram channels..." >&2
TG_TSV="$CACHE_DIR/tg_latest.tsv"
: > "$TG_TSV"

if [ -n "$NEWS_TG_CHANNELS" ] && [ -d "$TG_PARSER_DIR/scripts" ]; then
    (
        export LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
        bash "$TG_PARSER_DIR/scripts/digest.sh" \
            --channels "$NEWS_TG_CHANNELS" \
            --period "$PERIOD" > "$CACHE_DIR/tg_raw.txt"
    ) 2>/dev/null || true

    # Convert TG digest output to our TSV format
    # TG digest shows: time | views | text
    # We need: date, platform, title, url, summary
    if [ -s "$CACHE_DIR/tg_raw.txt" ]; then
        _current_channel=""
        while IFS= read -r line; do
            # Channel header: --- @channelname ---
            case "$line" in
                "--- @"*)
                    _current_channel="${line#--- @}"
                    _current_channel="${_current_channel% ---}"
                    continue
                    ;;
            esac
            # Post line: HH:MM | NNK views | text...
            case "$line" in
                *"|"*"views"*"|"*)
                    _text="${line##*views*| }"
                    _tg_url="https://t.me/$_current_channel"
                    printf "%s\ttelegram\t[TG @%s] %s\t%s\t%s\n" \
                        "$TODAY" "$_current_channel" "$_text" "$_tg_url" "" >> "$TG_TSV"
                    ;;
            esac
        done < "$CACHE_DIR/tg_raw.txt"
    fi
    echo "TG posts collected: $(wc -l < "$TG_TSV" | tr -d ' ')" >&2
else
    echo "Skipping TG (no channels configured or parser not found)" >&2
fi

# ---- Step 3: Merge, dedup, format ----
echo "Step 3/3: Building digest..." >&2

{
    echo "# KUBRIK News Digest"
    echo "**Date:** $TODAY | **Period:** last $PERIOD days"
    echo ""

    # Process blogs by platform
    _has_content=0

    for _plat in google yandex meta tiktok; do
        _plat_upper=$(echo "$_plat" | tr '[:lower:]' '[:upper:]')
        _plat_items=""

        if [ -s "$BLOGS_TSV" ]; then
            _plat_items=$(awk -F'\t' -v p="$_plat" '$2 == p { print }' "$BLOGS_TSV")
        fi

        if [ -n "$_plat_items" ]; then
            echo "## $_plat_upper"
            echo ""
            while IFS=$'\t' read -r _date _platform _title _url _summary; do
                if [ -z "$NO_DEDUP" ] && is_seen "$_url"; then
                    continue
                fi
                echo "- **[$_title]($_url)** ($_date)"
                if [ -n "$_summary" ]; then
                    echo "  $_summary"
                fi
                echo ""
                _has_content=1
            done <<< "$_plat_items"
        fi
    done

    # TG section
    if [ -s "$TG_TSV" ]; then
        echo "## TELEGRAM"
        echo ""
        _prev_channel=""
        while IFS=$'\t' read -r _date _platform _title _url _summary; do
            # Extract channel: [TG @channel] text -> channel
            _ch="${_title#\[TG @}"
            _ch="${_ch%%\]*}"
            if [ "$_ch" != "$_prev_channel" ]; then
                echo "### @$_ch"
                _prev_channel="$_ch"
            fi
            # Extract text after [TG @channel]
            _text="${_title#*\] }"
            if [ ${#_text} -gt 150 ]; then
                _text="${_text:0:150}..."
            fi
            echo "- $_text"
        done < "$TG_TSV"
        echo ""
    fi

    echo "---"
    echo "*Generated: $(date '+%Y-%m-%d %H:%M') | Sources: RSS blogs + Telegram channels*"

} > "$DIGEST_FILE"

# Mark all blog URLs as seen (unless --no-dedup)
if [ -z "$NO_DEDUP" ] && [ -s "$BLOGS_TSV" ]; then
    while IFS=$'\t' read -r _date _platform _title _url _summary; do
        [ -n "$_url" ] && mark_seen "$_url"
    done < "$BLOGS_TSV"
fi

# Output the digest
cat "$DIGEST_FILE"

echo "" >&2
echo "Digest saved: $DIGEST_FILE" >&2
echo "Seen DB: $(wc -c < "$SEEN_FILE" | tr -d ' ') bytes" >&2
