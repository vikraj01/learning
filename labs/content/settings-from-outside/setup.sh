set -e
docker rm -f hello >/dev/null 2>&1 || true
docker build -q -t greet-lab . >/dev/null
echo "Ready"
