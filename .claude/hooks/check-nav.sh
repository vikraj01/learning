#!/usr/bin/env bash
# Stop: every page in docs/ must be wired into the site. Each .md under docs/
# has to be in mkdocs.yml `nav` and linked from docs/README.md (the index).
# Blocks once with the list of unwired pages; never twice in a row.
set -u
input=$(cat)
[ "$(jq -r '.stop_hook_active // false' <<<"$input")" = "true" ] && exit 0
root="${CLAUDE_PROJECT_DIR:-$(pwd)}"
cd "$root" || exit 0
[ -f mkdocs.yml ] || exit 0

missing=""
while IFS= read -r f; do
  page=${f#docs/}
  [ "$page" = "README.md" ] && continue
  grep -qF -- "$page" mkdocs.yml || missing+="$page (not in mkdocs.yml nav)"$'\n'
  grep -qF -- "($page" docs/README.md || missing+="$page (not linked from docs/README.md)"$'\n'
done < <(find docs -name '*.md' -not -path '*/node_modules/*' | sort)

[ -z "$missing" ] && exit 0
jq -n --arg m "$missing" '{
  decision: "block",
  reason: ("Every docs/ page must be wired into the site. Fix these before stopping:\n" + $m + "Add each page to nav in mkdocs.yml (in reading order, under its section) and link it from docs/README.md.")
}'
exit 0
