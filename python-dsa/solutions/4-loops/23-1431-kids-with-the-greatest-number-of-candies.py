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

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        most = max(candies)  # the most any kid has right now
        answer = []

        for candy in candies:
            # with all the extras, does this kid reach the most?
            answer.append(candy + extraCandies >= most)

        return answer


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

# ---------- how this works ----------
#
# Pattern: BUILD A RESULT LIST, after one quick look at the whole list
# with max().
#
# Walk through candies = [2, 3, 5, 1, 3], extraCandies = 3:
#   most = 5
#   kid with 2: 2 + 3 = 5 >= 5  -> True
#   kid with 3: 3 + 3 = 6 >= 5  -> True
#   kid with 5: 5 + 3 = 8 >= 5  -> True
#   kid with 1: 1 + 3 = 4 >= 5  -> False
#   kid with 3: 6 >= 5          -> True
#
# Note: candy + extraCandies >= most is itself True or False, so there's no
# need for if/else around it.
#
# Another way: a list comprehension does the whole loop in one line.
#     return [candy + extraCandies >= most for candy in candies]
