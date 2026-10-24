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
        current = 0  # length of the run we're in right now
        longest = 0  # longest run seen so far

        for number in nums:
            if number == 1:
                current += 1        # the run gets one longer
                if current > longest:
                    longest = current
            else:
                current = 0         # a 0 breaks the run

        return longest


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

# ---------- how this works ----------
#
# Pattern: COUNTER + BEST-SO-FAR. current counts the run we're in;
# longest remembers the record. A 0 resets current but not longest.
#
# Walk through nums = [1, 1, 0, 1, 1, 1]:
#   1: current 1, longest 1
#   1: current 2, longest 2
#   0: current 0, longest 2   (the run is broken)
#   1: current 1, longest 2
#   1: current 2, longest 2
#   1: current 3, longest 3
#   return 3
#
# Another way: split the list into runs by turning it into a string.
#     text = "".join([str(n) for n in nums])   # "110111"
#     runs = text.split("0")                   # ["11", "111"]
#     return max([len(run) for run in runs])
# Clever, but the loop above is the pattern you'll reuse elsewhere.
