"""
125. Valid Palindrome  (Easy)
https://leetcode.com/problems/valid-palindrome/

In plain words:
    You get a string s. First clean it: make every letter lowercase and
    throw away everything that isn't a letter or a digit (spaces, commas,
    colons...). Then: does it read the same forwards and backwards?
    Return True or False. An empty string counts as True.

Example:
    s = "A man, a plan, a canal: Panama"  ->  True
    cleaned it is "amanaplanacanalpanama", the same both ways

You'll need: for over a string (page 8), isalnum, lower and [::-1] (page 6)

Run this file:  python3 28-0125-valid-palindrome.py
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (input, expected answer)
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    ("0P", False),
    ("No 'x' in Nixon", True),
]

for s, expected in tests:
    got = Solution().isPalindrome(s)
    if got == expected:
        print("✓", s, "->", got)
    else:
        print("✗", s, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Do it in two parts: first clean the string, then check it.
# Hint 2: Loop over the characters. ch.isalnum() is True for letters and
#         digits. Add the lowercase version of those to a new string.
# Hint 3: Page 6 showed how to reverse a string. Compare the cleaned string
#         with its reverse.
