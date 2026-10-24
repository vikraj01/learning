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
        # your code here
        pass


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

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Squaring then sorting works. Can you do it without sorting?
# Hint 2: The biggest square is always at one of the two ends of nums
#         (a big negative number or a big positive number).
# Hint 3: Put a pointer at each end. Compare the two squares, put the bigger
#         one at the end of a result list, move that pointer inward.
#         Fill the result from the back to the front.
