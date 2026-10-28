source "$LAB_DIR/../_lib/check.sh"

id_of() { docker image inspect -f '{{.Id}}' "$1" 2>/dev/null; }
h1_of() { docker run --rm "$1" grep -o '<h1>[A-Za-z]*' app.js 2>/dev/null | sed 's/<h1>//'; }

one=$(id_of greet-tags:1.0); two=$(id_of greet-tags:2.0); latest=$(id_of greet-tags:latest)

if [ -z "$one" ]; then
  fail one "There's no \`greet-tags:1.0\` yet."
elif [ "$(h1_of greet-tags:1.0)" = "Hello" ]; then
  pass one "\`greet-tags:1.0\` says Hello."
else
  fail one "\`greet-tags:1.0\` says \`$(h1_of greet-tags:1.0)\`, not Hello. It was built after the change. Put \`Hello\` back, build 1.0 again, then redo 2.0."
fi

if [ -z "$two" ]; then
  fail two "There's no \`greet-tags:2.0\` yet."
elif [ "$(h1_of greet-tags:2.0)" = "Welcome" ]; then
  pass two "\`greet-tags:2.0\` says Welcome."
else
  fail two "\`greet-tags:2.0\` says \`$(h1_of greet-tags:2.0)\`. Change \`Hello\` to \`Welcome\` in \`app.js\`, save, and build 2.0 again."
fi

if [ -z "$latest" ]; then
  fail latest "There's no \`greet-tags:latest\` yet."
elif [ -n "$two" ] && [ "$latest" = "$two" ]; then
  pass latest "\`latest\` and \`2.0\` are two names for the same image."
else
  fail latest "\`greet-tags:latest\` is a different image from \`2.0\`. Point it there with \`docker tag\`."
fi

html=$(page http://localhost:3403/)
if ! running v1; then
  fail old "There's no running container called \`v1\`."
elif [ "$(image_of v1)" != "greet-tags:1.0" ]; then
  fail old "\`v1\` runs \`$(image_of v1)\`. It should run \`greet-tags:1.0\`."
elif grep -q "<h1>Hello," <<<"$html"; then
  pass old "Version 1.0 is running and still says Hello. Going back is easy."
else
  fail old "Nothing saying Hello on \`localhost:3403\`. It should be \`-p 3403:3000\`."
fi
