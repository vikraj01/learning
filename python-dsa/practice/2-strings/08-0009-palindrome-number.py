"""
9. Palindrome Number  (Easy)
https://leetcode.com/problems/palindrome-number/

In plain words:
    You get a whole number x. Return True if it reads the same forwards and
    backwards (a "palindrome"), and False if it doesn't.
    Negative numbers are never palindromes: -121 backwards is 121-.

Example:
    x = 121   ->  True
    x = -121  ->  False
    x = 10    ->  False   (backwards it's 01)

You'll need: str() and slicing with [::-1] (page 6), == (page 3), return (page 4)

Run this file:  python3 08-0009-palindrome-number.py
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (x, expected answer)
    (121, True),
    (-121, False),
    (10, False),
    (0, True),
    (12321, True),
]

for x, expected in tests:
    got = Solution().isPalindrome(x)
    if got == expected:
        print("✓", x, "->", got)
    else:
        print("✗", x, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Numbers can't be read backwards easily, but text can. Can you turn the
#         number into text?
# Hint 2: str(x) gives text. Page 6 shows a slice that reverses a string.
# Hint 3: Make the text, make its reversed copy with [::-1], and return whether
#         the two are equal (==).
