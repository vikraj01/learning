source "$LAB_DIR/../_lib/check.sh"
source "$LAB_DIR/../_lib/notes.sh"

if err=$(docker compose config -q 2>&1); then
  pass valid "Compose can read it."
else
  fail valid "Compose says: \`$(head -1 <<<"$err" | tr -d '`' | cut -c1-160)\`"
fi

notes_running
notes_page 3504

if cmp -s web/server.js "$LAB_DIR/starter/web/server.js" && cmp -s api/server.js "$LAB_DIR/starter/api/server.js"; then
  pass code "The code is untouched. All three fixes were in \`compose.yaml\`."
else
  fail code "\`web/server.js\` or \`api/server.js\` changed. Put them back; the mistakes are in \`compose.yaml\`."
fi
