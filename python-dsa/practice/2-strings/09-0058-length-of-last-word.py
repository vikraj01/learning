"""
58. Length of Last Word  (Easy)
https://leetcode.com/problems/length-of-last-word/

In plain words:
    You get a string s made of words and spaces. Return how many letters the
    last word has. A word is a run of letters with no spaces in it.
    There can be extra spaces anywhere, even at the end.
    There is always at least one word.

Example:
    s = "Hello World"                  ->  5   ("World")
    s = "   fly me   to   the moon  "   ->  4   ("moon")

You'll need: split, indexing with [-1] and len (page 6), return (page 4)

Run this file:  python3 09-0058-length-of-last-word.py
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (s, expected answer)
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6),
    ("a", 1),
    ("day   ", 3),
]

for s, expected in tests:
    got = Solution().lengthOfLastWord(s)
    # repr() prints text with its quotes, so you can see spaces at the start or end
    if got == expected:
        print("✓", repr(s), "->", got)
    else:
        print("✗", repr(s), "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: First get the words out of the sentence, without the spaces.
# Hint 2: split() with nothing in the brackets cuts at spaces and ignores extra
#         ones. What does it give for "day   "? Try it with print.
# Hint 3: Split, take the last word with [-1], and return its len().
