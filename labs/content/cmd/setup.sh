set -e
docker rm -f say-ravi sayer-web >/dev/null 2>&1 || true
docker rmi -f sayer >/dev/null 2>&1 || true
docker build -q -t greet-cmd . >/dev/null
echo "Ready"
