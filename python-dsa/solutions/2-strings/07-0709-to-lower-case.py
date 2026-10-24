"""
709. To Lower Case  (Easy)
https://leetcode.com/problems/to-lower-case/

In plain words:
    You get a string s. Return it with every capital letter changed to a
    small letter. Everything else (small letters, digits, symbols) stays
    the same.

Example:
    s = "Hello"   ->  "hello"
    s = "LOVELY"  ->  "lovely"

You'll need: the string method lower (page 6), return (page 4)

Run this file:  python3 07-0709-to-lower-case.py
"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        # lower() gives back a copy of s with all capital letters made small
        return s.lower()


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (s, expected answer)
    ("Hello", "hello"),
    ("here", "here"),
    ("LOVELY", "lovely"),
    ("a1B2-C!", "a1b2-c!"),
]

for s, expected in tests:
    got = Solution().toLowerCase(s)
    # repr() prints text with its quotes, so you can see spaces at the start or end
    if got == expected:
        print("✓", repr(s), "->", repr(got))
    else:
        print("✗", repr(s), "-> got", repr(got), "but expected", repr(expected))

# ---------- how this works ----------
#
# lower() goes through the string for you and changes every capital letter
# to a small one. Digits and symbols have no capital form, so they stay.
#
# Example: s = "a1B2-C!"
#   "a1B2-C!".lower()  ->  "a1b2-c!"
#
# lower() doesn't change s itself. It gives back a new string, which we return.
#
# Another way: after page 8 (loops) you could go through s one character at
# a time and change each capital letter yourself. That's what LeetCode wants
# you to think about, but in real Python, lower() is the right tool.
