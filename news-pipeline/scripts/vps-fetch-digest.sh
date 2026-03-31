#!/usr/bin/env bash
# VPS cron script: fetch RSS feeds and push digest to kubrik repo
# Runs on VPS every Monday at 08:00 MSK via cron
# Remote trigger then processes the digest at 08:23 MSK
#
# Setup on VPS:
#   git clone https://github.com/drobotmax/kubrik.git ~/kubrik
#   crontab -e -> 0 5 * * 1 /home/maxos/kubrik/news-pipeline/scripts/vps-fetch-digest.sh

set -e
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

REPO_DIR="${KUBRIK_REPO:-$HOME/kubrik}"
PIPELINE_DIR="$REPO_DIR/news-pipeline"
SCRIPTS_DIR="$PIPELINE_DIR/scripts"
DATA_DIR="$PIPELINE_DIR/data"
CACHE_DIR="$PIPELINE_DIR/cache"
CONFIG_FILE="$PIPELINE_DIR/config/.env"
TODAY=$(date +%Y-%m-%d)
DIGEST_FILE="$DATA_DIR/digests/digest_${TODAY}.md"
LOG_FILE="$PIPELINE_DIR/data/fetch.log"

mkdir -p "$DATA_DIR/digests" "$CACHE_DIR"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "=== KUBRIK News Fetch Starting ==="

# Pull latest repo
cd "$REPO_DIR"
git pull --quiet 2>/dev/null || log "WARNING: git pull failed, continuing with local copy"

# Load config
if [ -f "$CONFIG_FILE" ]; then
    . "$CONFIG_FILE"
else
    log "ERROR: no config/.env found"
    exit 1
fi

PERIOD="${NEWS_DIGEST_PERIOD:-7}"
CUTOFF_DATE=$(date -d "$PERIOD days ago" +%Y-%m-%d 2>/dev/null || date -v-"${PERIOD}d" +%Y-%m-%d)

log "Period: $PERIOD days (since $CUTOFF_DATE)"

# --- Fetch RSS feeds ---
BLOGS_TSV="$CACHE_DIR/blogs_latest.tsv"
: > "$BLOGS_TSV"

fetch_rss() {
    local name="$1" url="$2" platform="$3"
    local cache_file="$CACHE_DIR/rss_$(echo "$url" | sha256sum 2>/dev/null | cut -c1-12 || shasum -a 256 <<< "$url" | cut -c1-12).xml"

    log "Fetching: $name ($platform)..."

    sleep 1.5
    curl -sL \
        -H "Accept-Language: en-US,en;q=0.9,ru;q=0.5" \
        -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" \
        --max-time 15 \
        "$url" > "$cache_file" 2>/dev/null

    if [ ! -s "$cache_file" ]; then
        log "WARNING: empty response from $url"
        return
    fi

    # Split XML tags onto separate lines for awk parsing
    sed 's/></>\n</g' "$cache_file" > "$cache_file.split"

    # Parse with awk
    awk -v platform="$platform" -v cutoff="$CUTOFF_DATE" \
        -f "$SCRIPTS_DIR/parse_rss.awk" "$cache_file.split" >> "$BLOGS_TSV"

    local count=$(wc -l < "$BLOGS_TSV" | tr -d ' ')
    log "  -> $count articles total so far"
}

# Parse NEWS_RSS_FEEDS from config
echo "$NEWS_RSS_FEEDS" | while IFS= read -r line; do
    line=$(echo "$line" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
    [ -z "$line" ] && continue

    _name=$(echo "$line" | cut -d'|' -f1 | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
    _url=$(echo "$line" | cut -d'|' -f2 | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
    _platform=$(echo "$line" | cut -d'|' -f3 | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')

    [ -z "$_url" ] && continue
    fetch_rss "$_name" "$_url" "$_platform"
done

# Sort by date descending
if [ -s "$BLOGS_TSV" ]; then
    sort -t$'\t' -k1,1r "$BLOGS_TSV" -o "$BLOGS_TSV"
fi

TOTAL=$(wc -l < "$BLOGS_TSV" 2>/dev/null | tr -d ' ')
log "Total articles fetched: $TOTAL"

# --- Build digest markdown ---
{
    echo "# KUBRIK News Digest"
    echo "**Date:** $TODAY | **Period:** last $PERIOD days"
    echo ""

    for _plat in google yandex meta tiktok; do
        _plat_upper=$(echo "$_plat" | tr '[:lower:]' '[:upper:]')
        _plat_items=""

        if [ -s "$BLOGS_TSV" ]; then
            _plat_items=$(awk -F'\t' -v p="$_plat" '$2 == p { print }' "$BLOGS_TSV")
        fi

        if [ -n "$_plat_items" ]; then
            echo "## $_plat_upper"
            echo ""
            echo "$_plat_items" | while IFS=$'\t' read -r _date _platform _title _url _summary; do
                echo "- **[$_title]($_url)** ($_date)"
                if [ -n "$_summary" ]; then
                    echo "  $_summary"
                fi
                echo ""
            done
        fi
    done

    echo "---"
    echo "*Generated: $(date '+%Y-%m-%d %H:%M') by VPS cron | Sources: RSS blogs*"

} > "$DIGEST_FILE"

log "Digest written: $DIGEST_FILE"

# --- Commit and push ---
if [ "$TOTAL" -gt 0 ]; then
    cd "$REPO_DIR"
    git add news-pipeline/data/digests/ news-pipeline/data/fetch.log news-pipeline/cache/ 2>/dev/null || true
    git commit -m "news-pipeline: fetch digest $TODAY ($TOTAL articles)

Co-Authored-By: VPS Cron <noreply@kubrik.dev>" --quiet 2>/dev/null || true

    git push --quiet 2>/dev/null && log "Pushed to repo" || log "WARNING: push failed"
else
    log "No articles found, skipping commit"
fi

log "=== KUBRIK News Fetch Complete ==="
