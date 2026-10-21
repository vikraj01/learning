#!/usr/bin/env bash
# SessionStart: a short status block injected into Claude's context.
# Points Claude at new notes in plan/ so context/ never drifts behind.
set -u
root="${CLAUDE_PROJECT_DIR:-$(pwd)}"
cd "$root" || exit 0

log=context/progress.md
echo "## learning: session status"
echo "- Teaching Tanvi, slowly. Read context/README.md before non-trivial work."
echo "- git: $(git branch --show-current 2>/dev/null) @ $(git log -1 --format='%h %s' 2>/dev/null)"
docs=$(find docs -name '*.md' 2>/dev/null | wc -l)
echo "- docs/ pages: $docs"
echo "- skills: /sync-context /write-doc /excalidraw"

if [ -f "$log" ]; then
  newer=$(find plan -type f -newer "$log" 2>/dev/null | head -10)
  if [ -n "$newer" ]; then
    echo
    echo "## plan/ changed since context was last updated"
    echo "$newer" | sed 's/^/- /'
    echo "Read these and run /sync-context before anything else."
  fi
  echo
  echo "## Latest progress (context/progress.md, newest first)"
  awk '/<!-- entries below/{f=1;next} f' "$log" | head -20
fi
exit 0
