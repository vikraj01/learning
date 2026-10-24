"""
1480. Running Sum of 1d Array  (Easy)
https://leetcode.com/problems/running-sum-of-1d-array/

In plain words:
    You get a list of numbers, nums. Return a new list of the same
    length where each place holds the sum of everything up to and
    including that place in nums.

Example:
    nums = [1, 2, 3, 4]  ->  [1, 3, 6, 10]
    because 1, 1+2, 1+2+3, 1+2+3+4

You'll need: for over a list (page 8), += (page 2), append (page 7)

Run this file:  python3 16-1480-running-sum-of-1d-array.py
"""

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        total = 0  # the sum so far

        for number in nums:
            total += number       # add this number to the sum so far
            answer.append(total)  # write down the sum so far

        return answer


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (input, expected answer)
    ([1, 2, 3, 4], [1, 3, 6, 10]),
    ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
    ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
    ([5], [5]),
]

for nums, expected in tests:
    got = Solution().runningSum(nums)
    if got == expected:
        print("✓", nums, "->", got)
    else:
        print("✗", nums, "-> got", got, "but expected", expected)

# ---------- how this works ----------
#
# Pattern: RUNNING TOTAL, plus BUILD A RESULT LIST.
# total remembers the sum so far. After adding each number, we write the
# total down in answer.
#
# Walk through nums = [1, 2, 3, 4]:
#   start:     total = 0,  answer = []
#   number 1:  total = 1,  answer = [1]
#   number 2:  total = 3,  answer = [1, 3]
#   number 3:  total = 6,  answer = [1, 3, 6]
#   number 4:  total = 10, answer = [1, 3, 6, 10]
#
# Another way (no new list): add the previous place into each place.
#     for i in range(1, len(nums)):
#         nums[i] += nums[i - 1]
#     return nums
# This changes nums itself, which LeetCode allows here.
