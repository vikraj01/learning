source "$LAB_DIR/../_lib/check.sh"

secret=$(sed -n 's/^DB_PASSWORD=//p' "$LAB_DIR/starter/.env")
found=$(tr -d ' \r\n' < found.txt 2>/dev/null)
if [ "$found" = "$secret" ]; then
  pass found "You found it: \`$secret\`. Anyone with the \`leaky\` image could."
elif [ -z "$found" ]; then
  fail found "\`found.txt\` is empty or missing."
else
  fail found "\`found.txt\` says \`$found\`. That's not the password in the image."
fi

if [ -f .dockerignore ] && grep -qE '^\s*(/?\.env\*?|\*\.env|\.env.*)\s*$' .dockerignore; then
  pass ignore "\`.dockerignore\` leaves \`.env\` out."
elif [ -f .dockerignore ]; then
  fail ignore "\`.dockerignore\` exists, but has no \`.env\` line."
elif ls -a | grep -qi 'dockerignore'; then
  fail ignore "The file must be called exactly \`.dockerignore\`, starting with a dot."
else
  fail ignore "There's no \`.dockerignore\` yet."
fi

if ! docker image inspect greet-clean >/dev/null 2>&1; then
  fail clean "There's no image called \`greet-clean\` yet."
elif docker run --rm greet-clean test -e /app/.env >/dev/null 2>&1; then
  fail clean "\`greet-clean\` still has \`/app/.env\` inside. Save \`.dockerignore\` first, then build again."
else
  pass clean "\`greet-clean\` has no \`.env\` inside. Nothing to steal."
fi

html=$(page http://localhost:3402/)
if ! running clean; then
  fail running "There's no running container called \`clean\`."
elif [[ "$(image_of clean)" != greet-clean* ]]; then
  fail running "\`clean\` was made from \`$(image_of clean)\`. Use \`greet-clean\`."
elif grep -q "Hello, Tanvi!" <<<"$html" && grep -q "color: pink" <<<"$html"; then
  pass running "Tanvi on pink, with the settings handed in from outside."
elif [ -z "$html" ]; then
  fail running "Nothing answers on \`localhost:3402\`. It should be \`-p 3402:3000\`."
else
  fail running "The page isn't Tanvi on pink. The image has no \`.env\` now, so hand it in: \`--env-file .env\`."
fi
