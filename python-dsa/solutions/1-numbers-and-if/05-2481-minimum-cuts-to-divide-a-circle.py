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
        if n == 1:
            return 0         # one slice: the whole circle, no cutting needed
        elif n % 2 == 0:
            return n // 2    # even: every full cut makes 2 slices at once
        else:
            return n         # odd: full cuts don't fit, so each slice needs its own half cut


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

# ---------- how this works ----------
#
# There are three cases.
#   - n = 1: the whole circle is already one slice. 0 cuts.
#   - n even: each full cut goes through the centre and adds 2 slices,
#     so n // 2 full cuts are enough. For n = 6: 6 // 2 = 3 cuts.
#   - n odd (and more than 1): slices can't pair up across the centre,
#     so we need one half cut per slice. For n = 3: 3 cuts (a Y shape).
#
# We check n == 1 first. 1 is odd, so if the odd case came first it would
# answer 1 instead of 0.
#
# Why // and not /? 6 / 2 gives 3.0, a decimal number. The answer should be
# a whole number, so we use // which gives 3.
#
# Another way: the order of the checks can change, as long as n == 1 is
# handled before the odd case.
