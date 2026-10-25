# Start clean, and download the Node image now so her builds are quick.
docker rm -f box >/dev/null 2>&1
docker rmi -f message-box-fixed >/dev/null 2>&1
docker pull -q node:24-slim
