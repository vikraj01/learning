# Helpers for check.sh files. Each check prints one line:
#   PASS <task-id> <message>     or     FAIL <task-id> <message>
# Messages may use `backticks` for commands and names.

pass() { echo "PASS $1 ${*:2}"; }
fail() { echo "FAIL $1 ${*:2}"; }

# Is a container with this name running / does it exist at all?
running() { [ "$(docker inspect -f '{{.State.Running}}' "$1" 2>/dev/null)" = "true" ]; }
exists() { docker inspect "$1" >/dev/null 2>&1; }

# The image a container was started from.
image_of() { docker inspect -f '{{.Config.Image}}' "$1" 2>/dev/null; }

# The networks a container is on, space separated.
networks_of() { docker inspect -f '{{range $k, $v := .NetworkSettings.Networks}}{{$k}} {{end}}' "$1" 2>/dev/null | xargs; }

# Fetch a page (empty if nothing answers).
page() { curl -s --max-time 5 "$1"; }
