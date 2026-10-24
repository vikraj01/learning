"""
383. Ransom Note  (Easy)
https://leetcode.com/problems/ransom-note/

In plain words:
    You get two strings, ransomNote and magazine (only lowercase letters).
    Can you build ransomNote by cutting letters out of magazine?
    Each letter in magazine can be used only once.
    Return True or False.

Example:
    ransomNote = "aa", magazine = "ab"   ->  False  (only one "a")
    ransomNote = "aa", magazine = "aab"  ->  True

You'll need: for loops (page 8), counting with a dictionary and
             .get(key, 0) (page 9)

Run this file:  python3 35-0383-ransom-note.py
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (("a", "b"), False),
    (("aa", "ab"), False),
    (("aa", "aab"), True),
    (("abc", "cbad"), True),
]

for inputs, expected in tests:
    got = Solution().canConstruct(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Think of the magazine as a box of letter tiles.
# Hint 2: Count how many of each letter the magazine has.
# Hint 3: Walk the note. For each letter, if the count is 0, return False.
#         Otherwise take one away from the count.
