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
        s.reverse()   # turns the list s itself around; nothing new is made


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

# ---------- how this works ----------
#
# s.reverse() changes the list s itself: no new list, no return. That's
# what "in place" means, and it's what LeetCode checks.
#
# Example: s = ["h", "e", "l", "l", "o"]
#   after s.reverse(), the same list is ["o", "l", "l", "e", "h"]
#
# Why s = s[::-1] fails: s[::-1] builds a NEW list. Then s = ... sticks the
# name s on that new list, but only inside your function. The list LeetCode
# gave you, and checks afterwards, was never touched.
#
# Another way: s[:] = s[::-1]. The [:] on the left means "replace everything
# inside this same list", so the original list does change. After page 11
# you'll also do it with two pointers, swapping the ends and walking inwards.
