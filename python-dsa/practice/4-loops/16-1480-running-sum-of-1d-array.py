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

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        # your code here
        pass


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

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Think of a shop till. Each new item is added to the total, and the
#         till shows the total so far after every item.
# Hint 2: Keep one variable, total, that starts at 0. Keep a list, answer,
#         that starts empty.
# Hint 3: For each number: add it to total, then append total to answer.
