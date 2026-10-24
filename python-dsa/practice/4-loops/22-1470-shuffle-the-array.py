"""
1470. Shuffle the Array  (Easy)
https://leetcode.com/problems/shuffle-the-array/

In plain words:
    You get a list nums with 2n numbers, and the number n.
    Think of nums as two halves: x1, x2, ..., xn, then y1, y2, ..., yn.
    Return a new list that takes one from each half in turn:
    x1, y1, x2, y2, ..., xn, yn.

Example:
    nums = [2, 5, 1, 3, 4, 7], n = 3  ->  [2, 3, 5, 4, 1, 7]
    halves [2, 5, 1] and [3, 4, 7], zipped together

You'll need: for and range (page 8), indexes and append (page 7)

Run this file:  python3 22-1470-shuffle-the-array.py
"""

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (([2, 5, 1, 3, 4, 7], 3), [2, 3, 5, 4, 1, 7]),
    (([1, 2, 3, 4, 4, 3, 2, 1], 4), [1, 4, 2, 3, 3, 2, 4, 1]),
    (([1, 1, 2, 2], 2), [1, 2, 1, 2]),
    (([8, 9], 1), [8, 9]),
]

for inputs, expected in tests:
    got = Solution().shuffle(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Draw the indexes under nums = [2, 5, 1, 3, 4, 7] with n = 3.
#         Which index is the partner of index 0? Of index 1?
# Hint 2: The partner of index i is always index i + n.
# Hint 3: Loop i over range(n). Each time, append nums[i] and then
#         nums[i + n] to a new list.
