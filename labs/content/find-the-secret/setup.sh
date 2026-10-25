set -e
docker rm -f vault >/dev/null 2>&1 || true
docker pull -q busybox >/dev/null
words=(lighthouse pineapple thunder origami lantern compass marble falcon velvet harbor)
word=${words[$RANDOM % ${#words[@]}]}-$((RANDOM % 90 + 10))
docker run -d --name vault busybox sh -c "mkdir -p /var/lib/vault/rooms/blue /var/lib/vault/rooms/red/.hidden && echo 'nothing here, keep looking' > /var/lib/vault/rooms/blue/note.txt && echo '$word' > /var/lib/vault/rooms/red/.hidden/code.txt && tail -f /dev/null" >/dev/null
mkdir -p .lab-state
echo "$word" > .lab-state/secret
: > answer.txt
echo "Ready"
