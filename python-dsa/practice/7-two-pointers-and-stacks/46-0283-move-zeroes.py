"""
283. Move Zeroes  (Easy)
https://leetcode.com/problems/move-zeroes/

In plain words:
    You get a list of numbers, nums. Move every 0 to the end of the list.
    The other numbers must stay in the same order as before.

    Change nums itself ("in place"); don't make a new list.
    Your function returns nothing. LeetCode doesn't look at a return value:
    it looks at the list nums after your function has run.

Example:
    nums = [0, 1, 0, 3, 12]  ->  nums becomes [1, 3, 12, 0, 0]

You'll need: changing a list in place (page 7), for and range (page 8),
             swapping a, b = b, a (page 10),
             a slow write pointer and a fast read pointer (page 11)

Run this file:  python3 46-0283-move-zeroes.py
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (list before, list after)
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0], [0]),
    ([1, 2, 3], [1, 2, 3]),
    ([0, 0, 1], [1, 0, 0]),
]

# LeetCode checks the list itself after your function runs, not what
# it returns. So we do the same: call the function, then look at nums.
for nums, expected in tests:
    before = nums[:]  # a copy, so we can print the list as it was
    Solution().moveZeroes(nums)
    if nums == expected:
        print("✓", before, "->", nums)
    else:
        print("✗", before, "-> list became", nums, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Use two positions: one reads every number, one marks where the
#         next non-zero number should be written.
# Hint 2: The read position moves every step. The write position moves
#         only when you find a non-zero number.
# Hint 3: When nums[read] is not 0, swap nums[read] and nums[write], then
#         move write forward by one.
