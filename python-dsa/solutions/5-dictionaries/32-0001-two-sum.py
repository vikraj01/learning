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

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # number -> the index where we saw it

        for i, num in enumerate(nums):
            need = target - num  # the partner that would make target
            if need in seen:
                # we saw the partner earlier, at index seen[need]
                return [seen[need], i]
            seen[num] = i  # remember this number for later


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

# ---------- how this works ----------
#
# For each number, the partner we need is target - number.
# A dictionary remembers every number we've passed and where it was.
#
# nums = [2, 7, 11, 15], target = 9
#   i=0, num=2: need 7. seen is {}, no. Remember seen = {2: 0}
#   i=1, num=7: need 2. 2 is in seen, at index 0. Return [0, 1].
#
# Another way (slower): two loops trying every pair i < j and
# returning [i, j] when nums[i] + nums[j] == target. It works,
# but for a long list it does a lot more checking.
