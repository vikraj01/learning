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
        merged = ""

        # loop as many times as the longer word is long
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):      # word1 still has a letter here
                merged += word1[i]
            if i < len(word2):      # word2 still has a letter here
                merged += word2[i]

        return merged


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

# ---------- how this works ----------
#
# Pattern: BUILD A RESULT (a string this time), walking both words with
# one index. The two ifs skip a word once it has run out.
#
# Walk through word1 = "ab", word2 = "pqrs" (loop runs 4 times):
#   i = 0: add "a", add "p"   merged = "ap"
#   i = 1: add "b", add "q"   merged = "apbq"
#   i = 2: word1 is done,     add "r"   merged = "apbqr"
#   i = 3: word1 is done,     add "s"   merged = "apbqrs"
#
# Another way: loop only as far as the shorter word, then glue on the
# leftovers with slicing.
#     short = min(len(word1), len(word2))
#     for i in range(short):
#         merged += word1[i] + word2[i]
#     return merged + word1[short:] + word2[short:]
# (One of the two leftover slices is always "".)
