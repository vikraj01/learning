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
        # your code here
        pass


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

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Try a few by hand: n = 3, n = 4, n = 7, n = 8. Do you see two kinds of n?
# Hint 2: When n is even, the answer is n. When n is odd, it isn't. How do you test
#         whether a number is even? (Remainder after dividing by 2.)
# Hint 3: If n % 2 == 0, return n. Otherwise return n doubled.
