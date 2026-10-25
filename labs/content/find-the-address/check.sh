source "$LAB_DIR/../_lib/check.sh"
answer() { tr -d ' \t\r\n' < "$1" 2>/dev/null; }

ip=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' target 2>/dev/null)
got=$(answer ip.txt)
if ! running target; then
  fail ip "\`target\` isn't running. Press Reset."
elif [ -z "$got" ]; then
  fail ip "\`ip.txt\` is empty."
elif [ "$got" = "$ip" ]; then
  pass ip "Right: \`target\` lives at \`$ip\`."
else
  fail ip "\`$got\` isn't \`target\`'s address."
fi

gw=$(docker network inspect -f '{{range .IPAM.Config}}{{.Gateway}}{{end}}' bridge 2>/dev/null)
got=$(answer gateway.txt)
if [ -z "$got" ]; then
  fail gateway "\`gateway.txt\` is empty."
elif [ "$got" = "$gw" ]; then
  pass gateway "Right: the gateway is \`$gw\`, your laptop's side of the street."
else
  fail gateway "\`$got\` isn't the gateway of \`bridge\`."
fi

got=$(tr -d '\r' < page.txt 2>/dev/null | xargs)
if [ -z "$got" ]; then
  fail visit "\`page.txt\` is empty."
elif grep -qi "^welcome to nginx!\?$" <<<"$got"; then
  pass visit "Right: \"Welcome to nginx!\", fetched by number."
else
  fail visit "\`$got\` isn't the page title. Look between \`<title>\` and \`</title>\`."
fi
