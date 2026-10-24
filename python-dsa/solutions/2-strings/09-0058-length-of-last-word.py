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
        words = s.split()       # split() with no argument cuts at spaces and drops the extra ones
                                # "  fly me  " -> ["fly", "me"]
        last_word = words[-1]   # [-1] is the last one, the same as with strings
        return len(last_word)   # how many letters it has


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

# ---------- how this works ----------
#
# split() cuts the sentence at the spaces and gives back the words. With no
# argument it also throws away extra spaces, so trailing spaces can't
# confuse us. Then [-1] picks the last word and len() counts its letters.
#
# Example: s = "   fly me   to   the moon  "
#   s.split()   ->  ["fly", "me", "to", "the", "moon"]
#   words[-1]   ->  "moon"
#   len("moon") ->  4
#
# Careful: s.split(" ") (with a space inside) is different. It keeps empty
# pieces for the extra spaces, and the last piece could be "".
#
# Another way: in one line,  return len(s.split()[-1]).  After page 8 (loops)
# you could also walk from the end of s: skip spaces, then count letters.
