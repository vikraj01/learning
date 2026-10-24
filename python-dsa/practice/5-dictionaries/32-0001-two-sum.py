"""
1. Two Sum  (Easy)
https://leetcode.com/problems/two-sum/

In plain words:
    You get a list of numbers, nums, and a number, target.
    Exactly two numbers in the list add up to target.
    Return their indexes (positions), as a list of two numbers.
    You can't use the same position twice.
    The two indexes can be in any order.

Example:
    nums = [2, 7, 11, 15], target = 9  ->  [0, 1]
    (because nums[0] + nums[1] = 2 + 7 = 9)

You'll need: enumerate (page 8), a dictionary that remembers
             number -> index, and `in` on a dictionary (page 9)

Run this file:  python3 32-0001-two-sum.py
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
    (([3, 3], 6), [0, 1]),
    (([-1, -2, -3, -4, -5], -8), [2, 4]),
]

# LeetCode accepts the two indexes in any order,
# so we sort your answer before comparing.
for inputs, expected in tests:
    got = Solution().twoSum(*inputs)
    if got is not None and sorted(got) == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Two loops, one inside the other, can try every pair. That works.
#         Can you do it with one loop?
# Hint 2: For each number, the partner you need is target - number.
# Hint 3: Walk the list once. Keep a dictionary of number -> index for the
#         numbers you've already passed. Before adding the current number,
#         check if its partner is already in the dictionary.
