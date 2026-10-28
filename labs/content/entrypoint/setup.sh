docker rm -f ep-web ep-say >/dev/null 2>&1
docker rmi -f greet-ep >/dev/null 2>&1
docker pull -q node:24-slim >/dev/null
echo "Ready"
