"""
169. Majority Element  (Easy)
https://leetcode.com/problems/majority-element/

In plain words:
    You get a list of numbers, nums. One number appears more than half
    of the time (more than len(nums) // 2 times). Return that number.
    There is always such a number.

Example:
    nums = [3, 2, 3]              ->  3
    nums = [2, 2, 1, 1, 1, 2, 2]  ->  2

You'll need: // (page 2), len (page 7),
             counting with a dictionary and .items() (page 9)

Run this file:  python3 36-0169-majority-element.py
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # count every number
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # find the one that appears more than half the time
        half = len(nums) // 2
        for num, count in counts.items():
            if count > half:
                return num


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (([3, 2, 3],), 3),
    (([2, 2, 1, 1, 1, 2, 2],), 2),
    (([1],), 1),
    (([6, 5, 5],), 5),
]

for inputs, expected in tests:
    got = Solution().majorityElement(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- how this works ----------
#
# Count, then look for the count that's bigger than half.
#
# nums = [2, 2, 1, 1, 1, 2, 2]: counts = {2: 4, 1: 3}, half = 7 // 2 = 3
#   2 has count 4, and 4 > 3, so return 2.
#
# Another way: sort the list. The majority number fills more than half,
# so it's always in the middle: sorted(nums)[len(nums) // 2].
