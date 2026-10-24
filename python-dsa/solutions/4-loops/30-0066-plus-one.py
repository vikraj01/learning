"""
66. Plus One  (Easy)
https://leetcode.com/problems/plus-one/

In plain words:
    A big number is stored as a list of its digits, most important digit
    first: 123 is [1, 2, 3]. There are no extra zeros at the start.
    Add 1 to the number and return the result as a list of digits.

Example:
    digits = [1, 2, 9]  ->  [1, 3, 0]
    129 + 1 = 130

You'll need: for over a list and [::-1] (pages 8 and 6), % and // (page 2), insert (page 7)

Run this file:  python3 30-0066-plus-one.py
"""

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        answer = []
        carry = 1  # the "+ 1" we're adding, which starts at the last digit

        # walk from the last digit to the first, like adding on paper
        for digit in digits[::-1]:
            total = digit + carry
            answer.insert(0, total % 10)  # the digit to write down (at the front)
            carry = total // 10           # 1 if total was 10, else 0

        # still carrying after the first digit (999 + 1)? add a new 1 in front
        if carry == 1:
            answer.insert(0, 1)

        return answer


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (input, expected answer)
    ([1, 2, 3], [1, 2, 4]),
    ([4, 3, 2, 1], [4, 3, 2, 2]),
    ([9], [1, 0]),
    ([1, 2, 9], [1, 3, 0]),
    ([9, 9, 9], [1, 0, 0, 0]),
]

for digits, expected in tests:
    got = Solution().plusOne(digits)
    if got == expected:
        print("✓", digits, "->", got)
    else:
        print("✗", digits, "-> got", got, "but expected", expected)

# ---------- how this works ----------
#
# Pattern: WALK FROM THE END WITH A CARRY, building a result list. It's
# school addition: the "+ 1" is a carry that starts at the last digit.
# insert(0, ...) puts each new digit at the front, because we're working
# right to left.
#
# Walk through digits = [1, 2, 9]:
#   digit 9: total 9 + 1 = 10 -> write 0, carry 1    answer = [0]
#   digit 2: total 2 + 1 = 3  -> write 3, carry 0    answer = [3, 0]
#   digit 1: total 1 + 0 = 1  -> write 1, carry 0    answer = [1, 3, 0]
#   carry is 0, return [1, 3, 0]
#
# For [9, 9, 9], every digit gives 10, so carry is still 1 at the end and
# a new 1 goes in front: [1, 0, 0, 0].
#
# Another way: turn the digits into a real number, add 1, turn it back.
#     number = int("".join([str(d) for d in digits])) + 1
#     return [int(ch) for ch in str(number)]
# Short, and Python copes with huge numbers. But the carry idea is what
# the problem is really teaching, and other languages need it.
