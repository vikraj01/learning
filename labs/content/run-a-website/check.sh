source "$LAB_DIR/../_lib/check.sh"

# 1. running
if running hello-web; then
  pass running "\`hello-web\` is up."
elif exists hello-web; then
  fail running "\`hello-web\` exists but has stopped. \`docker ps -a\` shows it; \`docker logs hello-web\` says why."
else
  fail running "There's no container called \`hello-web\`. Did you use \`--name hello-web\`?"
fi

# 2. image
img=$(image_of hello-web)
if [[ "$img" == nginx* ]]; then
  pass image "It runs \`$img\`."
elif [ -n "$img" ]; then
  fail image "It runs \`$img\`, not nginx."
else
  fail image "No \`hello-web\` container to look at yet."
fi

# 3. port
if page http://localhost:8080 | grep -qi "welcome to nginx"; then
  pass port "Your browser can reach it on port 8080."
else
  door=$(docker port hello-web 2>/dev/null | head -1)
  if ! exists hello-web; then
    fail port "Nothing answers on \`localhost:8080\` yet."
  elif [ -z "$door" ]; then
    fail port "The container has no door to your laptop: it was started without \`-p\`."
  else
    fail port "A door is open, but it isn't 8080 → 80: \`$door\`."
  fi
fi
