source "$LAB_DIR/../_lib/check.sh"
source "$LAB_DIR/../_lib/notes.sh"

web=$(svc web); api=$(svc api); db=$(svc db)
api_nets=$(networks_of "$api"); web_nets=$(networks_of "$web"); db_nets=$(networks_of "$db")

n=$(wc -w <<<"$api_nets")
if [ -z "$api" ]; then
  fail api "There's no \`api\` service running from this folder."
elif [ "$n" -ge 2 ]; then
  pass api "\`api\` is on \`$api_nets\`."
else
  fail api "\`api\` is only on \`${api_nets:-nothing}\`. Give it \`networks:\` \`- front\` and \`- back\`, then \`docker compose up -d\`."
fi

shared=""
for net in $web_nets; do [[ " $db_nets " == *" $net "* ]] && shared="$shared $net"; done
if [ -z "$web" ] || [ -z "$db" ]; then
  fail private "\`web\` or \`db\` isn't there. \`docker compose up -d\`."
elif [ -z "$shared" ]; then
  pass private "\`web\` (\`$web_nets\`) and \`db\` (\`$db_nets\`) share nothing. The pantry is out of sight."
else
  fail private "\`web\` and \`db\` are both on \`$(xargs <<<"$shared")\`. web: \`$web_nets\` · db: \`$db_nets\`"
fi

notes_page 3503
