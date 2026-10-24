"""
27. Remove Element  (Easy)
https://leetcode.com/problems/remove-element/

In plain words:
    You get a list of numbers, nums, and a number, val.
    Remove every val: change nums so that its first k items are the
    numbers that are not val. Return k.
    The first k items can be in any order, and what's left after them
    doesn't matter.

    Change nums itself ("in place"); don't make a new list.
    LeetCode checks two things: the k you return, and the first k items
    of nums after your function has run.

Example:
    nums = [3, 2, 2, 3], val = 3  ->  return 2, nums starts with [2, 2]
    nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2  ->  return 5,
        nums starts with 0, 1, 3, 0, 4 (in any order)

You'll need: changing a list in place (page 7), for and range (page 8),
             a slow write pointer and a fast read pointer (page 11)

Run this file:  python3 48-0027-remove-element.py
"""

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        write = 0  # where the next number we keep should go

        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]  # keep it
                write = write + 1

        return write  # how many numbers we kept


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (list before, val, expected k, expected first k items)
    ([3, 2, 2, 3], 3, 2, [2, 2]),
    ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]),
    ([], 0, 0, []),
    ([4, 4], 4, 0, []),
    ([1], 2, 1, [1]),
]

# LeetCode checks the k you return AND the list itself after your
# function runs. So we do the same: call it, then look at nums[:k].
# The first k items may be in any order, so we sort them before comparing.
for nums, val, expected_k, expected_start in tests:
    before = nums[:]  # a copy, so we can print the list as it was
    k = Solution().removeElement(nums, val)
    if k == expected_k and sorted(nums[:k]) == sorted(expected_start):
        print("✓", before, "val =", val, "-> k =", k, "first k:", nums[:k])
    else:
        print("✗", before, "val =", val, "-> got k =", k, "and list", nums,
              "but expected k =", expected_k, "first k:", expected_start)

# ---------- how this works ----------
#
# Every number that isn't val gets copied to the front, at write.
#
# nums = [3, 2, 2, 3], val = 3, write = 0
#   read 0: 3 is val, skip
#   read 1: 2, nums[0] = 2 -> [2, 2, 2, 3], write = 1
#   read 2: 2, nums[1] = 2 -> [2, 2, 2, 3], write = 2
#   read 3: 3 is val, skip
#   return 2: the first 2 items are [2, 2]
