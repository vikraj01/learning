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
        # each closing bracket -> the opening bracket it needs
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []  # opening brackets still waiting to be closed

        for ch in s:
            if ch in pairs:
                # a closing bracket: the top of the stack must be its partner
                if len(stack) == 0 or stack[-1] != pairs[ch]:
                    return False
                stack.pop()  # matched, so it's no longer waiting
            else:
                stack.append(ch)  # an opening bracket: put it on the stack

        # every opening bracket must have been closed
        return len(stack) == 0


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

# ---------- how this works ----------
#
# The stack holds opening brackets that are still waiting for a partner.
#
# s = "([)]"
#   "(" -> stack ["("]
#   "[" -> stack ["(", "["]
#   ")" needs "(", but the top is "[" -> False
# s = "([])": push (, push [, ] matches [ (pop), ) matches ( (pop),
#   stack is empty at the end -> True
