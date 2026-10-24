"""
1929. Concatenation of Array  (Easy)
https://leetcode.com/problems/concatenation-of-array/

In plain words:
    You get a list of numbers, nums. Return a new list that is nums followed
    by nums again (so it's twice as long).

Example:
    nums = [1, 2, 1]     ->  [1, 2, 1, 1, 2, 1]
    nums = [1, 3, 2, 1]  ->  [1, 3, 2, 1, 1, 3, 2, 1]

You'll need: joining lists with + (page 7), return (page 4)

Run this file:  python3 12-1929-concatenation-of-array.py
"""

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = nums + nums   # + puts two lists one after the other, in a new list
        return ans


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (nums, expected answer)
    ([1, 2, 1], [1, 2, 1, 1, 2, 1]),
    ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]),
    ([5], [5, 5]),
]

for nums, expected in tests:
    got = Solution().getConcatenation(nums)
    if got == expected:
        print("✓", nums, "->", got)
    else:
        print("✗", nums, "-> got", got, "but expected", expected)

# ---------- how this works ----------
#
# + with two lists makes a new list: everything from the first, then
# everything from the second. Here both are nums.
#
# Example: nums = [1, 2, 1]
#   [1, 2, 1] + [1, 2, 1]  ->  [1, 2, 1, 1, 2, 1]
#
# nums itself doesn't change; + builds a new list.
#
# Another way: * repeats a list, the same as it repeats a string:
#     return nums * 2
