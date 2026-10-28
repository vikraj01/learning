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

# One environment variable of a container ("" if not set).
env_of() { docker inspect -f '{{range .Config.Env}}{{println .}}{{end}}' "$1" 2>/dev/null | sed -n "s/^$2=//p" | head -1; }

# Compose: the container of <service> started from this lab's folder (running or
# not), whatever project name was used. Compose labels every container with it.
here() { echo "label=com.docker.compose.project.working_dir=$LAB_WORKSPACE"; }
svc() { docker ps -aq --filter "$(here)" --filter "label=com.docker.compose.service=$1" | head -1; }
svc_running() { local c; c=$(svc "$1"); [ -n "$c" ] && running "$c"; }

# Remove everything Compose made from this lab's folder (plus any project names
# given): containers, networks, volumes, built images.
compose_wipe() {
  local projects p
  projects=$(docker ps -a --filter "$(here)" --format '{{.Label "com.docker.compose.project"}}' | sort -u)
  for p in $projects "$@"; do
    docker rm -f $(docker ps -aq --filter "label=com.docker.compose.project=$p") >/dev/null 2>&1
    docker network rm $(docker network ls -q --filter "label=com.docker.compose.project=$p") >/dev/null 2>&1
    docker volume rm $(docker volume ls -q --filter "label=com.docker.compose.project=$p") >/dev/null 2>&1
    docker rmi -f $(docker images -q --filter "label=com.docker.compose.project=$p") >/dev/null 2>&1
  done
  true
}
