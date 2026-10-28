source "$LAB_DIR/../_lib/check.sh"

file=$(ls compose.yaml compose.yml docker-compose.yaml docker-compose.yml 2>/dev/null | head -1)
if [ -z "$file" ]; then
  fail file "There's no \`compose.yaml\` yet."
elif err=$(docker compose config -q 2>&1); then
  pass file "Compose can read \`$file\`."
else
  fail file "Compose can't read \`$file\`: \`$(head -1 <<<"$err" | tr -d '`' | cut -c1-160)\`"
fi

if svc_running web; then
  pass web "\`web\` is running."
elif [ -n "$(svc web)" ]; then
  fail web "\`web\` stopped. \`docker compose logs web\` says why."
else
  fail web "No service \`web\` started from this folder yet: \`docker compose up -d\`."
fi

html=$(page http://localhost:3500/)
said=$(grep -o "Hello, [^!]*!" <<<"$html" | head -1)
color=$(grep -o "color: [a-z]*" <<<"$html" | head -1 | cut -d' ' -f2)
if [ -z "$html" ]; then
  fail page "Nothing answers on \`localhost:3500\`. \`ports:\` should have \`- \"3500:3000\"\`."
elif [ "$said" = "Hello, friend!" ]; then
  fail page "It says \`Hello, friend!\`: no \`NAME\` yet. Add it under \`environment:\`, then \`docker compose up -d\`."
elif [ "$color" != "pink" ]; then
  fail page "It says \`$said\`, but the page is \`$color\`. Add \`COLOR: pink\`."
else
  pass page "\`$said\` on pink."
fi

c=$(svc say)
if [ -z "$c" ]; then
  fail say "No service \`say\` has run yet."
elif docker logs "$c" 2>&1 | grep -q "^Hello, .*!$"; then
  pass say "\`say\` printed \`$(docker logs "$c" 2>&1 | grep -m1 '^Hello')\` and finished."
elif docker logs "$c" 2>&1 | grep -q "Saying hello"; then
  fail say "\`say\` started the web app. Give it \`command: [\"node\", \"say.js\"]\`."
else
  fail say "\`say\` printed nothing like hello. \`docker compose logs say\`."
fi
