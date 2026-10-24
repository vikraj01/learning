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
        if n == 0:
            return 0

        before = 0  # F(0)
        current = 1  # F(1)

        # each time round, move one place along the sequence
        for step in range(n - 1):
            next_one = before + current
            before = current
            current = next_one

        return current


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

# ---------- how this works ----------
#
# Pattern: keep the LAST TWO VALUES and slide them along. before and
# current are always two neighbours in the sequence. Each loop step moves
# both one place to the right.
#
# Walk through n = 4 (the loop runs n - 1 = 3 times):
#   start:   before 0, current 1    (F(0), F(1))
#   step 1:  next 1 -> before 1, current 1   (F(1), F(2))
#   step 2:  next 2 -> before 1, current 2   (F(2), F(3))
#   step 3:  next 3 -> before 2, current 3   (F(3), F(4))
#   return current = 3
#
# For n = 1 the loop runs 0 times and we return current = 1.
#
# Another way: keep the whole sequence in a list.
#     numbers = [0, 1]
#     for i in range(2, n + 1):
#         numbers.append(numbers[i - 1] + numbers[i - 2])
#     return numbers[n]
