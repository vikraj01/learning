"""
1281. Subtract the Product and Sum of Digits of an Integer  (Easy)
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

In plain words:
    You get a positive whole number n. Multiply all its digits together
    (the product), and add all its digits together (the sum).
    Return product minus sum.

Example:
    n = 234  ->  15
    product 2*3*4 = 24, sum 2+3+4 = 9, 24 - 9 = 15

You'll need: while (page 8), % 10 and // 10 (page 2)

Run this file:  python3 19-1281-subtract-the-product-and-sum-of-digits.py
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1  # start at 1: multiplying by 0 would wipe everything out
        total = 0    # start at 0 for adding

        while n > 0:
            digit = n % 10  # the last digit: 234 % 10 is 4
            n = n // 10     # drop the last digit: 234 // 10 is 23
            product = product * digit
            total += digit

        return product - total


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (input, expected answer)
    (234, 15),
    (4421, 21),
    (5, 0),
    (10, -1),
]

for n, expected in tests:
    got = Solution().subtractProductAndSum(n)
    if got == expected:
        print("✓", n, "->", got)
    else:
        print("✗", n, "-> got", got, "but expected", expected)

# ---------- how this works ----------
#
# Pattern: WHILE-TAKE-DIGITS. % 10 takes the last digit off, // 10 throws
# it away. Repeat until nothing is left. Along the way, keep a running
# product and a running total.
#
# Walk through n = 234:
#   n 234: digit 4, n becomes 23   product 4,  total 4
#   n 23:  digit 3, n becomes 2    product 12, total 7
#   n 2:   digit 2, n becomes 0    product 24, total 9
#   n is 0, stop. Return 24 - 9 = 15.
#
# Another way: turn the number into a string and loop over its characters.
#     for ch in str(n):
#         digit = int(ch)
#         ...
# Same answer; the % and // way is worth knowing because many number
# problems use it.
