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

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m - 1  # last real number in nums1
        j = n - 1  # last number in nums2
        write = m + n - 1  # last spot in nums1

        # fill nums1 from the back, biggest number first
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[write] = nums1[i]
                i = i - 1
            else:
                nums1[write] = nums2[j]
                j = j - 1
            write = write - 1
        # when nums2 is used up, what's left of nums1 is already in place


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

# ---------- how this works ----------
#
# Fill nums1 from the back, so we only write into empty spaces or spots
# we've already copied away.
#
# nums1 = [1, 2, 3, 0, 0, 0], nums2 = [2, 5, 6]
#   3 vs 6: 6 -> [1, 2, 3, 0, 0, 6]
#   3 vs 5: 5 -> [1, 2, 3, 0, 5, 6]
#   3 vs 2: 3 -> [1, 2, 3, 3, 5, 6]
#   2 vs 2: 2 (from nums2) -> [1, 2, 2, 3, 5, 6], nums2 used up, done
#
# Another way: copy nums2 into the zeros, then nums1.sort().
# Shorter, but sorting does more work than needed.
