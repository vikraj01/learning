"""
771. Jewels and Stones  (Easy)
https://leetcode.com/problems/jewels-and-stones/

In plain words:
    You get two strings. Each letter in jewels is a kind of stone that is
    a jewel (all different letters). Each letter in stones is a stone you
    have. Return how many of your stones are jewels.
    Upper and lower case are different: "a" and "A" are different stones.

Example:
    jewels = "aA", stones = "aAAbbbb"  ->  3
    jewels = "z",  stones = "ZZ"       ->  0

You'll need: for loops (page 8), a set and `in` (page 10)

Run this file:  python3 41-0771-jewels-and-stones.py
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (("aA", "aAAbbbb"), 3),
    (("z", "ZZ"), 0),
    (("b", "bbb"), 3),
    (("abc", "xyz"), 0),
]

for inputs, expected in tests:
    got = Solution().numJewelsInStones(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Walk through stones one letter at a time.
# Hint 2: For each stone, ask: is this letter one of the jewels?
# Hint 3: Put the jewels in a set, then count the stones that are `in` it.
