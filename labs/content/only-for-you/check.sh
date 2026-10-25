source "$LAB_DIR/../_lib/check.sh"

if running private-site && [[ "$(image_of private-site)" == nginx* ]]; then
  pass running "\`private-site\` is up."
elif exists private-site; then
  fail running "\`private-site\` exists, but it isn't a running nginx."
else
  fail running "There's no container called \`private-site\`."
fi

if page http://localhost:8095 | grep -qi "welcome to nginx"; then
  pass page "It opens on port 8095."
else
  fail page "Nothing answers on \`localhost:8095\` yet."
fi

doors=$(docker port private-site 80 2>/dev/null | xargs)
if [ -z "$doors" ]; then
  fail only "There's no door to check yet."
elif [ "$doors" = "127.0.0.1:8095" ]; then
  pass only "The door is \`127.0.0.1:8095\`: only this laptop can use it."
else
  fail only "The door is \`$doors\`. \`0.0.0.0\` (or \`[::]\`) means anyone who can reach your laptop."
fi
