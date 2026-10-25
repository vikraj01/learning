set -e
docker rm -f target >/dev/null 2>&1 || true
docker pull -q nginx >/dev/null
docker pull -q busybox >/dev/null
docker run -d --name target nginx >/dev/null
: > ip.txt; : > gateway.txt; : > page.txt
echo "Ready"
