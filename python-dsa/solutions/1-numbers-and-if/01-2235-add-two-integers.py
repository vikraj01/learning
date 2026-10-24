"""
2235. Add Two Integers  (Easy)
https://leetcode.com/problems/add-two-integers/

In plain words:
    You get two whole numbers, num1 and num2. Return their sum.
    The numbers can be negative.

Example:
    num1 = 12, num2 = 5   ->  17
    num1 = -10, num2 = 4  ->  -6

You'll need: + (page 2), return (page 4)

Run this file:  python3 01-2235-add-two-integers.py
"""


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        total = num1 + num2  # add the two numbers
        return total         # give the answer back to whoever called us


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    ((12, 5), 17),
    ((-10, 4), -6),
    ((0, 0), 0),
    ((-3, -7), -10),
]

for inputs, expected in tests:
    got = Solution().sum(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- how this works ----------
#
# The function gets two numbers. We add them with + and keep the result
# in a variable called total. Then we return it.
#
# Example: num1 = 12, num2 = 5
#   total = 12 + 5   ->  total is 17
#   return 17
#
# Negative numbers need nothing special: -10 + 4 is -6.
#
# Another way: you don't need the variable. One line does it:
#     return num1 + num2
