"""
1207. Unique Number of Occurrences  (Easy)
https://leetcode.com/problems/unique-number-of-occurrences/

In plain words:
    You get a list of numbers, arr. Count how many times each number
    appears. Return True if no two numbers have the same count.
    Otherwise return False.

Example:
    arr = [1, 2, 2, 1, 1, 3]  ->  True
    (1 appears 3 times, 2 appears 2 times, 3 appears 1 time: all different)
    arr = [1, 2]              ->  False
    (1 and 2 both appear 1 time)

You'll need: counting with a dictionary, .items() and `in` (page 9)

Run this file:  python3 37-1207-unique-number-of-occurrences.py
"""

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (([1, 2, 2, 1, 1, 3],), True),
    (([1, 2],), False),
    (([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0],), True),
    (([5],), True),
]

for inputs, expected in tests:
    got = Solution().uniqueOccurrences(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: First count how many times each number appears.
# Hint 2: Now the question is about the counts: are any two the same?
# Hint 3: Loop over the counts. Keep a second dictionary of the counts you've
#         seen. If a count is already in it, return False.
