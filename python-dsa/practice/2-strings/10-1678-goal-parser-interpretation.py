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
        # your code here
        pass


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

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: "G" already means "G", so only two of the pieces need changing.
# Hint 2: You can call replace more than once. Each call gives back a new string
#         that you can store and change again.
# Hint 3: Replace "()" with "o", then replace "(al)" with "al" in the result.
