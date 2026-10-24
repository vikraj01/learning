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
        # your code here
        pass


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

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Page 2 showed how to get the last digit of a number with % 10,
#         and the number without its last digit with // 10.
# Hint 2: Do that again and again while n > 0. Each time you get one digit.
# Hint 3: Keep product starting at 1 and total starting at 0. Multiply and
#         add each digit in. Return product - total at the end.
