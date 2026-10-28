source "$LAB_DIR/../_lib/check.sh"

img_env() { docker image inspect -f '{{range .Config.Env}}{{println .}}{{end}}' "$1" 2>/dev/null | sed -n "s/^$2=//p"; }
img_cmd() { docker image inspect -f '{{json .Config.Cmd}}' "$1" 2>/dev/null; }

if ! cmp -s Dockerfile "$LAB_DIR/starter/Dockerfile"; then
  fail prod "\`Dockerfile\` was changed. Keep it as it was (the dev changes go in \`Dockerfile.dev\`)."
elif ! docker image inspect greet-f:1.0 >/dev/null 2>&1; then
  fail prod "There's no \`greet-f:1.0\` yet."
elif [ "$(img_env greet-f:1.0 COLOR)" = "lightblue" ] && [ "$(img_cmd greet-f:1.0)" = '["app.js"]' ]; then
  pass prod "\`greet-f:1.0\`: light blue, plain \`app.js\`. The real one."
else
  fail prod "\`greet-f:1.0\` has \`COLOR=$(img_env greet-f:1.0 COLOR)\` and CMD \`$(img_cmd greet-f:1.0)\`: it was built from \`Dockerfile.dev\`. Build it again without \`-f\`."
fi

if [ ! -f Dockerfile.dev ]; then
  fail dev "There's no \`Dockerfile.dev\` yet."
elif ! docker image inspect greet-f:dev >/dev/null 2>&1; then
  fail dev "There's no \`greet-f:dev\` yet: \`docker build -f Dockerfile.dev -t greet-f:dev .\`"
elif [ "$(img_env greet-f:dev COLOR)" = "lightyellow" ] && [[ "$(img_cmd greet-f:dev)" == *--watch* ]]; then
  pass dev "\`greet-f:dev\`: light yellow, with \`--watch\`."
else
  fail dev "\`greet-f:dev\` has \`COLOR=$(img_env greet-f:dev COLOR)\` and CMD \`$(img_cmd greet-f:dev)\`. Check \`Dockerfile.dev\`, save, and build it again with \`-f Dockerfile.dev\`."
fi

src=$(docker inspect -f '{{range .Mounts}}{{if eq .Destination "/app"}}{{.Source}}{{end}}{{end}}' greet-dev 2>/dev/null)
html=$(page http://localhost:3406/)
if ! running greet-dev; then
  fail running "There's no running container called \`greet-dev\`."
elif [ "$(image_of greet-dev)" != "greet-f:dev" ]; then
  fail running "\`greet-dev\` runs \`$(image_of greet-dev)\`. It should run \`greet-f:dev\`."
elif [ "$(realpath "$src" 2>/dev/null)" != "$(realpath "$LAB_WORKSPACE")" ]; then
  fail running "\`greet-dev\` doesn't have this folder on \`/app\`. Add \`-v \"\$(pwd)\":/app\` (run it from this lab's folder)."
elif grep -q "color: lightyellow" <<<"$html"; then
  pass running "Light yellow on 3406, with your folder inside."
else
  fail running "Nothing light yellow on \`localhost:3406\`. It should be \`-p 3406:3000\`."
fi

if ! grep -q "<h1>Hi," app.js; then
  fail live "\`app.js\` doesn't say \`<h1>Hi,\` yet. Change \`Hello\` to \`Hi\` and save."
elif grep -q "<h1>Hi," <<<"$html"; then
  pass live "The page says Hi. You saved, \`--watch\` restarted the app, no rebuild."
else
  fail live "\`app.js\` says Hi, but the page doesn't. Is \`greet-dev\` running with the bind mount and \`--watch\`? \`docker logs greet-dev\`."
fi
