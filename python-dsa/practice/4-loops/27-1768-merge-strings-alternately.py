"""
1768. Merge Strings Alternately  (Easy)
https://leetcode.com/problems/merge-strings-alternately/

In plain words:
    You get two strings, word1 and word2. Build a new string by taking
    letters in turn: one from word1, one from word2, one from word1, and
    so on. If one word is longer, put the rest of it on the end.
    Return the new string.

Example:
    word1 = "ab", word2 = "pqrs"  ->  "apbqrs"
    a p b q, then word1 has run out, so add the rest "rs"

You'll need: for and range (page 8), indexing, len and slicing (page 6), max (page 7)

Run this file:  python3 27-1768-merge-strings-alternately.py
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (("abc", "pqr"), "apbqcr"),
    (("ab", "pqrs"), "apbqrs"),
    (("abcd", "pq"), "apbqcd"),
    (("a", "z"), "az"),
]

for inputs, expected in tests:
    got = Solution().mergeAlternately(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Use an index i that goes 0, 1, 2, ... and take word1[i] then
#         word2[i] each time.
# Hint 2: The words can have different lengths. How many times should the
#         loop run so that nothing is left out?
# Hint 3: Loop up to the longer length. Before taking word1[i], check that
#         i < len(word1) (and the same for word2), or you'll get an
#         IndexError.
