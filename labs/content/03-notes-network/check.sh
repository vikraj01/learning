source "$LAB_DIR/../_lib/check.sh"

# 1. running
missing=""
for name in web api db; do running "$name" || missing="$missing $name"; done
if [ -z "$missing" ]; then
  pass running "All three are up."
else
  fail running "Not running:$(for m in $missing; do printf ' `%s`' "$m"; done). \`docker ps -a\` shows what happened."
fi

# 2. network: one network (not the default) that all three are on
shared=""
for net in $(networks_of web); do
  [ "$net" = "bridge" ] && continue
  if [[ " $(networks_of api) " == *" $net "* && " $(networks_of db) " == *" $net "* ]]; then
    shared="$net"
    break
  fi
done
if [ -n "$shared" ]; then
  pass network "All three share \`$shared\`."
else
  fail network "They don't share a network you made yet. web: \`$(networks_of web)\` · api: \`$(networks_of api)\` · db: \`$(networks_of db)\`"
fi

# 3. page
html=$(page http://localhost:3300/)
if [ -z "$html" ]; then
  fail page "Nothing answers on \`localhost:3300\`. Is \`web\` running with \`-p 3300:3000\`?"
elif grep -q "can't reach" <<<"$html"; then
  said=$(grep -o "<b>[^<]*</b>[^<]*" <<<"$html" | head -1 | sed 's/<[^>]*>//g' | tr -d '`')
  fail page "The page says: $said"
else
  pass page "The page opens with no error."
fi

# 4. note
if grep -q "<li>" <<<"$html"; then
  pass note "Your notes are in the list."
else
  fail note "No notes in the list yet."
fi
