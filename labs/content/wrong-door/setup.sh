set -e
docker rm -f quiet >/dev/null 2>&1 || true
docker build -q -t quiet-app . >/dev/null
docker run -d --name quiet -p 8098:8080 quiet-app >/dev/null
echo "Ready"
