# Shared checks for the Compose labs with the notes app (web, api, db).
# Needs check.sh sourced first. Prints the `running`, `page` and `note` lines.

notes_running() {
  local missing="" s
  for s in web api db; do svc_running "$s" || missing="$missing $s"; done
  if [ -z "$missing" ]; then
    pass running "\`web\`, \`api\` and \`db\` are up."
  else
    fail running "Not running:$(for m in $missing; do printf ' `%s`' "$m"; done). \`docker compose ps -a\` and \`docker compose logs <service>\` say why."
  fi
}

# notes_page <port>: sets NOTES_HTML for later checks.
notes_page() {
  NOTES_HTML=$(page "http://localhost:$1/")
  if [ -z "$NOTES_HTML" ]; then
    fail page "Nothing answers on \`localhost:$1\`. \`web\` needs \`ports:\` \`- \"$1:3000\"\` (the app listens on 3000)."
  elif grep -q "can't reach" <<<"$NOTES_HTML"; then
    local said
    said=$(grep -o "<b>[^<]*</b>[^<]*" <<<"$NOTES_HTML" | head -1 | sed 's/<[^>]*>//g' | tr -d '`')
    fail page "The page says: $said"
  else
    pass page "The page opens with no error."
  fi
  if grep -q "<li>" <<<"$NOTES_HTML"; then
    pass note "Your notes are in the list."
  else
    fail note "No notes in the list yet."
  fi
}
