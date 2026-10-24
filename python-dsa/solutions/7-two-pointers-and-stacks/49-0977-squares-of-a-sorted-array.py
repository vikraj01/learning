"""
977. Squares of a Sorted Array  (Easy)
https://leetcode.com/problems/squares-of-a-sorted-array/

In plain words:
    You get a list of numbers, nums, sorted from small to big.
    It can have negative numbers. Square every number (x * x) and
    return a new list of the squares, also sorted from small to big.

Example:
    nums = [-4, -1, 0, 3, 10]  ->  [0, 1, 9, 16, 100]
    nums = [-7, -3, 2, 3, 11]  ->  [4, 9, 9, 49, 121]

You'll need: while loops and list comprehensions (page 8),
             left and right pointers from both ends (page 11)

Run this file:  python3 49-0977-squares-of-a-sorted-array.py
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0 for i in range(n)]  # n empty spots to fill

        left = 0  # start of nums
        right = n - 1  # end of nums
        spot = n - 1  # we fill result from the end (biggest first)

        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            # the biggest square is always at one of the two ends
            if left_square > right_square:
                result[spot] = left_square
                left = left + 1
            else:
                result[spot] = right_square
                right = right - 1
            spot = spot - 1

        return result


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (([-4, -1, 0, 3, 10],), [0, 1, 9, 16, 100]),
    (([-7, -3, 2, 3, 11],), [4, 9, 9, 49, 121]),
    (([5],), [25]),
    (([-3, -2, -1],), [1, 4, 9]),
]

for inputs, expected in tests:
    got = Solution().sortedSquares(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- how this works ----------
#
# The biggest squares are at the ends, so we take from the ends and fill
# the result from the back.
#
# nums = [-4, -1, 0, 3, 10]
#   -4 -> 16 vs 10 -> 100: 100 wins, result [_, _, _, _, 100]
#   -4 -> 16 vs 3 -> 9:    16 wins,  result [_, _, _, 16, 100]
#   -1 -> 1  vs 3 -> 9:    9 wins,   result [_, _, 9, 16, 100]
#   -1 -> 1  vs 0 -> 0:    1 wins,   result [_, 1, 9, 16, 100]
#   0 -> 0 (left meets right),       result [0, 1, 9, 16, 100]
#
# Another way: return sorted([x * x for x in nums]). Shorter, a bit slower.
