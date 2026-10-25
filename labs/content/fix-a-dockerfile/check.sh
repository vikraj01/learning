source "$LAB_DIR/../_lib/check.sh"

# 1. build
if docker image inspect message-box-fixed >/dev/null 2>&1; then
  pass build "The image \`message-box-fixed\` is built."
else
  fail build "There's no image called \`message-box-fixed\` yet. Build it from this folder with \`docker build -t message-box-fixed .\`"
fi

# 2. running
img=$(image_of box)
if running box && [ "$img" = "message-box-fixed" ]; then
  pass running "\`box\` is up and staying up."
elif exists box && [ "$img" != "message-box-fixed" ]; then
  fail running "\`box\` was made from \`$img\`, not \`message-box-fixed\`."
elif exists box; then
  last=$(docker logs box 2>&1 | grep -m1 -E "Error|error" | cut -c1-120)
  fail running "\`box\` stopped right after it started. \`docker logs box\` says: \`${last:-(nothing)}\`"
else
  fail running "There's no container called \`box\`."
fi

# 3. page
if page http://localhost:8081/web | grep -q "Message box"; then
  pass page "The message box opens on port 8081."
else
  door=$(docker port box 2>/dev/null | head -1)
  if running box && [ -z "$door" ]; then
    fail page "\`box\` has no door to your laptop: it was started without \`-p\`."
  elif running box; then
    fail page "Nothing answers on \`localhost:8081/web\`. The door is \`$door\`: is it 8081 → 8080?"
  else
    fail page "Nothing answers on \`localhost:8081/web\` yet."
  fi
fi
