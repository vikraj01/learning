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
        # count every number
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1

        # a second dictionary remembers which counts we've already seen
        seen_counts = {}
        for num, count in counts.items():
            if count in seen_counts:
                return False  # another number had this same count
            seen_counts[count] = True

        return True


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

# ---------- how this works ----------
#
# Two steps: count the numbers, then check the counts for repeats.
#
# arr = [1, 2]: counts = {1: 1, 2: 1}
#   number 1, count 1: not seen yet, remember it.
#   number 2, count 1: already seen -> False
#
# Another way (after page 10): a set keeps only different values, so
# len(set(counts.values())) == len(counts) answers it in one line.
