set -e
docker rm -f clean >/dev/null 2>&1 || true
docker rmi -f greet-clean >/dev/null 2>&1 || true
docker build -q -t leaky . >/dev/null
echo "Ready"
