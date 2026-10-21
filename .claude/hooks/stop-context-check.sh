#!/usr/bin/env bash
# Stop: keep context/ fresh. If plan/, docs/ or .claude/ changed after
# context/progress.md was last written, ask Claude (once) to update context.
#
# Never twice in a row (stop_hook_active), so it cannot loop. Writing the
# progress log makes it go quiet.
set -u
input=$(cat)
[ "$(jq -r '.stop_hook_active // false' <<<"$input")" = "true" ] && exit 0
root="${CLAUDE_PROJECT_DIR:-$(pwd)}"
cd "$root" || exit 0
log=context/progress.md
[ -f "$log" ] || exit 0

newer=$(find plan docs .claude CLAUDE.md -type f -newer "$log" 2>/dev/null | head -8)
[ -z "$newer" ] && exit 0

jq -n --arg files "$newer" '{
  decision: "block",
  reason: ("These changed since context/progress.md was last updated: " + ($files | gsub("\n"; ", ")) + ". Before stopping: record anything new about Tanvi, the plan or teaching style in the right context/ file, refresh \"Current state\" in context/README.md if it moved, and add a short entry to context/progress.md (done / state / next). If nothing worth recording happened, add a one-line note to the log.")
}'
exit 0
