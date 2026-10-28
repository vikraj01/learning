source "$LAB_DIR/../_lib/check.sh"

if ! exists say-ravi; then
  fail ravi "There's no container called \`say-ravi\` yet (stopped ones count too: \`docker ps -a\`)."
elif [[ "$(image_of say-ravi)" != greet-cmd* ]]; then
  fail ravi "\`say-ravi\` was made from \`$(image_of say-ravi)\`. Use \`greet-cmd\`."
elif docker logs say-ravi 2>&1 | grep -q "Hello, Ravi!"; then
  pass ravi "\`say-ravi\` printed \`Hello, Ravi!\` and finished."
elif docker logs say-ravi 2>&1 | grep -q "Saying hello"; then
  fail ravi "\`say-ravi\` started the web app (the \`CMD\`). Put \`node say.js\` after the image name."
else
  fail ravi "\`say-ravi\` printed \`$(docker logs say-ravi 2>&1 | head -1)\`. Did you give it \`-e NAME=Ravi\`?"
fi

cmd=$(docker image inspect -f '{{json .Config.Cmd}}' sayer 2>/dev/null)
if [ -z "$cmd" ]; then
  fail sayer "There's no image called \`sayer\` yet."
elif [[ "$cmd" == *say.js* ]] && docker run --rm sayer 2>&1 | grep -q "Hello, friend!"; then
  pass sayer "\`sayer\`'s default is \`$cmd\`: it says hello and stops."
else
  fail sayer "\`sayer\`'s \`CMD\` is \`$cmd\`. Change the last line of the Dockerfile to \`CMD [\"node\", \"say.js\"]\`, save, and build again."
fi

html=$(page http://localhost:3404/)
if ! running sayer-web; then
  fail web "There's no running container called \`sayer-web\`. If it stopped right away, it ran \`say.js\`: give it \`node app.js\` after the image name."
elif [[ "$(image_of sayer-web)" != sayer* ]]; then
  fail web "\`sayer-web\` was made from \`$(image_of sayer-web)\`. Use \`sayer\`."
elif grep -q "<h1>Hello," <<<"$html"; then
  pass web "The web page, from an image whose default is \`say.js\`. The command line won."
else
  fail web "Nothing answers on \`localhost:3404\`. It should be \`-p 3404:3000\`."
fi
