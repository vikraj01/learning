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
        write = 0  # where the next non-zero number should go

        for read in range(len(nums)):
            if nums[read] != 0:
                # swap the non-zero number forward to the write spot
                nums[write], nums[read] = nums[read], nums[write]
                write = write + 1


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

# ---------- how this works ----------
#
# read visits every number; write marks where the next non-zero belongs.
# Swapping sends the non-zero forward and the zero backward.
#
# nums = [0, 1, 0, 3, 12], write = 0
#   read 0: 0, skip
#   read 1: 1, swap with index 0 -> [1, 0, 0, 3, 12], write = 1
#   read 2: 0, skip
#   read 3: 3, swap with index 1 -> [1, 3, 0, 0, 12], write = 2
#   read 4: 12, swap with index 2 -> [1, 3, 12, 0, 0], write = 3
