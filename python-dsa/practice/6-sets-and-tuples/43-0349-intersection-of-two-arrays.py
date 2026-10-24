"""
349. Intersection of Two Arrays  (Easy)
https://leetcode.com/problems/intersection-of-two-arrays/

In plain words:
    You get two lists of numbers, nums1 and nums2.
    Return a list of the numbers that appear in both lists.
    Each number appears only once in your answer, even if it repeats
    in the lists. The order of your answer doesn't matter.

Example:
    nums1 = [1, 2, 2, 1], nums2 = [2, 2]        ->  [2]
    nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]  ->  [4, 9]  (or [9, 4])

You'll need: list comprehensions (page 8), set() and & (page 10)

Run this file:  python3 43-0349-intersection-of-two-arrays.py
"""

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (([1, 2, 2, 1], [2, 2]), [2]),
    (([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9]),
    (([1, 2], [3, 4]), []),
    (([3], [3]), [3]),
]

# Any order is allowed, so we sort your answer before comparing.
for inputs, expected in tests:
    got = Solution().intersection(*inputs)
    if got is not None and sorted(got) == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: 'Only once in the answer' sounds like a job for a set.
# Hint 2: Page 10 showed an operator that keeps what two sets share.
# Hint 3: Turn both lists into sets, use &, then turn the result back
#         into a list.
