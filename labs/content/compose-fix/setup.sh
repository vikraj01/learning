source "$LAB_DIR/../_lib/check.sh"
compose_wipe labfix
docker pull -q postgres:17-alpine >/dev/null
docker pull -q node:20-alpine >/dev/null
echo "Ready"
