source "$LAB_DIR/../_lib/check.sh"
source "$LAB_DIR/../_lib/notes.sh"

notes_running
notes_page 3501

db=$(svc db)
vol=$(docker inspect -f '{{range .Mounts}}{{if eq .Destination "/var/lib/postgresql/data"}}{{.Type}}:{{.Name}}{{end}}{{end}}' "$db" 2>/dev/null)
if [ -z "$db" ]; then
  fail volume "There's no \`db\` service yet."
elif [[ "$vol" == volume:* ]] && ! docker volume inspect -f '{{.Labels}}' "${vol#volume:}" 2>/dev/null | grep -q "com.docker.compose.volume:"; then
  fail volume "\`db\` uses a volume Compose didn't name (\`${vol#volume:}\`). Give it one: \`- data:/var/lib/postgresql/data\`, and \`data:\` under \`volumes:\` at the bottom."
elif [[ "$vol" == volume:* ]]; then
  pass volume "\`db\` keeps its data in the volume \`${vol#volume:}\`."
else
  fail volume "\`db\` has no named volume on \`/var/lib/postgresql/data\`."
fi
