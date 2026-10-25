set -e
docker rm -f keeper >/dev/null 2>&1 || true
docker volume rm messages >/dev/null 2>&1 || true
docker build -q -t msg-keeper . >/dev/null
mkdir -p .lab-state && rm -f .lab-state/first-keeper
echo "Ready"
