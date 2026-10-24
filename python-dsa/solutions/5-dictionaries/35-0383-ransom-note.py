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
        # count the letters we have in the magazine
        counts = {}
        for ch in magazine:
            counts[ch] = counts.get(ch, 0) + 1

        # use one letter from the magazine for every letter of the note
        for ch in ransomNote:
            if counts.get(ch, 0) == 0:
                return False  # none of this letter left
            counts[ch] = counts[ch] - 1

        return True


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

# ---------- how this works ----------
#
# Count the magazine's letters, then spend them on the note.
#
# ransomNote = "aa", magazine = "ab": counts = {"a": 1, "b": 1}
#   first "a": count is 1, take one -> 0
#   second "a": count is 0, nothing left -> False
#
# Another way: with collections.Counter, check that
# Counter(ransomNote) <= Counter(magazine).
