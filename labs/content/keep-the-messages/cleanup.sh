docker rm -f keeper >/dev/null 2>&1
docker volume rm messages >/dev/null 2>&1
docker rmi -f msg-keeper >/dev/null 2>&1
true
