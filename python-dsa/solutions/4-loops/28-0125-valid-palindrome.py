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
        cleaned = ""

        # keep only letters and digits, in lowercase
        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        # a palindrome is the same as its reverse
        return cleaned == cleaned[::-1]


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

# ---------- how this works ----------
#
# Pattern: BUILD A RESULT (a cleaned string), then compare it with its
# reverse.
#
# Walk through s = "race a car":
#   r a c e     -> kept         cleaned = "race"
#   " "         -> not alnum, skipped
#   a           -> kept         cleaned = "racea"
#   " "         -> skipped
#   c a r       -> kept         cleaned = "raceacar"
#   reversed:  "racaecar"   not the same -> False
#
# " " cleans down to "", and "" reversed is still "", so it's True.
#
# Another way: build the cleaned string with a list comprehension and join.
#     cleaned = "".join([ch.lower() for ch in s if ch.isalnum()])
# Page 11 shows a way that skips building a new string: two pointers, one
# from each end, walking towards the middle.
