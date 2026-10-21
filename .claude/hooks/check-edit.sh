#!/usr/bin/env bash
# PostToolUse(Edit|Write): validate what was just written.
#   .excalidraw   -> draw.py --check (valid scene, bindings, not too busy)
#   .claude/*.json -> valid JSON
# Problems go back to Claude on stderr with exit 2; clean files are silent.
set -u
file=$(jq -r '.tool_input.file_path // ""')
[ -f "$file" ] || exit 0
root="${CLAUDE_PROJECT_DIR:-$(pwd)}"

case "$file" in
  *.excalidraw)
    out=$(python3 -I "$root/.claude/skills/excalidraw/draw.py" --check "$file" 2>&1) || {
      echo "$out" >&2
      exit 2
    }
    ;;
  */.claude/*.json)
    out=$(jq empty "$file" 2>&1) || {
      echo "Invalid JSON in $file: $out" >&2
      exit 2
    }
    ;;
esac
exit 0
