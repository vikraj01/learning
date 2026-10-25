source "$LAB_DIR/../_lib/check.sh"
state="$LAB_WORKSPACE/.lab-state"; mkdir -p "$state"

if docker volume inspect messages >/dev/null 2>&1; then
  pass volume "The volume \`messages\` exists."
else
  fail volume "There's no volume called \`messages\` yet."
fi

mounts=$(docker inspect -f '{{range .Mounts}}{{.Type}}:{{.Name}}:{{.Destination}} {{end}}' keeper 2>/dev/null)
if running keeper && [ "$(image_of keeper)" = "msg-keeper" ] && [[ " $mounts " == *" volume:messages:/app/data "* ]]; then
  pass mounted "\`keeper\` keeps its messages in the volume."
elif ! running keeper; then
  fail mounted "There's no running container called \`keeper\`."
elif [[ "$mounts" == *"bind:"* ]]; then
  fail mounted "That's a folder from your laptop (a bind mount). Use the volume name on the left of \`-v\`: \`messages:/app/data\`."
else
  fail mounted "\`keeper\` has no volume \`messages\` on \`/app/data\`. Mounted now: \`${mounts:-nothing}\`"
fi

count=$(docker run --rm -v messages:/d busybox sh -c 'grep -c . /d/messages.txt 2>/dev/null || echo 0' 2>/dev/null)
current=$(docker inspect -f '{{.Id}}' keeper 2>/dev/null)
if [ "${count:-0}" -gt 0 ] 2>/dev/null; then
  pass saved "$count message(s) saved in the volume."
  [ -s "$state/first-keeper" ] || echo "$current" > "$state/first-keeper"
else
  fail saved "No messages in the volume yet."
fi

first=$(cat "$state/first-keeper" 2>/dev/null)
if [ -z "$first" ]; then
  fail survived "First save a message and press Check."
elif [ "$current" = "$first" ] || [ -z "$current" ]; then
  fail survived "Now remove \`keeper\`, start a new one with the same volume, and press Check again."
elif [ "${count:-0}" -gt 0 ] && running keeper && [[ " $mounts " == *" volume:messages:/app/data "* ]]; then
  pass survived "A brand-new \`keeper\`, and the messages are still there. The volume remembered."
else
  fail survived "The new \`keeper\` doesn't have the messages. Did you give it \`-v messages:/app/data\`?"
fi
