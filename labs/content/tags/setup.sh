docker rm -f v1 >/dev/null 2>&1
docker rmi -f greet-tags:1.0 greet-tags:2.0 greet-tags:latest >/dev/null 2>&1
docker pull -q node:24-slim >/dev/null
echo "Ready"
