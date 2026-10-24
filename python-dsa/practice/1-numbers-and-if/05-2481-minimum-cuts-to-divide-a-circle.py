"""
2481. Minimum Cuts to Divide a Circle  (Easy)
https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

In plain words:
    Think of cutting a round cake into n equal slices. A cut is one straight
    line, and there are two kinds:
      - a full cut: straight across, through the centre, edge to edge
      - a half cut: from the centre out to the edge
    Return the smallest number of cuts that gives n equal slices.
    n is between 1 and 100. With n = 1 the whole cake is one slice.

Example:
    n = 4  ->  2   (two full cuts, like a +)
    n = 3  ->  3   (three half cuts, like a Y)

You'll need: % and // (page 2), if/elif/else (page 3), return (page 4)

Run this file:  python3 05-2481-minimum-cuts-to-divide-a-circle.py
"""


class Solution:
    def numberOfCuts(self, n: int) -> int:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (n, expected answer)
    (4, 2),
    (3, 3),
    (1, 0),
    (6, 3),
    (7, 7),
]

for n, expected in tests:
    got = Solution().numberOfCuts(n)
    if got == expected:
        print("✓", n, "->", got)
    else:
        print("✗", n, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Draw it. How many cuts for 2 slices? For 4? For 6? Now try 3 and 5.
# Hint 2: A full cut gives 2 slices at once, but only when the slices pair up
#         opposite each other. That works when n is even. There's also one special
#         case where you don't cut at all.
# Hint 3: Three cases: n is 1 (no cuts), n is even (n divided by 2, use //),
#         n is odd (n cuts).
