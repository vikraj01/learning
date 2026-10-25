source "$LAB_DIR/../_lib/check.sh"

if [ ! -f Dockerfile ]; then
  if ls | grep -qi '^dockerfile'; then
    fail file "There's a file, but its name must be exactly \`Dockerfile\`: capital D, no extension."
  else
    fail file "There's no \`Dockerfile\` in this folder yet."
  fi
elif grep -qiE '^\s*FROM\s+node' Dockerfile; then
  pass file "\`Dockerfile\` found, starting $(grep -iE '^\s*FROM' Dockerfile | head -1 | xargs | sed 's/^/from `/; s/$/`/')."
else
  fail file "The Dockerfile should start with a \`FROM node:...\` line."
fi

if docker image inspect my-box >/dev/null 2>&1; then
  pass build "The image \`my-box\` is built."
else
  fail build "There's no image called \`my-box\` yet."
fi

img=$(image_of my-box)
if running my-box && [ "$img" = "my-box" ]; then
  pass running "\`my-box\` is up and staying up."
elif exists my-box && [ "$img" != "my-box" ]; then
  fail running "The container was made from \`$img\`, not from \`my-box\`."
elif exists my-box; then
  last=$(docker logs my-box 2>&1 | grep -m1 -iE "error" | cut -c1-120)
  fail running "\`my-box\` stopped right after starting. \`docker logs my-box\` says: \`${last:-(nothing)}\`"
else
  fail running "There's no container called \`my-box\`."
fi

if page http://localhost:8096/web | grep -q "Message box"; then
  pass page "The message box opens on port 8096. You wrote a working Dockerfile!"
else
  door=$(docker port my-box 2>/dev/null | head -1)
  fail page "Nothing answers on \`localhost:8096/web\` yet. Door: \`${door:-none}\`"
fi
