"""
169. Majority Element  (Easy)
https://leetcode.com/problems/majority-element/

In plain words:
    You get a list of numbers, nums. One number appears more than half
    of the time (more than len(nums) // 2 times). Return that number.
    There is always such a number.

Example:
    nums = [3, 2, 3]              ->  3
    nums = [2, 2, 1, 1, 1, 2, 2]  ->  2

You'll need: // (page 2), len (page 7),
             counting with a dictionary and .items() (page 9)

Run this file:  python3 36-0169-majority-element.py
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (([3, 2, 3],), 3),
    (([2, 2, 1, 1, 1, 2, 2],), 2),
    (([1],), 1),
    (([6, 5, 5],), 5),
]

for inputs, expected in tests:
    got = Solution().majorityElement(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Count how many times each number appears.
# Hint 2: 'More than half' means the count is bigger than len(nums) // 2.
# Hint 3: Count with a dictionary, then loop over .items() and return the
#         number whose count is bigger than half.
