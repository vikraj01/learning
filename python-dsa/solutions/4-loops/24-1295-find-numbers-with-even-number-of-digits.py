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

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0

        for number in nums:
            digits = len(str(number))  # 7896 -> "7896" -> 4
            if digits % 2 == 0:
                count += 1

        return count


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

# ---------- how this works ----------
#
# Pattern: COUNTER. Start at 0, add 1 every time a number passes the test.
#
# Walk through nums = [12, 345, 2, 6, 7896]:
#   12   -> "12"   -> 2 digits, even -> count = 1
#   345  -> "345"  -> 3 digits, odd
#   2    -> "2"    -> 1 digit,  odd
#   6    -> "6"    -> 1 digit,  odd
#   7896 -> "7896" -> 4 digits, even -> count = 2
#   return 2
#
# Another way, without strings: count digits by chopping them off with // 10.
#     digits = 0
#     while number > 0:
#         number = number // 10
#         digits += 1
