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
        # find() gives the index where needle first starts, or -1 if it isn't there
        position = haystack.find(needle)
        return position


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

# ---------- how this works ----------
#
# find() searches haystack from the start and gives back the index where
# needle first begins. If it never finds it, it gives -1, which is exactly
# what the problem asks for.
#
# Example: haystack = "hello", needle = "ll"
#    h  e  l  l  o
#    0  1  2  3  4
#   "ll" starts at index 2  ->  "hello".find("ll") is 2
#
# Another way: after page 8 (loops) you could check every starting index i
# yourself and compare haystack[i:i + len(needle)] with needle. That's how
# find() works inside, and it's what LeetCode wants you to practise.
