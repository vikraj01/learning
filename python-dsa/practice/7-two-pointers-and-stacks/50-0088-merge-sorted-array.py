"""
88. Merge Sorted Array  (Easy)
https://leetcode.com/problems/merge-sorted-array/

In plain words:
    You get two lists, nums1 and nums2, both sorted from small to big.
    nums1 has m real numbers, followed by n zeros (empty spaces).
    nums2 has n numbers.
    Put all the numbers into nums1, sorted from small to big.

    Change nums1 itself ("in place"); don't make a new list.
    Your function returns nothing. LeetCode doesn't look at a return value:
    it looks at nums1 after your function has run.

Example:
    nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
        ->  nums1 becomes [1, 2, 2, 3, 5, 6]

You'll need: changing a list in place (page 7), while loops (page 8),
             pointers (page 11)

Run this file:  python3 50-0088-merge-sorted-array.py
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (nums1 before, m, nums2, n, nums1 after)
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
    ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
    ([2, 0], 1, [1], 1, [1, 2]),
]

# LeetCode checks nums1 itself after your function runs, not what
# it returns. So we do the same: call the function, then look at nums1.
for nums1, m, nums2, n, expected in tests:
    before = nums1[:]  # a copy, so we can print the list as it was
    Solution().merge(nums1, m, nums2, n)
    if nums1 == expected:
        print("✓", before, m, nums2, n, "->", nums1)
    else:
        print("✗", before, m, nums2, n, "-> nums1 became", nums1, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Filling nums1 from the front would overwrite numbers you still
#         need. The empty spaces are at the back.
# Hint 2: The biggest number of all is either the last real number of nums1
#         or the last number of nums2.
# Hint 3: Use three positions: i at nums1's last real number, j at nums2's
#         last number, write at nums1's very end. Put the bigger of
#         nums1[i] and nums2[j] at write, move that pointer and write back
#         by one. Keep going while nums2 still has numbers.
