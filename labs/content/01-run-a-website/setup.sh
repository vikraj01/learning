# Start clean, and download nginx now so her first `docker run` is quick.
docker rm -f hello-web >/dev/null 2>&1
docker pull -q nginx
