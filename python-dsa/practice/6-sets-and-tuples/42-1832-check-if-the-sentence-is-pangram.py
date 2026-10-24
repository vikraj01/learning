"""
1832. Check if the Sentence Is Pangram  (Easy)
https://leetcode.com/problems/check-if-the-sentence-is-pangram/

In plain words:
    You get a string sentence (only lowercase letters, no spaces).
    A pangram uses every letter of the alphabet, a to z, at least once.
    Return True if sentence is a pangram, otherwise False.

Example:
    sentence = "thequickbrownfoxjumpsoverthelazydog"  ->  True
    sentence = "leetcode"                             ->  False

You'll need: len (page 6), set() and len(set(...)) (page 10)

Run this file:  python3 42-1832-check-if-the-sentence-is-pangram.py
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (("thequickbrownfoxjumpsoverthelazydog",), True),
    (("leetcode",), False),
    (("abcdefghijklmnopqrstuvwxyz",), True),
    (("abcdefghijklmnopqrstuvwxy",), False),
]

for inputs, expected in tests:
    got = Solution().checkIfPangram(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Repeated letters don't matter. Only which letters appear.
# Hint 2: What does set() do to repeats?
# Hint 3: There are 26 letters from a to z. Count the different letters
#         in the sentence and compare with 26.
