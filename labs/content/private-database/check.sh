source "$LAB_DIR/../_lib/check.sh"
on() { [[ " $(networks_of "$1") " == *" $2 "* ]]; }

missing=""
for n in front-net back-net; do docker network inspect "$n" >/dev/null 2>&1 || missing="$missing \`$n\`"; done
if [ -z "$missing" ]; then pass networks "Both networks exist."; else fail networks "Missing:$missing"; fi

if on api front-net && on api back-net; then
  pass api "\`api\` is on \`front-net\` and \`back-net\`."
else
  fail api "\`api\` is on: \`$(networks_of api)\`. It needs both \`front-net\` and \`back-net\`."
fi

shared=""
for n in $(networks_of web); do on db "$n" && shared="$shared \`$n\`"; done
if ! running web || ! running db; then
  fail private "\`web\` and \`db\` both need to be running."
elif [ -z "$shared" ]; then
  pass private "\`web\` can't reach \`db\` any more. The database is private."
else
  fail private "\`web\` and \`db\` still share:$shared"
fi

html=$(page http://localhost:3301/)
if [ -z "$html" ]; then
  fail page "Nothing answers on \`localhost:3301\`."
elif grep -q "can't reach" <<<"$html"; then
  said=$(grep -o "<b>[^<]*</b>[^<]*" <<<"$html" | head -1 | sed 's/<[^>]*>//g' | tr -d '`')
  fail page "The page says: $said"
else
  pass page "The notes app still works."
fi
