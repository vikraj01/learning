source "$LAB_DIR/../_lib/check.sh"

ep=$(docker image inspect -f '{{json .Config.Entrypoint}}' greet-ep 2>/dev/null)
cmd=$(docker image inspect -f '{{json .Config.Cmd}}' greet-ep 2>/dev/null)
if [ -z "$ep" ]; then
  fail image "There's no image called \`greet-ep\` yet."
elif [ "$ep" = '["node"]' ] && [ "$cmd" = '["app.js"]' ]; then
  pass image "\`greet-ep\`: ENTRYPOINT \`$ep\`, CMD \`$cmd\`."
else
  fail image "\`greet-ep\` has ENTRYPOINT \`$ep\` and CMD \`$cmd\`. It should be \`[\"node\"]\` and \`[\"app.js\"]\`. Save the Dockerfile and build again."
fi

html=$(page http://localhost:3405/)
if ! running ep-web; then
  fail web "There's no running container called \`ep-web\`."
elif [[ "$(image_of ep-web)" != greet-ep* ]]; then
  fail web "\`ep-web\` was made from \`$(image_of ep-web)\`. Use \`greet-ep\`."
elif grep -q "<h1>Hello," <<<"$html"; then
  pass web "\`node\` + \`app.js\`: the web page."
else
  fail web "Nothing answers on \`localhost:3405\`. It should be \`-p 3405:3000\`."
fi

logs=$(docker logs ep-say 2>&1)
if ! exists ep-say; then
  fail say "There's no container called \`ep-say\` yet (stopped ones count: \`docker ps -a\`)."
elif [[ "$(image_of ep-say)" != greet-ep* ]]; then
  fail say "\`ep-say\` was made from \`$(image_of ep-say)\`. Use \`greet-ep\`."
elif grep -q "Hello, Asha!" <<<"$logs"; then
  pass say "\`node\` + \`say.js\`: \`Hello, Asha!\`"
elif grep -q "/app/node" <<<"$logs"; then
  fail say "It ran \`node node say.js\`: \`node\` is already the ENTRYPOINT. Give only \`say.js\` after the image name."
else
  fail say "\`ep-say\` printed \`$(head -1 <<<"$logs")\`. Did you give it \`-e NAME=Asha\` and \`say.js\`?"
fi

want=$(docker run --rm greet-ep --version 2>/dev/null)
got=$(tr -d ' \r\n' < version.txt 2>/dev/null)
if [ -z "$got" ]; then
  fail version "\`version.txt\` is empty or missing."
elif [ -n "$want" ] && [ "$got" = "$want" ]; then
  pass version "Node \`$want\`, asked with \`--version\` through the ENTRYPOINT."
else
  fail version "\`version.txt\` says \`$got\`, but the image has \`${want:-?}\`."
fi
