"""
2011. Final Value of Variable After Performing Operations  (Easy)
https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

In plain words:
    A variable X starts at 0. You get a list of operations, each one a
    string: "++X" or "X++" adds 1 to X, "--X" or "X--" takes 1 away.
    Do them all in order and return the final value of X.

Example:
    operations = ["--X", "X++", "X++"]  ->  1
    0 - 1 + 1 + 1 = 1

You'll need: for over a list (page 8), in on strings (page 6), if/else (page 3)

Run this file:  python3 21-2011-final-value-of-variable.py
"""

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (input, expected answer)
    (["--X", "X++", "X++"], 1),
    (["++X", "++X", "X++"], 3),
    (["X++", "++X", "--X", "X--"], 0),
    (["X--"], -1),
]

for operations, expected in tests:
    got = Solution().finalValueAfterOperations(operations)
    if got == expected:
        print("✓", operations, "->", got)
    else:
        print("✗", operations, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Start a variable at 0 and loop over the operations.
# Hint 2: There are 4 possible strings, but only 2 meanings: add 1 or take
#         away 1. Is there one character that tells them apart?
# Hint 3: if "+" in operation: add 1, else take away 1.
