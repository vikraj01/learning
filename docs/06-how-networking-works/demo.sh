#!/usr/bin/env bash
# How networking works, live: the commands from pages 1-6, one at a time.
#
#   cd docs/06-how-networking-works
#   ./demo.sh            # pauses before each step: press Enter to run it
#   ./demo.sh --no-wait  # runs straight through
#
# Works on Linux and macOS. Needs python3 and curl, and an internet connection.
# Starts small web servers on ports 9001-9004 and stops them when it ends (or on Ctrl+C).
set -u
cd "$(dirname "$0")"

WAIT=1
[ "${1:-}" = "--no-wait" ] && WAIT=0

bold=$'\e[1m'; blue=$'\e[34m'; green=$'\e[32m'; gray=$'\e[90m'; off=$'\e[0m'

part() { printf '\n%s━━━ %s ━━━%s\n' "$bold$blue" "$1" "$off"; }
say() { printf '\n%s%s%s\n' "$green" "$1" "$off"; }
run() {
  printf '%s$ %s%s' "$bold" "$*" "$off"
  if [ "$WAIT" = 1 ]; then read -r _; else echo; fi
  eval "$@"
}

WORK=$(mktemp -d)
PIDS=()
# serve <folder> <port> [bind address]: start a python web server in the background
serve() {
  (cd "$WORK/$1" && exec python3 -u -m http.server "$2" ${3:+--bind "$3"} >"$WORK/server-$2.log" 2>&1) &
  PIDS+=($!)
  sleep 1
  printf '%s%s%s\n' "$gray" "$(head -1 "$WORK/server-$2.log")" "$off"
}
log() { printf '%s' "$gray"; cat "$WORK/server-$1.log"; printf '%s' "$off"; }

cleanup() {
  for pid in "${PIDS[@]:-}"; do [ -n "$pid" ] && kill "$pid" 2>/dev/null; done
  rm -rf "$WORK"
}
trap cleanup EXIT

if [ "$(uname)" = "Darwin" ]; then
  MY_IP=$(ipconfig getifaddr en0)
  IP_CMD="ipconfig getifaddr en0"
  ROUTER_CMD="route -n get default | grep gateway"
else
  MY_IP=$(hostname -I | awk '{print $1}')
  IP_CMD="hostname -I"
  ROUTER_CMD="ip route | grep default"
fi

mkdir -p "$WORK/flat-1" "$WORK/flat-2"
echo "<h1>Hello from flat 1</h1>" > "$WORK/flat-1/index.html"
echo "<h1>Hello from flat 2</h1>" > "$WORK/flat-2/index.html"

part "1. Every computer has an address"
say "My laptop's IP address (its building address):"
run "$IP_CMD"
say "127.0.0.1 is 'myself'. A note to yourself: look how fast."
run ping -c 2 127.0.0.1
say "localhost is just its name."
run ping -c 1 localhost
say "A building far away: one of Google's computers. A thousand times slower."
run ping -c 2 8.8.8.8

part "2. One address, many doors: ports"
say "Two servers, two flats: 9001 and 9002."
serve flat-1 9001
serve flat-2 9002
run curl -s localhost:9001
run curl -s localhost:9002
say "The server wrote down who knocked:"
log 9001
say "A second program wants flat 9001. It's taken."
run "(cd $WORK/flat-2 && python3 -m http.server 9001 2>&1 | tail -1)"
say "Who lives in flat 9001?"
run lsof -nP -iTCP:9001 -sTCP:LISTEN
say "An empty flat: the building is there, but nobody answers."
run curl -sS localhost:9005

part "3. Who can come in? 127.0.0.1 vs 0.0.0.0"
say "Server A: intercom only (127.0.0.1). Server B: front door (0.0.0.0)."
serve flat-1 9003 127.0.0.1
serve flat-1 9004 0.0.0.0
say "From inside, with localhost: both answer."
run curl -s localhost:9003
run curl -s localhost:9004
say "From the street address ($MY_IP): only B answers."
run curl -sS -m 3 "$MY_IP:9003"
run curl -sS -m 3 "$MY_IP:9004"
say "On your phone (same Wi-Fi), open:  http://$MY_IP:9004  (works)  and  http://$MY_IP:9003  (doesn't)."

part "4. DNS: names into numbers"
run nslookup example.com
say "ping looks the name up first. Watch the first line."
run ping -c 2 google.com
say "A name nobody has: NXDOMAIN, no such contact."
run "nslookup made-up-tanvi.com | grep -i nxdomain"
say "Your private contacts, checked before any DNS server:"
run "grep localhost /etc/hosts"
say "Any name ending in .localhost means 'myself'."
run curl -s http://tanvi.localhost:9001

part "5. Opening a website, step by step"
say "* = what curl does, > = our request, < = the response."
run "curl -sv -o /dev/null http://example.com 2>&1 | grep -E '^[*<>]' | head -16"
say "Be the website: ask our own server for a page that exists, and one that doesn't."
run curl -s -o /dev/null -w '"%{http_code}\n"' localhost:9001/
run curl -s -o /dev/null -w '"%{http_code}\n"' localhost:9001/nope
say "What the server saw:"
log 9001

part "6. Your home network"
say "Private address (inside the society):"
run "$IP_CMD"
say "The router (the watchman at the gate):"
run "$ROUTER_CMD"
say "Public address (the gate, as the internet sees it):"
run curl -s ifconfig.me
echo

part "Done"
say "Stopping the servers on 9001-9004."
