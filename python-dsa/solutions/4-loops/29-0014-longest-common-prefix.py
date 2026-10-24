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
        first = strs[0]

        # check the first word one letter at a time
        for i in range(len(first)):
            letter = first[i]
            # does every word have this same letter at place i?
            for word in strs:
                if i >= len(word) or word[i] != letter:
                    # this word is too short, or has a different letter:
                    # the shared part is everything before place i
                    return first[:i]

        # every letter of the first word was shared
        return first


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

# ---------- how this works ----------
#
# Pattern: NESTED LOOPS, column by column. The outer loop picks a place i
# in the first word; the inner loop checks that place in every word. The
# first mismatch ends everything with return.
#
#     f l o w e r
#     f l o w
#     f l i g h t
#     ^ ^ ^
#     0 1 2   <- column 2: o, o, i don't match
#
# Walk through it:
#   i = 0: letter "f", all words have "f" at 0, keep going
#   i = 1: letter "l", all words have "l" at 1, keep going
#   i = 2: letter "o", "flight"[2] is "i"  -> return first[:2] = "fl"
#
# The check i >= len(word) comes first so that word[i] is never read past
# the end (that would be an IndexError). With "or", Python stops at the
# first True part.
#
# Another way: sort the words. Then only the first and last word need
# comparing, because they're the most different.
