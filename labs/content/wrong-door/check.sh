source "$LAB_DIR/../_lib/check.sh"

if page http://localhost:8098 | grep -q "Quiet app"; then
  pass page "The page opens: the laptop's 8098 now leads to the app's real door, 5000."
else
  door=$(docker port quiet 2>/dev/null | head -1)
  fail page "Nothing answers yet. The door now is: \`${door:-none}\`. What does \`docker logs quiet\` say?"
fi

if running quiet && [ "$(image_of quiet)" = "quiet-app" ]; then
  pass running "\`quiet\` runs \`quiet-app\`."
else
  fail running "There's no running container called \`quiet\` made from \`quiet-app\`."
fi

if grep -qE 'PORT\s*=\s*5000' app.js 2>/dev/null; then
  pass code "\`app.js\` is unchanged."
else
  fail code "\`app.js\` was changed. The fix belongs in \`docker run\`."
fi
