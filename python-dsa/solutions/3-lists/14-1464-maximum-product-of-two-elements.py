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
        nums.sort()              # smallest first, biggest last: [3, 4, 5, 2] -> [2, 3, 4, 5]
        biggest = nums[-1]       # last item
        second = nums[-2]        # the one before it
        return (biggest - 1) * (second - 1)


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

# ---------- how this works ----------
#
# Every number is at least 1, so after taking 1 away nothing is negative.
# Then the biggest product always comes from the two biggest numbers.
# Sorting puts them at the end, where [-1] and [-2] can reach them.
#
# Example: nums = [3, 4, 5, 2]
#   sorted          ->  [2, 3, 4, 5]
#   biggest = 5, second = 4
#   (5 - 1) * (4 - 1) = 4 * 3 = 12
#
# If the biggest number appears twice, like [1, 5, 4, 5], sorting gives
# [1, 4, 5, 5], and [-1] and [-2] are both 5. That's allowed: they're at
# different positions.
#
# Another way: after page 8 (loops) you can find the two biggest in one walk
# through the list, keeping a "biggest so far" and "second biggest so far".
# That's faster than sorting on very long lists.
