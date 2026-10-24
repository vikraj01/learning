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
        steps = 0

        # we don't know how many steps it takes, so: while, not for
        while num > 0:
            if num % 2 == 0:
                num = num // 2  # even: halve it (// keeps it a whole number)
            else:
                num = num - 1   # odd: take away 1
            steps += 1          # either way, that was one step

        return steps


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

# ---------- how this works ----------
#
# Pattern: COUNTER inside a WHILE loop. We loop until num reaches 0 and
# count one step each time round.
#
# Walk through num = 8:
#   num 8, even -> 4    steps = 1
#   num 4, even -> 2    steps = 2
#   num 2, even -> 1    steps = 3
#   num 1, odd  -> 0    steps = 4
#   num is 0, the loop stops. Return 4.
#
# For num = 0 the loop never runs at all, and we return 0. That's right.
#
# Another way: there's a shortcut using how the number looks in binary
# (only 0s and 1s), but the loop above is the clear way to think about it.
