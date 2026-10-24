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
        answer = []

        for i in range(n):
            answer.append(nums[i])      # from the first half
            answer.append(nums[i + n])  # its partner, n places later

        return answer


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

# ---------- how this works ----------
#
# Pattern: BUILD A RESULT LIST, using range to get indexes.
# The first half lives at indexes 0 to n-1. Each one's partner sits exactly
# n places later.
#
#     nums:   [ 2,  5,  1,  3,  4,  7 ]      n = 3
#     index:    0   1   2   3   4   5
#
# Walk through it:
#   i = 0: append nums[0] = 2, nums[3] = 3   answer = [2, 3]
#   i = 1: append nums[1] = 5, nums[4] = 4   answer = [2, 3, 5, 4]
#   i = 2: append nums[2] = 1, nums[5] = 7   answer = [2, 3, 5, 4, 1, 7]
#
# Another way: slice the halves first, then walk both at once.
#     first = nums[:n]
#     second = nums[n:]
#     for i in range(n):
#         answer.append(first[i])
#         answer.append(second[i])
