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
        # your code here
        pass


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

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Strings have methods for changing capital and small letters.
# Hint 2: One of them is on page 6, and it's the opposite of upper().
# Hint 3: Return s.lower().
