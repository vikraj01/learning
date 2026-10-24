"""
242. Valid Anagram  (Easy)
https://leetcode.com/problems/valid-anagram/

In plain words:
    You get two words, s and t (only lowercase letters).
    Return True if t uses exactly the same letters as s, the same number
    of times each, just in a different order. Otherwise return False.
    (Such a word is called an anagram: "listen" and "silent".)

Example:
    s = "anagram", t = "nagaram"  ->  True
    s = "rat", t = "car"          ->  False

You'll need: len (page 6), for loops (page 8),
             counting with a dictionary and .get(key, 0) (page 9)

Run this file:  python3 33-0242-valid-anagram.py
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (("anagram", "nagaram"), True),
    (("rat", "car"), False),
    (("a", "ab"), False),
    (("aacc", "ccac"), False),
    (("listen", "silent"), True),
]

for inputs, expected in tests:
    got = Solution().isAnagram(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: If the two words have different lengths, the answer is False.
# Hint 2: Count how many times each letter appears (the counting pattern
#         from page 9).
# Hint 3: Count the letters of s. Then walk t and take one away for each
#         letter. If a count ever goes below 0, return False.
