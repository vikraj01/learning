source "$LAB_DIR/../_lib/check.sh"

want_name=$(sed -n 's/^NAME=//p' .env 2>/dev/null | tail -1)
want_color=$(sed -n 's/^COLOR=//p' .env 2>/dev/null | tail -1)
got_name=$(env_of from-file NAME)
got_color=$(env_of from-file COLOR)

if ! running from-file; then
  fail file "There's no running container called \`from-file\`."
elif [[ "$(image_of from-file)" != greet-lab* ]]; then
  fail file "\`from-file\` was made from \`$(image_of from-file)\`. Use \`greet-lab\`."
elif [ "$got_name" = "$want_name" ] && [ "$got_color" = "$want_color" ]; then
  pass file "\`from-file\` has \`NAME=$got_name\` and \`COLOR=$got_color\`, same as \`.env\`."
elif [ -z "$got_name" ]; then
  fail file "\`from-file\` has no \`NAME\` at all. Did you add \`--env-file .env\`?"
else
  fail file "\`from-file\` has \`NAME=$got_name\`, \`COLOR=$got_color\`, but \`.env\` says \`NAME=$want_name\`, \`COLOR=$want_color\`. Was it made before you changed the file?"
fi

html=$(page http://localhost:3401/)
if [ -z "$html" ]; then
  fail page "Nothing answers on \`localhost:3401\`. It should be \`-p 3401:3000\`."
elif grep -q "Hello, $want_name!" <<<"$html" && grep -q "color: $want_color" <<<"$html"; then
  pass page "The page says \`Hello, $want_name!\` on \`$want_color\`."
else
  fail page "The page shows \`$(grep -o "Hello, [^!]*!" <<<"$html" | head -1)\` on \`$(grep -o "color: [a-z]*" <<<"$html" | head -1 | cut -d' ' -f2)\`, not what \`.env\` says."
fi

if [ "$want_color" != "lightgreen" ]; then
  fail changed "\`.env\` still says \`COLOR=$want_color\`. Change it to \`lightgreen\` and save."
elif grep -q "color: lightgreen" <<<"$html"; then
  pass changed "Light green. A new container read the new file."
elif [ -n "$got_color" ]; then
  fail changed "The file says \`lightgreen\`, but \`from-file\` still has \`COLOR=$got_color\`. It read the file when it was made: remove it and run it again."
else
  fail changed "The page isn't light green yet."
fi
