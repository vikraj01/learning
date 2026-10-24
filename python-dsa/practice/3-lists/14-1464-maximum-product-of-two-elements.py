"""
1464. Maximum Product of Two Elements in an Array  (Easy)
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

In plain words:
    You get a list of whole numbers, nums (at least 2 of them, each 1 or more).
    Pick two items at different positions. Take 1 away from each, and multiply.
    Return the biggest answer you can get.

Example:
    nums = [3, 4, 5, 2]  ->  12   (pick 5 and 4: (5-1) * (4-1) = 4 * 3 = 12)
    nums = [1, 5, 4, 5]  ->  16   (pick both 5s: (5-1) * (5-1) = 16)

You'll need: sort and indexing with [-1] and [-2] (page 7), - and * (page 2), return (page 4)

Run this file:  python3 14-1464-maximum-product-of-two-elements.py
"""

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (nums, expected answer)
    ([3, 4, 5, 2], 12),
    ([1, 5, 4, 5], 16),
    ([3, 7], 12),
    ([1, 1], 0),
    ([10, 2, 5, 2], 36),
]

for nums, expected in tests:
    got = Solution().maxProduct(nums[:])   # pass a copy, so the list printed below is unchanged
    if got == expected:
        print("✓", nums, "->", got)
    else:
        print("✗", nums, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: All numbers are 1 or more, so the biggest product comes from the two
#         biggest numbers.
# Hint 2: How can you get the two biggest? If the list were in order, where would
#         they be?
# Hint 3: Sort the list, take the last two items ([-1] and [-2]), subtract 1 from
#         each, and multiply.
