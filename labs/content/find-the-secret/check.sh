source "$LAB_DIR/../_lib/check.sh"
want=$(cat "$LAB_WORKSPACE/.lab-state/secret" 2>/dev/null)
got=$(tr -d ' \t\r\n' < answer.txt 2>/dev/null)

if [ -z "$got" ]; then
  fail secret "\`answer.txt\` is empty. Did you save it (Ctrl + S)?"
elif [ "$got" = "$want" ]; then
  pass secret "Correct: the code is \`$want\`."
elif [ "$got" = "nothingherekeeplooking" ] || [ "$got" = "nothing here, keep looking" ]; then
  fail secret "That's the decoy note. There's another folder, and a hidden one."
else
  fail secret "\`$got\` isn't the code. Look for a hidden folder with \`ls -a\`."
fi

if running vault; then pass alive "\`vault\` is still running."; else fail alive "\`vault\` isn't running."; fi
