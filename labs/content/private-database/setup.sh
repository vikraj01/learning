set -e
docker rm -f web api db >/dev/null 2>&1 || true
for n in notes-all front-net back-net; do docker network rm "$n" >/dev/null 2>&1 || true; done
docker build -q -t notes-db  ./db  >/dev/null
docker build -q -t notes-api ./api >/dev/null
docker build -q -t notes-web ./web >/dev/null
docker network create notes-all >/dev/null
docker run -d --name db  --network notes-all notes-db  >/dev/null
docker run -d --name api --network notes-all notes-api >/dev/null
docker run -d --name web --network notes-all -p 3301:3000 notes-web >/dev/null
echo "Ready"
