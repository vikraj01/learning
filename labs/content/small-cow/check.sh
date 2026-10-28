source "$LAB_DIR/../_lib/check.sh"

froms=$(grep -ciE '^\s*FROM\s' Dockerfile 2>/dev/null)
if [ "${froms:-0}" -ge 2 ] && grep -qiE '^\s*COPY\s+--from=' Dockerfile; then
  pass stages "$froms stages, and the last one copies from an earlier one."
elif [ "${froms:-0}" -ge 2 ]; then
  fail stages "Two \`FROM\`s, but nothing comes across. Add \`COPY --from=build /src/cow /cow\` in the last stage."
else
  fail stages "Only one \`FROM\` so far. Add a second stage: \`FROM scratch\`."
fi

out=$(docker run --rm small-cow 2>&1)
if ! docker image inspect small-cow >/dev/null 2>&1; then
  fail works "There's no \`small-cow\` yet: \`docker build -t small-cow .\`"
elif grep -q "Ship me small" <<<"$out"; then
  pass works "The cow talks."
else
  fail works "\`docker run --rm small-cow\` said: \`$(head -1 <<<"$out" | cut -c1-120)\`. Is the \`ENTRYPOINT\` pointing at where you copied the program (\`/cow\`)?"
fi

size=$(docker image inspect -f '{{.Size}}' small-cow 2>/dev/null)
if [ -z "$size" ]; then
  fail small "Build \`small-cow\` first."
elif [ "$size" -lt 20000000 ]; then
  pass small "$((size / 1000000)) MB, down from over 1 GB. Only the program ships."
else
  fail small "\`small-cow\` is $((size / 1000000)) MB. Make the last stage \`FROM scratch\` and copy only \`/src/cow\` into it."
fi
