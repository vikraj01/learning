source "$LAB_DIR/../_lib/check.sh"

html=$(page http://localhost:8100)
if running live-site && [ -n "$html" ]; then
  pass running "\`live-site\` answers on port 8100."
elif running live-site; then
  fail running "\`live-site\` runs, but nothing answers on \`localhost:8100\`. Door: \`$(docker port live-site 2>/dev/null | head -1)\`"
else
  fail running "There's no running container called \`live-site\`."
fi

src=$(docker inspect -f '{{range .Mounts}}{{if eq .Destination "/usr/share/nginx/html"}}{{.Type}}:{{.Source}}{{end}}{{end}}' live-site 2>/dev/null)
if [ "$src" = "bind:$LAB_WORKSPACE/site" ]; then
  pass mount "nginx shows the \`site\` folder from your laptop."
elif [[ "$src" == bind:* ]]; then
  fail mount "A folder is shared, but it's \`${src#bind:}\`, not this lab's \`site\` folder."
elif [[ "$src" == volume:* ]]; then
  fail mount "That's a volume. Use a path to your folder on the left of \`-v\`."
else
  fail mount "Nothing is mounted on \`/usr/share/nginx/html\`, so nginx shows its own default page."
fi

file=$(cat site/index.html 2>/dev/null)
if [ "$src" != "bind:$LAB_WORKSPACE/site" ]; then
  fail edited "Share the folder first."
elif grep -q "Hello from my laptop" <<<"$file"; then
  fail edited "The page still says \"Hello from my laptop\". Change the \`<h1>\` and save."
elif [ "$html" = "$file" ]; then
  pass edited "The page shows your edit: \`$(grep -o '<h1>[^<]*</h1>' <<<"$file" | sed 's/<[^>]*>//g' | head -1)\`"
else
  fail edited "The page doesn't match the file yet. Saved it? Reloaded?"
fi
