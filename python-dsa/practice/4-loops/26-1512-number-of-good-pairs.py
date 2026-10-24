"""
1512. Number of Good Pairs  (Easy)
https://leetcode.com/problems/number-of-good-pairs/

In plain words:
    You get a list of numbers, nums. A "good pair" is two different
    places i and j, with i before j (i < j), that hold the same number:
    nums[i] == nums[j]. Return how many good pairs there are.

Example:
    nums = [1, 2, 3, 1, 1, 3]  ->  4
    the pairs of indexes are (0,3), (0,4), (3,4) (all 1s) and (2,5) (both 3s)

You'll need: nested for loops, range(len(...)) (page 8), == (page 3)

Run this file:  python3 26-1512-number-of-good-pairs.py
"""

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (input, expected answer)
    ([1, 2, 3, 1, 1, 3], 4),
    ([1, 1, 1, 1], 6),
    ([1, 2, 3], 0),
    ([5], 0),
]

for nums, expected in tests:
    got = Solution().numIdenticalPairs(nums)
    if got == expected:
        print("✓", nums, "->", got)
    else:
        print("✗", nums, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: You need to look at every pair of places. How would you do that
#         by hand? Fix the first one, then try every place after it.
# Hint 2: That's a loop inside a loop: one for i, one for j.
# Hint 3: Let j start at i + 1: range(i + 1, len(nums)). Then i < j always,
#         and you never count a pair twice. Count when nums[i] == nums[j].
