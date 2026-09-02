#!/usr/bin/env bash
# Install (or reinstall) the launchd agent that polls for new briefings.
#
#   ./local/install.sh            install and start
#   ./local/install.sh --uninstall  stop and remove
#
# The agent runs local/poll-briefings.sh every 30 minutes while you are logged
# in. launchd runs a missed interval once shortly after the Mac wakes, so a
# briefing that lands while the machine is asleep still reaches you.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LABEL="com.maestrokurtc.ai-researcher.poll"
PLIST="$HOME/Library/LaunchAgents/${LABEL}.plist"
INTERVAL="${POLL_INTERVAL_SECONDS:-1800}"

if [ "${1:-}" = "--uninstall" ]; then
    launchctl bootout "gui/$(id -u)/${LABEL}" 2>/dev/null || true
    rm -f "$PLIST"
    echo "Removed the launchd agent (${LABEL})."
    exit 0
fi

mkdir -p "$HOME/Library/LaunchAgents"

# The repo path contains spaces, so every path goes in its own array element -
# never a single shell string.
cat > "$PLIST" <<PLIST_EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>${LABEL}</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>${REPO_DIR}/local/poll-briefings.sh</string>
    </array>
    <key>WorkingDirectory</key>
    <string>${REPO_DIR}</string>
    <key>StartInterval</key>
    <integer>${INTERVAL}</integer>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>${REPO_DIR}/local/launchd.out.log</string>
    <key>StandardErrorPath</key>
    <string>${REPO_DIR}/local/launchd.err.log</string>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
    </dict>
</dict>
</plist>
PLIST_EOF

plutil -lint "$PLIST" > /dev/null

# bootout first so a rerun replaces the old definition instead of erroring.
launchctl bootout "gui/$(id -u)/${LABEL}" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"

echo "Installed ${LABEL}"
echo "  polls every $((INTERVAL / 60)) minutes"
echo "  plist:  $PLIST"
echo "  log:    ${REPO_DIR}/local/poll.log"
echo
echo "Check it with:  launchctl print gui/$(id -u)/${LABEL} | head -20"
echo "Remove it with: ./local/install.sh --uninstall"
