docker rm -f web api db >/dev/null 2>&1
for n in notes-all front-net back-net; do docker network rm "$n" >/dev/null 2>&1; done
true
