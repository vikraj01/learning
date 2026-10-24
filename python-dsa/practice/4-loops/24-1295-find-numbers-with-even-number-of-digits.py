"""
1295. Find Numbers with Even Number of Digits  (Easy)
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

In plain words:
    You get a list of positive whole numbers, nums. Count how many of
    them have an even number of digits (2 digits, 4 digits, ...).
    Return that count.

Example:
    nums = [12, 345, 2, 6, 7896]  ->  2
    12 has 2 digits and 7896 has 4; the others have 3, 1 and 1

You'll need: for over a list (page 8), str() and len (page 6), % (page 2)

Run this file:  python3 24-1295-find-numbers-with-even-number-of-digits.py
"""

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (input, expected answer)
    ([12, 345, 2, 6, 7896], 2),
    ([555, 901, 482, 1771], 1),
    ([100000], 1),
    ([1], 0),
]

for nums, expected in tests:
    got = Solution().findNumbers(nums)
    if got == expected:
        print("✓", nums, "->", got)
    else:
        print("✗", nums, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: How many digits does 7896 have? If it were the string "7896",
#         how would you find out?
# Hint 2: str(number) turns the number into a string, and len() counts its
#         characters.
# Hint 3: Keep a counter. For each number, if its digit count % 2 == 0,
#         add 1.
