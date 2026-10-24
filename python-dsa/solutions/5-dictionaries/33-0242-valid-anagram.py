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
        # different lengths can never be anagrams
        if len(s) != len(t):
            return False

        # count every letter in s
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        # take one away for every letter in t
        for ch in t:
            counts[ch] = counts.get(ch, 0) - 1
            if counts[ch] < 0:
                # t has more of this letter than s
                return False

        return True


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

# ---------- how this works ----------
#
# Same length + same letter counts = anagram.
# We count s's letters, then 'spend' them while walking t.
#
# s = "rat", t = "car": counts after s = {"r": 1, "a": 1, "t": 1}
#   "c": counts["c"] becomes -1, below 0, so return False.
# If we get through t without going below 0, and the lengths are equal,
# every count is back to exactly 0, so the letters match.
#
# Another way: sorted(s) == sorted(t), or collections.Counter(s) == Counter(t).
