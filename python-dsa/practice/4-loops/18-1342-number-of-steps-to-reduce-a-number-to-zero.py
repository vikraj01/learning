"""
1342. Number of Steps to Reduce a Number to Zero  (Easy)
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

In plain words:
    You get a whole number num (0 or more). Repeat until it is 0:
      - if num is even, divide it by 2,
      - if num is odd, take away 1.
    Each of those is one step. Return how many steps it takes.

Example:
    num = 14  ->  6
    14 -> 7 -> 6 -> 3 -> 2 -> 1 -> 0  (6 arrows, 6 steps)

You'll need: while (page 8), % and // (page 2), if/else (page 3)

Run this file:  python3 18-1342-number-of-steps-to-reduce-a-number-to-zero.py
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (input, expected answer)
    (14, 6),
    (8, 4),
    (123, 12),
    (0, 0),
]

for num, expected in tests:
    got = Solution().numberOfSteps(num)
    if got == expected:
        print("✓", num, "->", got)
    else:
        print("✗", num, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: You don't know in advance how many steps there will be. Which
#         loop keeps going "while something is true"?
# Hint 2: Even means num % 2 == 0. Use // to halve it, so it stays a whole
#         number.
# Hint 3: Keep a counter, steps = 0. Loop while num > 0: change num, then
#         add 1 to steps.
