"""
28. Find the Index of the First Occurrence in a String  (Easy)
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

In plain words:
    You get two strings, haystack and needle. Return the index (position,
    counting from 0) where needle first appears inside haystack.
    If needle isn't in haystack at all, return -1.

Example:
    haystack = "sadbutsad", needle = "sad"   ->  0   (it's at 0 and at 6; the first is 0)
    haystack = "leetcode",  needle = "leeto" ->  -1

You'll need: the string method find (page 6), return (page 4)

Run this file:  python3 11-0028-find-the-index-of-the-first-occurrence.py
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (("sadbutsad", "sad"), 0),
    (("leetcode", "leeto"), -1),
    (("hello", "ll"), 2),
    (("a", "a"), 0),
    (("mississippi", "issip"), 4),
]

for inputs, expected in tests:
    got = Solution().strStr(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: You need a position, not True/False, so `in` alone isn't enough.
# Hint 2: Page 6 has a string method that searches and gives back a position.
#         What does it give when it finds nothing?
# Hint 3: Return haystack.find(needle). It already gives -1 when needle is missing.
