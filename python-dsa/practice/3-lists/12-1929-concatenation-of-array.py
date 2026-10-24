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
        # your code here
        pass


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

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: "Concatenation" means joining things end to end.
# Hint 2: Page 7 shows how to join two lists with one operator.
# Hint 3: Return nums + nums.
