source "$LAB_DIR/../_lib/check.sh"
source "$LAB_DIR/../_lib/notes.sh"

want=$(sed -n 's/^DB_PASSWORD=//p' .env 2>/dev/null | tail -1 | tr -d '\r"'"'")
if [ ! -f .env ]; then
  fail envfile "There's no \`.env\` next to \`compose.yaml\` yet."
elif [ -z "$want" ]; then
  fail envfile "\`.env\` has no \`DB_PASSWORD=...\` line."
elif [ "$want" = "secret" ]; then
  fail envfile "\`.env\` still says \`secret\`. Pick a new password."
else
  pass envfile "\`.env\` has a new password."
fi

uses=$(grep -cE '\$\{DB_PASSWORD(:-[^}]*)?\}' compose.yaml 2>/dev/null)
if grep -qw secret compose.yaml; then
  fail yaml "\`compose.yaml\` still has \`secret\` in it."
elif [ "${uses:-0}" -ge 2 ]; then
  pass yaml "\`compose.yaml\` only says \`\${DB_PASSWORD}\`."
else
  fail yaml "\`\${DB_PASSWORD}\` should be in two places: under \`api\` and under \`db\`."
fi

api_pw=$(env_of "$(svc api)" DB_PASSWORD)
db_pw=$(env_of "$(svc db)" POSTGRES_PASSWORD)
if [ -z "$(svc api)" ] || [ -z "$(svc db)" ]; then
  fail same "\`api\` or \`db\` isn't there. \`docker compose up -d\`."
elif [ -n "$want" ] && [ "$api_pw" = "$want" ] && [ "$db_pw" = "$want" ]; then
  pass same "\`api\` and \`db\` both got the password from \`.env\`."
elif [ "$api_pw" = "secret" ] || [ "$db_pw" = "secret" ]; then
  fail same "A container still has the old password. Run \`docker compose up -d\` after saving both files."
else
  fail same "\`api\` and \`db\` don't have the password from \`.env\`. Save both files and \`docker compose up -d\`."
fi

notes_page 3502
