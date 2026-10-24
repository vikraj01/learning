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
        # a set keeps each letter only once
        different_letters = set(sentence)

        # the alphabet has 26 letters; we need all of them
        return len(different_letters) == 26


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

# ---------- how this works ----------
#
# set(sentence) keeps one copy of each letter. Since the sentence has
# only lowercase letters, 26 different letters means all of a to z.
#
# sentence = "leetcode" -> {"l", "e", "t", "c", "o", "d"}: 6 letters, not 26 -> False
#
# Another way: loop over "abcdefghijklmnopqrstuvwxyz" and return False
# as soon as a letter is not `in` the sentence.
