"""
14. Longest Common Prefix  (Easy)
https://leetcode.com/problems/longest-common-prefix/

In plain words:
    You get a list of words, strs (at least one word). Find the longest
    start (prefix) that ALL the words share. Return it, or "" if they
    don't even share the first letter.

Example:
    strs = ["flower", "flow", "flight"]  ->  "fl"
    all three start with "fl"; the third letters o, o, i are not all equal

You'll need: nested for loops, range(len(...)) (page 8), indexing and slicing (page 6)

Run this file:  python3 29-0014-longest-common-prefix.py
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (input, expected answer)
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
    (["alone"], "alone"),
    (["ab", "a"], "a"),
    (["", "b"], ""),
]

for strs, expected in tests:
    got = Solution().longestCommonPrefix(strs)
    if got == expected:
        print("✓", strs, "->", got)
    else:
        print("✗", strs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Write the words one under the other, lined up on the left.
#         Read down the columns: column 0, then column 1, ...
# Hint 2: Use the first word as the guide. For each place i in it, check
#         that every word has the same letter at place i.
# Hint 3: As soon as one word is too short or has a different letter at i,
#         return first[:i]. If you get through every place, return the
#         whole first word.
