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
        seen = set()

        for num in nums:
            if num in seen:
                seen.remove(num)  # second time: it has a pair, drop it
            else:
                seen.add(num)  # first time: keep it for now

        # every pair cancelled out; one number is left in the set
        for num in seen:
            return num


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

# ---------- how this works ----------
#
# Numbers with a pair get added, then removed. The single one stays.
#
# nums = [4, 1, 2, 1, 2]
#   4 -> {4}   1 -> {4, 1}   2 -> {4, 1, 2}
#   1 again -> {4, 2}   2 again -> {4}   left: 4
# The last loop runs once and returns the only number in the set.
#
# A curiosity for later: ^ (XOR) cancels equal numbers (5 ^ 5 is 0), so
# XOR-ing every number together leaves the single one, with no set at all.
