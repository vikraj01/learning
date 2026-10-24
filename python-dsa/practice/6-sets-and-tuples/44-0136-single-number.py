"""
136. Single Number  (Easy)
https://leetcode.com/problems/single-number/

In plain words:
    You get a list of numbers, nums. Every number appears exactly twice,
    except one number, which appears only once. Return that one.

Example:
    nums = [2, 2, 1]        ->  1
    nums = [4, 1, 2, 1, 2]  ->  4

You'll need: for loops (page 8), a set with add, remove and `in` (page 10)

Run this file:  python3 44-0136-single-number.py
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (([2, 2, 1],), 1),
    (([4, 1, 2, 1, 2],), 4),
    (([1],), 1),
    (([-1, 5, -1],), 5),
]

for inputs, expected in tests:
    got = Solution().singleNumber(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Picture a table. A number arrives: put it on the table.
#         Its twin arrives: take both off.
# Hint 2: A set can be that table (add and remove).
# Hint 3: For each number: if it's in the set, remove it; otherwise add it.
#         At the end, one number is left in the set.
