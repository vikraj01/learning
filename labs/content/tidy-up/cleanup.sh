docker rm -f keep-me sleepy old-1 old-2 >/dev/null 2>&1
docker volume rm junk-1 junk-2 keep-data >/dev/null 2>&1
true
