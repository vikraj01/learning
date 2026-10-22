#!/usr/bin/env bash
# Docker networking, live: every step from pages 1-4, one at a time.
#
#   cd docs/04-networking
#   ./demo.sh            # pauses before each step: press Enter to run it
#   ./demo.sh --no-wait  # runs straight through
#
# Cleans up everything it made when it ends (or when you press Ctrl+C).
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
page() { sleep 1; printf '%s' "$gray"; curl -s "$1" | sed -e 's/<[^>]*>/ /g' -e 's/  */ /g'; printf '%s\n' "$off"; }

cleanup() {
  docker rm -f box1 box2 box3 outsider web web2 db db2 >/dev/null 2>&1
  docker network rm lab counter-net >/dev/null 2>&1
}
trap cleanup EXIT
cleanup

part "Getting ready"
say "Build the visit-counter image and fetch busybox and redis."
run docker build -q -t visit-counter visit-counter
run docker pull -q busybox:1.37
run docker pull -q redis:8-alpine

part "1. The default network: numbers work, names don't"
say "Docker's own networks. Every container joins 'bridge' unless told otherwise."
run docker network ls
say "Two containers on the default network."
run docker run -d --name box1 busybox:1.37 sleep 3600
run docker run -d --name box2 busybox:1.37 sleep 3600
say "Each one has its own IP address, like a room number."
run docker exec box1 hostname -i
run docker exec box2 hostname -i
BOX1_IP=$(docker exec box1 hostname -i)
say "box2 can reach box1 by number..."
run docker exec box2 ping -c 2 "$BOX1_IP"
say "...but not by name. No phone book on the default network."
run docker exec box2 ping -c 1 box1
run docker rm -f box1 box2

part "2. Your own network: names work"
run docker network create lab
run docker run -d --name box1 --network lab busybox:1.37 sleep 3600
run docker run -d --name box2 --network lab busybox:1.37 sleep 3600
say "Same ping by name, now on 'lab'. It works."
run docker exec box2 ping -c 2 box1
say "Ask the phone book (Docker DNS at 127.0.0.11) directly."
run docker exec box2 nslookup box1
say "An alias: a second name for a container on this network."
run docker run -d --name box3 --network lab --network-alias helper busybox:1.37 sleep 3600
run docker exec box1 ping -c 1 helper
say "A container on another network can't see 'lab' at all."
run docker run -d --name outsider busybox:1.37 sleep 3600
run docker exec outsider ping -c 1 box1
say "Connect it to 'lab' while it's running, and now it can."
run docker network connect lab outsider
run docker exec outsider ping -c 1 box1
run docker rm -f box1 box2 box3 outsider
run docker network rm lab

part "3. The visit counter: app + database"
say "First on the default network: the app can't find 'db'."
run docker run -d --name db redis:8-alpine
run docker run -d --name web -p 8080:3000 visit-counter
page http://localhost:8080
run docker rm -f web db
say "Now on their own network. Only web gets a door (-p). db stays private."
run docker network create counter-net
run docker run -d --name db --network counter-net redis:8-alpine
run docker run -d --name web --network counter-net -p 8080:3000 visit-counter
say "Open http://localhost:8080 in the browser too. Three visits:"
page http://localhost:8080
page http://localhost:8080
page http://localhost:8080
say "Read and change the count from a third container, by name."
run docker run --rm --network counter-net redis:8-alpine redis-cli -h db GET visits
run docker run --rm --network counter-net redis:8-alpine redis-cli -h db SET visits 100
page http://localhost:8080
say "Replace the app: the count lives in db, so it carries on."
run docker rm -f web
run docker run -d --name web --network counter-net -p 8080:3000 visit-counter
page http://localhost:8080

part "4. Which address? The three mistakes"
say "Mistake 1: localhost inside a container means that container itself."
run docker run -d --name web2 --network counter-net -p 8081:3000 -e DB_URL=redis://localhost:6379 visit-counter
page http://localhost:8081
run docker rm -f web2
say "Mistake 2: using the laptop's door number (6380) inside the network."
run docker run -d --name db2 --network counter-net -p 6380:6379 redis:8-alpine
run docker run -d --name web2 --network counter-net -p 8081:3000 -e DB_URL=redis://db2:6380 visit-counter
page http://localhost:8081
run docker rm -f web2
say "Fixed: name + the port it listens on inside (6379)."
run docker run -d --name web2 --network counter-net -p 8081:3000 -e DB_URL=redis://db2:6379 visit-counter
page http://localhost:8081
say "Mistake 3: a container on the wrong network can't find db at all."
run docker run --rm redis:8-alpine redis-cli -h db PING
say "Same command, on counter-net."
run docker run --rm --network counter-net redis:8-alpine redis-cli -h db PING

part "Done"
say "Cleaning up: containers web, web2, db, db2 and network counter-net."
