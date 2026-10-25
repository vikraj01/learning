source "$LAB_DIR/../_lib/check.sh"

# 1. order: COPY package.json  <  RUN npm install  <  COPY of app.js (or .)
order=$(python3 - <<'PY'
import re
lines = [l.strip() for l in open("Dockerfile") if l.strip() and not l.strip().startswith("#")]
def first(pattern):
    return next((i for i, l in enumerate(lines) if re.search(pattern, l, re.I)), None)
pkg = first(r"^COPY\s+.*package")
install = first(r"^RUN\s+.*npm\s+(install|i|ci)\b")
code = first(r"^COPY\s+(\.|app\.js|\*)")
if install is None: print("no-install")
elif pkg is None or pkg > install: print("no-package-first")
elif code is None: print("no-code")
elif code < install: print("code-before")
else: print("ok")
PY
)
case "$order" in
  ok) pass order "\`package.json\` and \`npm install\` come first, the code comes after." ;;
  no-install) fail order "There's no \`RUN npm install\` line any more." ;;
  no-package-first) fail order "Copy \`package.json\` on its own line, before \`RUN npm install\`." ;;
  no-code) fail order "The app itself is never copied. Add \`COPY app.js .\` after \`npm install\`." ;;
  code-before) fail order "Something that copies \`app.js\` still comes before \`npm install\`." ;;
  *) fail order "Couldn't read the Dockerfile." ;;
esac

# 2. built after the last change to the Dockerfile
built=$(docker image inspect -f '{{.Created}}' fast-box 2>/dev/null)
if [ -z "$built" ]; then
  fail build "There's no image called \`fast-box\` yet."
elif python3 -c "
import sys, os, datetime
created = datetime.datetime.fromisoformat(sys.argv[1][:26].rstrip('Z') + '+00:00')
sys.exit(0 if created.timestamp() >= os.path.getmtime('Dockerfile') - 2 else 1)" "$built"; then
  pass build "\`fast-box\` is built from the latest Dockerfile."
else
  fail build "\`fast-box\` is older than your last change to the Dockerfile. Build it again."
fi

# 3. really cached: build a copy with a changed app.js
if [ "$order" != "ok" ]; then
  fail cached "Fix the order first."
else
  tmp=$(mktemp -d)
  cp -r . "$tmp" && rm -rf "$tmp/.lab-state"
  echo "// changed by the check at $(date +%s%N)" >> "$tmp/app.js"
  out=$(docker build --progress=plain -t fast-box-check "$tmp" 2>&1)
  rm -rf "$tmp"
  docker rmi -f fast-box-check >/dev/null 2>&1
  step=$(grep -m1 -E '^#[0-9]+ \[.*\] RUN .*npm' <<<"$out" | cut -d' ' -f1)
  if [ -n "$step" ] && grep -q "^$step CACHED" <<<"$out"; then
    pass cached "\`app.js\` changed, and \`npm install\` said CACHED. Rebuilds are fast now."
  else
    fail cached "\`npm install\` ran again after a change to \`app.js\`."
  fi
fi
