set -e
docker rm -f keep-me sleepy old-1 old-2 >/dev/null 2>&1 || true
docker volume rm junk-1 junk-2 keep-data >/dev/null 2>&1 || true
docker pull -q nginx >/dev/null
docker pull -q busybox >/dev/null
docker run -d --name keep-me nginx >/dev/null
docker run -d --name sleepy nginx >/dev/null
docker stop sleepy >/dev/null
docker run --name old-1 busybox echo "job 1 done" >/dev/null
docker run --name old-2 busybox echo "job 2 done" >/dev/null
docker volume create junk-1 >/dev/null
docker volume create junk-2 >/dev/null
docker volume create keep-data >/dev/null
mkdir -p .lab-state
docker inspect -f '{{.Id}}' sleepy > .lab-state/sleepy-id
docker inspect -f '{{.Id}}' keep-me > .lab-state/keep-me-id
echo "Ready"
