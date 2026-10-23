#!/usr/bin/env bash
# Docker Compose, live: the todo app (frontend + backend + database), pages 2-5, one step at a time.
#
#   cd docs/07-compose
#   ./demo.sh            # pauses before each step: press Enter to run it
#   ./demo.sh --no-wait  # runs straight through
#
# Cleans up everything it made when it ends (or when you press Ctrl+C).
set -u
cd "$(dirname "$0")/todo-app"

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
api() { printf '%s' "$gray"; curl -s "$@"; printf '%s\n' "$off"; }
# Wait until the app answers through nginx (up to ~15s), so the next call isn't too early.
ready() { for _ in $(seq 1 30); do [ "$(curl -s -o /dev/null -w '%{http_code}' localhost:8080/api/todos)" = 200 ] && return; sleep 0.5; done; }
add() { api -X POST -H "Content-Type: application/json" -d "{\"text\":\"$1\"}" localhost:8080/api/todos; }

cleanup() {
  docker compose down -v >/dev/null 2>&1
  docker rm -f frontend backend db >/dev/null 2>&1
  docker network rm todo-net >/dev/null 2>&1
  docker volume rm todo-data >/dev/null 2>&1
}
trap cleanup EXIT
cleanup

part "1. By hand: seven commands, in the right order"
run docker network create todo-net
run docker volume create todo-data
run docker build -q -t todo-frontend ./frontend
run docker build -q -t todo-backend ./backend
run 'docker run -d --name db --network todo-net -e POSTGRES_USER=todo -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=todo -v todo-data:/var/lib/postgresql/data -v "$(pwd)/db/init.sql:/docker-entrypoint-initdb.d/init.sql" postgres:17-alpine'
run docker run -d --name backend --network todo-net -e DB_HOST=db -e DB_USER=todo -e DB_PASSWORD=secret -e DB_NAME=todo todo-backend
run docker run -d --name frontend --network todo-net -p 8080:80 todo-frontend
say "Ask straight away, a few times a second. Nothing made the backend wait for the database:"
last=""
for _ in $(seq 1 40); do
  out=$(curl -s -m 1 localhost:8080/api/todos -w ' %{http_code}')
  case "$out" in
    *" 500") now="error 500: $(grep -oiE 'error: [^<]*' <<<"$out" | head -1)" ;;
    *" 200") now="works: ${out% 200}" ;;
    *) now="no answer yet (${out##* })" ;;
  esac
  [ "$now" != "$last" ] && printf '%s  %s%s\n' "$gray" "$now" "$off" && last=$now
  case "$now" in works*) break ;; esac
  sleep 0.2
done
say "And cleaning up is three more commands."
run docker rm -f frontend backend db
run docker network rm todo-net
run docker volume rm todo-data

part "2. With Compose: one file, one command"
run cat compose.yaml
run docker compose up -d --build
run docker compose ps
ready
say "Open http://localhost:8080 in the browser. The API, through nginx:"
api localhost:8080/api/todos
add "Water the plants"
api -X PATCH localhost:8080/api/todos/1
api localhost:8080/api/todos

part "3. Living with it"
say "nginx writes down every request:"
run 'docker compose logs frontend | grep -E "\"(GET|POST|PATCH|DELETE) " | tail -3'
run docker compose logs backend
say "The real table, from inside the db service:"
run docker compose exec db psql -U todo -c '"SELECT * FROM todos ORDER BY id;"'
say "A bug: an empty todo gets saved."
add ""
run docker compose exec db psql -U todo -c '"SELECT * FROM todos ORDER BY id;"'
say "down keeps the volume. up again: the todos are still there."
run docker compose down
run 'docker volume ls | grep todo'
run docker compose up -d
ready
api localhost:8080/api/todos
say "down -v deletes the volume. up again: init.sql runs, two sample todos."
run docker compose down -v
run docker compose up -d
ready
api localhost:8080/api/todos

part "4. How the parts find each other"
run docker compose exec backend getent hosts db
run docker compose exec frontend getent hosts backend
run docker compose exec backend printenv DB_HOST DB_USER DB_NAME
say "Play nginx's part: ask the backend by name, on its inside port."
run docker compose exec frontend wget -qO- http://backend:3000/api/todos; echo
say "From the laptop, only the frontend has a door:"
run 'curl -s -m 2 -o /dev/null -w "localhost:8080 -> %{http_code}\n" localhost:8080/api/todos'
run 'curl -s -m 2 localhost:3000/api/todos || echo "localhost:3000 -> no door"'
say "Stop just the backend: the page loads, the API says 502."
run docker compose stop backend
run 'curl -s -o /dev/null -w "page -> %{http_code}\n" localhost:8080/'
run 'curl -s -o /dev/null -w "api  -> %{http_code}\n" localhost:8080/api/todos'
run docker compose start backend
sleep 5
ready
api localhost:8080/api/todos

part "Done"
say "Cleaning up: docker compose down -v."
