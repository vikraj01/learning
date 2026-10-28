source "$LAB_DIR/../_lib/check.sh"

img=$(image_of hello)
if running hello && [[ "$img" == greet-lab || "$img" == greet-lab:latest ]]; then
  pass running "\`hello\` is up, from \`greet-lab\`."
elif running hello; then
  fail running "\`hello\` was made from \`$img\`. Use the image \`greet-lab\`."
elif exists hello; then
  fail running "\`hello\` exists but stopped. \`docker logs hello\` says why."
else
  fail running "There's no container called \`hello\` yet."
fi

html=$(page http://localhost:3400/)
said=$(grep -o "Hello, [^!]*!" <<<"$html" | head -1)
if [ -z "$html" ]; then
  fail name "Nothing answers on \`localhost:3400\`. Door now: \`$(docker port hello 2>/dev/null | head -1)\`. It should be \`-p 3400:3000\`."
elif [ "$said" = "Hello, friend!" ]; then
  fail name "The page still says \`Hello, friend!\`. \`NAME\` isn't set: add \`-e NAME=...\`."
elif [ -n "$said" ]; then
  pass name "The page says \`$said\`"
else
  fail name "The page doesn't say hello at all."
fi

color=$(grep -o "color: [a-z]*" <<<"$html" | head -1 | cut -d' ' -f2)
if [ "$color" = "pink" ]; then
  pass color "Pink. Your \`-e COLOR=pink\` beat the image's \`ENV COLOR=lightblue\`."
elif [ -n "$color" ]; then
  fail color "The page is \`$color\`. Set \`-e COLOR=pink\`."
else
  fail color "Couldn't read the colour from the page yet."
fi

if cmp -s app.js "$LAB_DIR/starter/app.js" && cmp -s Dockerfile "$LAB_DIR/starter/Dockerfile"; then
  pass code "The code is untouched. All of it came from outside."
else
  fail code "\`app.js\` or the \`Dockerfile\` changed. Put them back; use \`-e\` instead."
fi
