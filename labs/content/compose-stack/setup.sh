source "$LAB_DIR/../_lib/check.sh"
compose_wipe
docker pull -q postgres:17-alpine >/dev/null
docker pull -q node:20-alpine >/dev/null
echo "Ready"
