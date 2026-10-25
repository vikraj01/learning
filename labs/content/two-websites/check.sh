source "$LAB_DIR/../_lib/check.sh"

check_site() { # task, name, image, port, text
  local task=$1 name=$2 want=$3 port=$4 text=$5 img
  img=$(image_of "$name")
  if ! exists "$name"; then
    fail "$task" "There's no container called \`$name\`."
  elif [[ "$img" != $want* ]]; then
    fail "$task" "\`$name\` runs \`$img\`, not \`$want\`."
  elif ! running "$name"; then
    fail "$task" "\`$name\` has stopped. \`docker logs $name\` says why."
  elif page "http://localhost:$port" | grep -qi "$text"; then
    pass "$task" "Opens on port $port."
  else
    door=$(docker port "$name" 2>/dev/null | head -1)
    fail "$task" "Nothing answers on \`localhost:$port\`. Its door is: \`${door:-none}\`"
  fi
}

check_site one site-one nginx 8091 "welcome to nginx"
check_site two site-two httpd 8092 "it works"

if running site-one && running site-two; then
  pass both "Two web servers, both on port 80 inside, side by side."
else
  fail both "Both have to be running: \`docker ps\` shows which ones are."
fi
