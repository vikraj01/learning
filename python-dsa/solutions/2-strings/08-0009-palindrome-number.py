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
        text = str(x)            # turn the number into text: 121 -> "121"
        backwards = text[::-1]   # the same text, read from the end: "121"
        return text == backwards # True if they match, False if not


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

# ---------- how this works ----------
#
# Reading backwards is easy for strings, so we turn the number into a string
# first, reverse it, and compare.
#
# Example: x = 121
#   text = "121", backwards = "121"   ->  equal  ->  True
# Example: x = -121
#   text = "-121", backwards = "121-" ->  not equal  ->  False
#
# The minus sign takes care of negative numbers for us: it ends up at the
# other end, so they never match.
#
# text == backwards is already True or False, so we can return it directly.
#
# Another way: LeetCode asks "could you do it without turning it into a
# string?" After page 8 (loops) you can: take the last digit with x % 10,
# remove it with x // 10, and build the reversed number step by step.
