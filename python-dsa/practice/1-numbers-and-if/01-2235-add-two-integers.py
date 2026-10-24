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
        # your code here
        pass


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

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Python adds two numbers with +.
# Hint 2: The answer has to come back out of the function. print() only shows it;
#         you need return.
# Hint 3: Add num1 and num2, store it in a variable, and return that variable.
