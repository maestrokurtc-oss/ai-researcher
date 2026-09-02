#!/usr/bin/env bash
# Pull new briefings and raise a macOS notification for each one.
#
# Installed as a launchd agent by local/install.sh; it can also be run by hand.
# Safe to run when nothing has changed - it notifies only on briefings it has
# not already announced, tracked in local/.seen-briefings.

set -uo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SEEN_FILE="$REPO_DIR/local/.seen-briefings"
LOG_FILE="$REPO_DIR/local/poll.log"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOG_FILE"; }

# Keep the log from growing without bound.
if [ -f "$LOG_FILE" ] && [ "$(wc -c < "$LOG_FILE")" -gt 262144 ]; then
    tail -n 200 "$LOG_FILE" > "$LOG_FILE.tmp" && mv "$LOG_FILE.tmp" "$LOG_FILE"
fi

cd "$REPO_DIR" || { log "Repo directory is missing: $REPO_DIR"; exit 1; }

notify() {
    local title="$1" message="$2" file="$3"
    # terminal-notifier makes the notification clickable; osascript is the
    # fallback that is always present on macOS.
    if command -v terminal-notifier > /dev/null 2>&1; then
        terminal-notifier -title "$title" -message "$message" \
            -execute "open -R '$file'" -sound Glass > /dev/null 2>&1
    else
        # Escape double quotes and backslashes for AppleScript's string literal.
        local safe_title safe_message
        safe_title=$(printf '%s' "$title"   | sed 's/\\/\\\\/g; s/"/\\"/g')
        safe_message=$(printf '%s' "$message" | sed 's/\\/\\\\/g; s/"/\\"/g')
        osascript -e "display notification \"$safe_message\" with title \"$safe_title\" sound name \"Glass\"" \
            > /dev/null 2>&1
    fi
}

# A dirty worktree or local commits would make --ff-only fail; say so plainly
# rather than leaving the user wondering why briefings stopped arriving.
if ! git diff --quiet || ! git diff --staged --quiet; then
    log "Worktree has uncommitted changes; skipping the pull."
else
    if ! git fetch --quiet origin 2>>"$LOG_FILE"; then
        log "git fetch failed (offline?); will retry on the next tick."
        exit 0
    fi
    branch=$(git rev-parse --abbrev-ref HEAD)
    if ! git merge --ff-only "origin/$branch" --quiet 2>>"$LOG_FILE"; then
        log "Fast-forward onto origin/$branch failed; local commits may have diverged."
    fi
fi

touch "$SEEN_FILE"

# First run adopts whatever already exists rather than firing a burst of
# notifications for the entire back catalogue.
if [ ! -s "$SEEN_FILE" ]; then
    find briefings -name '*.md' -type f 2>/dev/null | sort > "$SEEN_FILE"
    log "Baseline recorded: $(wc -l < "$SEEN_FILE" | tr -d ' ') existing briefings."
    exit 0
fi

new_count=0
while IFS= read -r file; do
    [ -z "$file" ] && continue
    grep -Fxq "$file" "$SEEN_FILE" && continue

    base=$(basename "$file" .md)          # e.g. 2026-09-02-morning
    slot=${base##*-}
    date=${base%-*}
    case "$slot" in
        morning) label='아침 브리핑' ;;
        evening) label='저녁 브리핑' ;;
        *)       label='브리핑' ;;
    esac

    items=$(grep -c '^### ' "$file" 2>/dev/null || echo 0)
    headline=$(grep -m 1 '^### ' "$file" 2>/dev/null \
               | sed -E 's/^### \[([^]]*)\].*/\1/; s/^### //' \
               | cut -c1-90)

    notify "$label · ${date}" "${items}건${headline:+ — $headline}" "$REPO_DIR/$file"
    echo "$file" >> "$SEEN_FILE"
    log "Notified: $file ($items items)"
    new_count=$((new_count + 1))
done < <(find briefings -name '*.md' -type f 2>/dev/null | sort)

[ "$new_count" -eq 0 ] && log "No new briefings."
exit 0
