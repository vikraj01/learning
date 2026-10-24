"""
344. Reverse String  (Easy)
https://leetcode.com/problems/reverse-string/

In plain words:
    You get a list of single characters, s, like ["h", "e", "l", "l", "o"].
    Reverse it IN PLACE: change the list s itself, so its last item becomes
    the first, and so on. Don't make a new list, and don't return anything.

Example:
    s = ["h", "e", "l", "l", "o"]  ->  s becomes ["o", "l", "l", "e", "h"]

You'll need: changing a list in place, reverse (page 7)

Run this file:  python3 13-0344-reverse-string.py
"""

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (s before, what s should be after)
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
    (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    (["a", "b"], ["b", "a"]),
    (["x", "y", "z"], ["z", "y", "x"]),
]

for start, expected in tests:
    s = start[:]   # a copy, so the list in tests stays as it was
    Solution().reverseString(s)
    # This function returns nothing. LeetCode looks at the list s after your
    # function has run, so that's what we check here too.
    if s == expected:
        print("✓", start, "->", s)
    else:
        print("✗", start, "-> s is", s, "but should be", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: The answer isn't returned. LeetCode looks at the list you were given
#         afterwards, so you must change that same list.
# Hint 2: s = s[::-1] looks right but doesn't work: it makes a new list and only
#         moves the name s inside your function. LeetCode's list stays the same.
# Hint 3: Lists have a method (page 7) that reverses the list itself.
