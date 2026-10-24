"""
485. Max Consecutive Ones  (Easy)
https://leetcode.com/problems/max-consecutive-ones/

In plain words:
    You get a list nums that holds only 0s and 1s. Find the longest run
    of 1s in a row, with no 0 in between. Return its length.

Example:
    nums = [1, 1, 0, 1, 1, 1]  ->  3
    there's a run of two 1s, then a 0, then a run of three 1s

You'll need: for over a list (page 8), if/else (page 3)

Run this file:  python3 25-0485-max-consecutive-ones.py
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (input, expected answer)
    ([1, 1, 0, 1, 1, 1], 3),
    ([1, 0, 1, 1, 0, 1], 2),
    ([0, 0], 0),
    ([1], 1),
]

for nums, expected in tests:
    got = Solution().findMaxConsecutiveOnes(nums)
    if got == expected:
        print("✓", nums, "->", got)
    else:
        print("✗", nums, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Imagine counting days in a row you went for a walk. A missed
#         day resets the count to 0, but you still remember your record.
# Hint 2: You need two variables: the current run, and the longest run
#         so far.
# Hint 3: On a 1: current goes up by 1, and if it beats longest, update
#         longest. On a 0: current goes back to 0.
