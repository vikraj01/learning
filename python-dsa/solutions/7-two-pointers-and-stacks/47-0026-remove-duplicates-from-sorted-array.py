"""
26. Remove Duplicates from Sorted Array  (Easy)
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

In plain words:
    You get a list of numbers, nums, sorted from small to big.
    Some numbers repeat. Change nums so that its first k items are the
    different numbers, each once, in the same order. Return k.
    What's left after the first k items doesn't matter.

    Change nums itself ("in place"); don't make a new list.
    LeetCode checks two things: the k you return, and the first k items
    of nums after your function has run.

Example:
    nums = [1, 1, 2]  ->  return 2, nums starts with [1, 2]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  ->  return 5, nums starts with [0, 1, 2, 3, 4]

You'll need: changing a list in place (page 7), for and range (page 8),
             a slow write pointer and a fast read pointer (page 11)

Run this file:  python3 47-0026-remove-duplicates-from-sorted-array.py
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1  # nums[0] is always kept, so start writing at index 1

        for read in range(1, len(nums)):
            # the list is sorted, so a new number differs from the last kept one
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write = write + 1

        return write  # how many different numbers we kept


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (list before, expected k, expected first k items)
    ([1, 1, 2], 2, [1, 2]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
    ([1], 1, [1]),
    ([1, 2, 3], 3, [1, 2, 3]),
]

# LeetCode checks the k you return AND the list itself after your
# function runs. So we do the same: call it, then look at nums[:k].
for nums, expected_k, expected_start in tests:
    before = nums[:]  # a copy, so we can print the list as it was
    k = Solution().removeDuplicates(nums)
    if k == expected_k and nums[:k] == expected_start:
        print("✓", before, "-> k =", k, "first k:", nums[:k])
    else:
        print("✗", before, "-> got k =", k, "and list", nums,
              "but expected k =", expected_k, "first k:", expected_start)

# ---------- how this works ----------
#
# write is the length of the 'kept' part at the front of the list.
#
# nums = [1, 1, 2], write = 1 (kept: [1])
#   read 1: 1 is the same as nums[0], skip
#   read 2: 2 differs from nums[0], nums[1] = 2 -> [1, 2, 2], write = 2
#   return 2: the first 2 items are [1, 2]
#
# Another way: len(set(nums)) tells you k, but it doesn't change nums,
# and LeetCode checks the list too.
