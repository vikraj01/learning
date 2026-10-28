source "$LAB_DIR/../_lib/check.sh"
compose_wipe labenv
docker compose up -d --build --quiet-pull >/dev/null 2>&1 || docker compose up -d --build
echo "Ready"
