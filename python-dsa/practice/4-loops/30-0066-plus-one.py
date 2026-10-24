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
        # your code here
        pass


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

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Do it the way you add on paper: start at the right-hand end.
#         Usually only the last digit changes. When does more than that
#         change?
# Hint 2: A 9 plus 1 becomes 0, and you carry 1 to the digit on its left.
#         digits[::-1] lets you loop from the end.
# Hint 3: Keep carry = 1 to start. For each digit from the end: total =
#         digit + carry, write down total % 10, the new carry is total // 10.
#         If carry is still 1 at the very end, put a 1 in front.
