source "$LAB_DIR/../_lib/check.sh"
compose_wipe hello
docker pull -q node:24-slim >/dev/null
echo "Ready"
