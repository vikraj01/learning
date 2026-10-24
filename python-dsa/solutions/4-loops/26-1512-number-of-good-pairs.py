"""
1512. Number of Good Pairs  (Easy)
https://leetcode.com/problems/number-of-good-pairs/

In plain words:
    You get a list of numbers, nums. A "good pair" is two different
    places i and j, with i before j (i < j), that hold the same number:
    nums[i] == nums[j]. Return how many good pairs there are.

Example:
    nums = [1, 2, 3, 1, 1, 3]  ->  4
    the pairs of indexes are (0,3), (0,4), (3,4) (all 1s) and (2,5) (both 3s)

You'll need: nested for loops, range(len(...)) (page 8), == (page 3)

Run this file:  python3 26-1512-number-of-good-pairs.py
"""

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0

        # i is the first place of the pair
        for i in range(len(nums)):
            # j is the second place, always after i, so each pair is
            # counted once and a place is never paired with itself
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1

        return count


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (input, expected answer)
    ([1, 2, 3, 1, 1, 3], 4),
    ([1, 1, 1, 1], 6),
    ([1, 2, 3], 0),
    ([5], 0),
]

for nums, expected in tests:
    got = Solution().numIdenticalPairs(nums)
    if got == expected:
        print("✓", nums, "->", got)
    else:
        print("✗", nums, "-> got", got, "but expected", expected)

# ---------- how this works ----------
#
# Pattern: NESTED PAIRS. The outer loop picks the first place i, the inner
# loop tries every place j after it. That visits each pair exactly once.
#
# Walk through nums = [1, 1, 1, 1] (indexes 0 to 3):
#   i = 0: j = 1, 2, 3  -> all equal, count = 3
#   i = 1: j = 2, 3     -> all equal, count = 5
#   i = 2: j = 3        -> equal,     count = 6
#   i = 3: j has nothing after it
#   return 6
#
# For a list of 100 numbers this checks about 5000 pairs. Fine here.
#
# Another way (after page 9): a dictionary counts how many times you've
# seen each number. When a number turns up again, it makes a new pair with
# every earlier copy, so you add that count. One loop instead of two, which
# is much faster for long lists.
