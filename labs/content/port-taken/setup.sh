docker rm -f squatter shop >/dev/null 2>&1
docker pull -q nginx
docker run -d --name squatter -p 8093:80 nginx
