docker rm -f greet-dev >/dev/null 2>&1
docker rmi -f greet-f:1.0 greet-f:dev >/dev/null 2>&1
docker pull -q node:24-slim >/dev/null
echo "Ready"
