#!/usr/bin/env bash
# Common functions for kubrik-news skill

set -e
export LC_ALL=en_US.UTF-8

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
CONFIG_FILE="$SKILL_DIR/config/.env"
DATA_DIR="$SKILL_DIR/data"
CACHE_DIR="$SKILL_DIR/cache"
SEEN_FILE="$DATA_DIR/seen.json"

# telegram-channel-parser (optional, may not exist in remote env)
TG_PARSER_DIR="$HOME/.claude/skills/telegram-channel-parser"

REQUEST_DELAY="1.5"

# Detect OS for date command compatibility
IS_MACOS=false
if [ "$(uname)" = "Darwin" ]; then
    IS_MACOS=true
fi

load_config() {
    if [ -f "$CONFIG_FILE" ]; then
        . "$CONFIG_FILE"
    else
        echo "Warning: no config/.env found. Copy config/.env.example to config/.env" >&2
    fi
}

ensure_dirs() {
    mkdir -p "$DATA_DIR/digests" "$CACHE_DIR"
}

ensure_seen() {
    if [ ! -f "$SEEN_FILE" ]; then
        echo '{}' > "$SEEN_FILE"
    fi
}

# Portable SHA-256 hash (works on both Linux and macOS)
portable_sha256() {
    echo -n "$1" | (sha256sum 2>/dev/null || shasum -a 256) | cut -c1-"${2:-16}"
}

# Generate a hash for dedup (URL-based)
hash_url() {
    portable_sha256 "$1" 16
}

# Check if URL hash already seen
is_seen() {
    local hash
    hash=$(hash_url "$1")
    if [ -f "$SEEN_FILE" ]; then
        # Simple grep check in JSON
        grep -q "\"$hash\"" "$SEEN_FILE" 2>/dev/null && return 0
    fi
    return 1
}

# Mark URL as seen
mark_seen() {
    local url="$1"
    local hash
    hash=$(hash_url "$url")
    local today
    today=$(date +%Y-%m-%d)

    if [ ! -f "$SEEN_FILE" ] || [ ! -s "$SEEN_FILE" ]; then
        echo "{\"$hash\":\"$today\"}" > "$SEEN_FILE"
    else
        local content
        content=$(cat "$SEEN_FILE")
        if echo "$content" | grep -q '"' 2>/dev/null; then
            # Cross-platform sed -i
            if $IS_MACOS; then
                sed -i '' "s/}$/,\"$hash\":\"$today\"}/" "$SEEN_FILE"
            else
                sed -i "s/}$/,\"$hash\":\"$today\"}/" "$SEEN_FILE"
            fi
        else
            echo "{\"$hash\":\"$today\"}" > "$SEEN_FILE"
        fi
    fi
}

# Portable sed: split XML closing/opening tags onto separate lines
# Works on both GNU sed (Linux) and BSD sed (macOS)
split_xml_tags() {
    sed $'s/></>\\\n</g' "$1"
}

# HTTP fetch with rate limiting
web_fetch() {
    sleep "$REQUEST_DELAY"
    curl -sL \
        -H "Accept-Language: en-US,en;q=0.9,ru;q=0.5" \
        -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" \
        --max-time 15 \
        "$1"
}

# Get cutoff date N days ago (ISO format, cross-platform)
days_ago_iso() {
    local n="${1:-7}"
    if $IS_MACOS; then
        date -v-"${n}d" +%Y-%m-%d
    else
        date -d "$n days ago" +%Y-%m-%d
    fi
}

parse_common_params() {
    PERIOD=""
    PLATFORM=""
    NO_DEDUP=""
    OUTPUT_FILE=""

    while [ $# -gt 0 ]; do
        case "$1" in
            --period)    PERIOD="$2"; shift 2 ;;
            --platform)  PLATFORM="$2"; shift 2 ;;
            --no-dedup)  NO_DEDUP="1"; shift ;;
            --output)    OUTPUT_FILE="$2"; shift 2 ;;
            *)           shift ;;
        esac
    done

    # Defaults
    PERIOD="${PERIOD:-${NEWS_DIGEST_PERIOD:-7}}"
}
