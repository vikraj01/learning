"""
1431. Kids With the Greatest Number of Candies  (Easy)
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

In plain words:
    You get a list candies: candies[i] is how many candies kid i has.
    You also have extraCandies to give away.
    For each kid, imagine giving them ALL the extra candies. Would they
    then have the most (or tie for the most)? Return a list of True/False,
    one for each kid, in the same order.

Example:
    candies = [2, 3, 5, 1, 3], extraCandies = 3
      ->  [True, True, True, False, True]
    the most anyone has is 5; only the kid with 1 can't reach 5 (1+3 = 4)

You'll need: for over a list (page 8), max and append (page 7), >= (page 3)

Run this file:  python3 23-1431-kids-with-the-greatest-number-of-candies.py
"""

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (([2, 3, 5, 1, 3], 3), [True, True, True, False, True]),
    (([4, 2, 1, 1, 2], 1), [True, False, False, False, False]),
    (([12, 1, 12], 10), [True, False, True]),
    (([7], 0), [True]),
]

for inputs, expected in tests:
    got = Solution().kidsWithCandies(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: First find the most candies any kid has. Which list function
#         from page 7 does that?
# Hint 2: Then loop over the kids. For each, add extraCandies and compare
#         with the most. A tie counts, so use >=.
# Hint 3: A comparison like a >= b already gives True or False, so you can
#         append it straight to your answer list.
