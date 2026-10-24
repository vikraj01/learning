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
        jewel_set = set(jewels)  # set("aA") is {"a", "A"}: fast to check

        count = 0
        for stone in stones:
            if stone in jewel_set:
                count = count + 1

        return count


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

# ---------- how this works ----------
#
# Turn jewels into a set, then count the stones found in it.
#
# jewels = "aA" -> {"a", "A"}, stones = "aAAbbbb"
#   a yes (1), A yes (2), A yes (3), b no, b no, b no, b no -> 3
#
# Another way: `stone in jewels` also works on the string itself,
# it's only slower when jewels is long. Shorter still:
# sum([1 for s in stones if s in jewel_set]).
