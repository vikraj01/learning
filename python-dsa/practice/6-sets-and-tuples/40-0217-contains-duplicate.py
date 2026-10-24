"""
217. Contains Duplicate  (Easy)
https://leetcode.com/problems/contains-duplicate/

In plain words:
    You get a list of numbers, nums.
    Return True if any number appears at least twice.
    Return False if every number is different.

Example:
    nums = [1, 2, 3, 1]  ->  True
    nums = [1, 2, 3, 4]  ->  False

You'll need: for loops (page 8), a set with add and `in` (page 10)

Run this file:  python3 40-0217-contains-duplicate.py
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (([1, 2, 3, 1],), True),
    (([1, 2, 3, 4],), False),
    (([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],), True),
    (([7],), False),
]

for inputs, expected in tests:
    got = Solution().containsDuplicate(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Walk the list and remember every number you've passed.
# Hint 2: A set is a good place to remember things: `in` on a set is fast.
# Hint 3: For each number: if it's already in the set, return True.
#         Otherwise add it. If the loop ends, return False.
