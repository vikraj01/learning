source "$LAB_DIR/../_lib/check.sh"

if running squatter && docker port squatter 2>/dev/null | grep -q ":8093"; then
  pass squatter "\`squatter\` still holds port 8093."
elif exists squatter; then
  fail squatter "\`squatter\` isn't running. Start it again: \`docker start squatter\`."
else
  fail squatter "\`squatter\` is gone. Press Reset to start this lab over."
fi

if running shop && page http://localhost:8094 | grep -qi "welcome to nginx"; then
  pass shop "\`shop\` opens on port 8094."
elif running shop; then
  door=$(docker port shop 2>/dev/null | head -1)
  fail shop "\`shop\` is running, but its door is \`${door:-none}\`, not 8094."
elif exists shop; then
  fail shop "\`shop\` exists but isn't running: it's left over from the try that failed. Remove it with \`docker rm shop\`, then run it again on 8094."
else
  fail shop "There's no container called \`shop\` yet."
fi
