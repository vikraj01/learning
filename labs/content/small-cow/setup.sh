set -e
docker rmi -f small-cow >/dev/null 2>&1 || true
docker build -q -t big-cow . >/dev/null
echo "Ready"
