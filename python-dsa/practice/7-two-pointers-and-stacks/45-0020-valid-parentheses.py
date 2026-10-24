"""
20. Valid Parentheses  (Easy)
https://leetcode.com/problems/valid-parentheses/

In plain words:
    You get a string s made only of the brackets ( ) [ ] { }.
    Return True if the brackets are correctly matched:
      - every opening bracket is closed by the same kind of bracket,
      - brackets close in the right order (the last one opened closes first),
      - every closing bracket has an opening bracket before it.
    Otherwise return False.

Example:
    s = "()[]{}"  ->  True
    s = "([])"    ->  True
    s = "(]"      ->  False
    s = "([)]"    ->  False

You'll need: a dictionary (page 9), a list used as a stack:
             append, pop and [-1] (page 11)

Run this file:  python3 45-0020-valid-parentheses.py
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (("()",), True),
    (("()[]{}",), True),
    (("(]",), False),
    (("([])",), True),
    (("([)]",), False),
    (("]",), False),
]

for inputs, expected in tests:
    got = Solution().isValid(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: The bracket opened last must be closed first. That's a stack.
# Hint 2: A dictionary like {")": "(", ...} tells you which opening
#         bracket each closing one needs.
# Hint 3: Opening bracket: append it. Closing bracket: the top of the stack
#         (stack[-1]) must be its partner; if so pop, if not (or the stack is
#         empty) return False. At the end the stack must be empty.
