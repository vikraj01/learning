"""
387. First Unique Character in a String  (Easy)
https://leetcode.com/problems/first-unique-character-in-a-string/

In plain words:
    You get a string s (only lowercase letters).
    Find the first letter that appears only once in the whole string,
    and return its index. If every letter repeats, return -1.

Example:
    s = "leetcode"      ->  0   ("l" appears once, at index 0)
    s = "loveleetcode"  ->  2   ("v" appears once, at index 2)
    s = "aabb"          ->  -1

You'll need: enumerate (page 8), counting with a dictionary (page 9)

Run this file:  python3 34-0387-first-unique-character-in-a-string.py
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (("leetcode",), 0),
    (("loveleetcode",), 2),
    (("aabb",), -1),
    (("z",), 0),
    (("aadadaad",), -1),
]

for inputs, expected in tests:
    got = Solution().firstUniqChar(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: You can't know a letter is unique until you've seen the whole string.
# Hint 2: So walk the string twice.
# Hint 3: First walk: count every letter in a dictionary. Second walk (with
#         enumerate): return the index of the first letter whose count is 1.
