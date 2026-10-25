# Build the three images from the lab folder and start them on the default network (the broken start).
set -e
docker rm -f web api db >/dev/null 2>&1 || true
docker build -q -t notes-db  ./db
docker build -q -t notes-api ./api
docker build -q -t notes-web ./web
docker run -d --name db  notes-db
docker run -d --name api notes-api
docker run -d --name web -p 3300:3000 notes-web
