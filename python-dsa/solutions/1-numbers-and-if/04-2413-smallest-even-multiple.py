"""
2413. Smallest Even Multiple  (Easy)
https://leetcode.com/problems/smallest-even-multiple/

In plain words:
    You get a positive whole number n. Return the smallest positive number
    that can be divided exactly by both 2 and n (no remainder for either).

Example:
    n = 5  ->  10   (10 / 2 = 5 and 10 / 5 = 2, nothing smaller works)
    n = 6  ->  6    (6 is already even, and 6 / 6 = 1)

You'll need: % (page 2), if/else (page 3), return (page 4)

Run this file:  python3 04-2413-smallest-even-multiple.py
"""


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:   # n is even: n itself can be divided by 2 and by n
            return n
        else:            # n is odd: the smallest even number we can make from it is n * 2
            return n * 2


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (n, expected answer)
    (5, 10),
    (6, 6),
    (1, 2),
    (2, 2),
    (150, 150),
]

for n, expected in tests:
    got = Solution().smallestEvenMultiple(n)
    if got == expected:
        print("✓", n, "->", got)
    else:
        print("✗", n, "-> got", got, "but expected", expected)

# ---------- how this works ----------
#
# The answer must be a multiple of n, so it's n, or 2n, or 3n, ...
# It must also be even.
#   - If n is even, n itself already works, and nothing smaller is a multiple of n.
#   - If n is odd, n doesn't work (it's odd), but 2n is always even.
#
# Example: n = 5
#   5 % 2 is 1, so 5 is odd  ->  return 5 * 2  ->  10
# Example: n = 6
#   6 % 2 is 0, so 6 is even  ->  return 6
#
# Another way: Python's maths module has lcm ("least common multiple"),
# which is exactly this question:  import math  then  return math.lcm(2, n)
