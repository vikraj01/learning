source "$LAB_DIR/../_lib/check.sh"
state="$LAB_WORKSPACE/.lab-state"
id_of() { docker inspect -f '{{.Id}}' "$1" 2>/dev/null; }

if running sleepy && [ "$(id_of sleepy)" = "$(cat "$state/sleepy-id" 2>/dev/null)" ]; then
  pass sleepy "\`sleepy\` is running, and it's the same container as before."
elif running sleepy; then
  fail sleepy "\`sleepy\` is running, but it's a new container. The old one was removed. Press Reset to try again, and use \`docker start\`."
elif exists sleepy; then
  fail sleepy "\`sleepy\` is still stopped."
else
  fail sleepy "\`sleepy\` was removed. Press Reset to try again."
fi

left=""
for c in old-1 old-2; do exists "$c" && left="$left \`$c\`"; done
if [ -z "$left" ]; then pass old "Both are gone."; else fail old "Still there:$left"; fi

left=""
for v in junk-1 junk-2; do docker volume inspect "$v" >/dev/null 2>&1 && left="$left \`$v\`"; done
if [ -z "$left" ]; then pass junk "Both junk volumes are gone."; else fail junk "Still there:$left"; fi

if ! running keep-me || [ "$(id_of keep-me)" != "$(cat "$state/keep-me-id" 2>/dev/null)" ]; then
  fail kept "\`keep-me\` was stopped or replaced. Press Reset to try again."
elif ! docker volume inspect keep-data >/dev/null 2>&1; then
  fail kept "The volume \`keep-data\` was removed. Press Reset to try again."
else
  pass kept "\`keep-me\` and \`keep-data\` are safe."
fi
