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

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()  # numbers we've already passed

        for num in nums:
            if num in seen:
                return True  # we've met this number before
            seen.add(num)

        return False  # got to the end, no repeats


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

# ---------- how this works ----------
#
# A set remembers what we've seen. A repeat is a number already in it.
#
# nums = [1, 2, 3, 1]
#   1: not seen, add -> {1}
#   2: not seen, add -> {1, 2}
#   3: not seen, add -> {1, 2, 3}
#   1: already in the set -> True
#
# Another way: a set drops repeats, so len(set(nums)) != len(nums)
# is True exactly when there's a duplicate.
