"""
509. Fibonacci Number  (Easy)
https://leetcode.com/problems/fibonacci-number/

In plain words:
    The Fibonacci numbers start 0, 1, and every next one is the sum of
    the two before it: 0, 1, 1, 2, 3, 5, 8, 13, ...
    F(0) is 0, F(1) is 1. You get n (between 0 and 30). Return F(n).

Example:
    n = 4  ->  3
    0, 1, 1, 2, 3  (counting from F(0), the one at place 4 is 3)

You'll need: for and range (page 8), if (page 3)

Run this file:  python3 20-0509-fibonacci-number.py
"""


class Solution:
    def fib(self, n: int) -> int:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (input, expected answer)
    (2, 1),
    (3, 2),
    (4, 3),
    (0, 0),
    (1, 1),
    (10, 55),
]

for n, expected in tests:
    got = Solution().fib(n)
    if got == expected:
        print("✓", n, "->", got)
    else:
        print("✗", n, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Write the sequence on paper: 0, 1, 1, 2, 3, 5, 8. To get the next
#         number, which numbers do you look at?
# Hint 2: You only ever need the last two numbers. Keep them in two
#         variables.
# Hint 3: Each time round the loop: next = the two added; then the second
#         becomes the first, and next becomes the second. Watch out for
#         n = 0 and n = 1.
