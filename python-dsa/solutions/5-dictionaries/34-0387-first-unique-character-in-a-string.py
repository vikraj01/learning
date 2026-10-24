"""
387. First Unique Character in a String  (Easy)
https://leetcode.com/problems/first-unique-character-in-a-string/

In plain words:
    You get a string s (only lowercase letters).
    Find the first letter that appears only once in the whole string,
    and return its index. If every letter repeats, return -1.

Example:
    s = "leetcode"      ->  0   ("l" appears once, at index 0)
    s = "loveleetcode"  ->  2   ("v" appears once, at index 2)
    s = "aabb"          ->  -1

You'll need: enumerate (page 8), counting with a dictionary (page 9)

Run this file:  python3 34-0387-first-unique-character-in-a-string.py
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # first pass: count every letter
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        # second pass: the first letter with count 1 wins
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i

        return -1  # no letter appears only once


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (("leetcode",), 0),
    (("loveleetcode",), 2),
    (("aabb",), -1),
    (("z",), 0),
    (("aadadaad",), -1),
]

for inputs, expected in tests:
    got = Solution().firstUniqChar(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- how this works ----------
#
# Two walks over the string: one to count, one to find.
#
# s = "loveleetcode"
#   counts: l=2, o=2, v=1, e=4, t=1, c=1, d=1
#   index 0 "l": 2, no.  index 1 "o": 2, no.  index 2 "v": 1, yes -> 2
#
# Another way: counts = collections.Counter(s) does the first walk for you.
