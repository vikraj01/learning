"""
1678. Goal Parser Interpretation  (Easy)
https://leetcode.com/problems/goal-parser-interpretation/

In plain words:
    You get a string command made only of these three pieces, in any order:
        "G"     means  "G"
        "()"    means  "o"
        "(al)"  means  "al"
    Return the string you get when every piece is changed to its meaning.

Example:
    command = "G()(al)"         ->  "Goal"
    command = "G()()()()(al)"   ->  "Gooooal"

You'll need: the string method replace (page 6), return (page 4)

Run this file:  python3 10-1678-goal-parser-interpretation.py
"""


class Solution:
    def interpret(self, command: str) -> str:
        result = command.replace("()", "o")     # every "()" becomes "o"
        result = result.replace("(al)", "al")   # every "(al)" becomes "al"
        return result                           # "G" was already right, so we leave it


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (command, expected answer)
    ("G()(al)", "Goal"),
    ("G()()()()(al)", "Gooooal"),
    ("(al)G(al)()()G", "alGalooG"),
    ("G", "G"),
]

for command, expected in tests:
    got = Solution().interpret(command)
    # repr() prints text with its quotes, so you can see spaces at the start or end
    if got == expected:
        print("✓", repr(command), "->", repr(got))
    else:
        print("✗", repr(command), "-> got", repr(got), "but expected", repr(expected))

# ---------- how this works ----------
#
# Each replace() changes every copy of one piece. We do it twice: once for
# "()" and once for "(al)". "G" needs no change.
#
# Example: command = "G()(al)"
#   "G()(al)".replace("()", "o")    ->  "Go(al)"
#   "Go(al)".replace("(al)", "al")  ->  "Goal"
#
# Important: replace() gives back a new string. The second call must use
# result, not command, or the first change is lost.
#
# Another way: chain the two calls in one line:
#     return command.replace("()", "o").replace("(al)", "al")
