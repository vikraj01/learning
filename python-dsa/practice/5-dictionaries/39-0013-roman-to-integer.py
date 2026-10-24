"""
13. Roman to Integer  (Easy)
https://leetcode.com/problems/roman-to-integer/

In plain words:
    You get a Roman numeral s, like "LVIII". Return its value as a number.

    The letters are worth:
        I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

    Usually you add the letters up, biggest first: "LVIII" = 50+5+1+1+1 = 58.
    But when a smaller letter comes right before a bigger one, you
    subtract it instead: "IV" = 5 - 1 = 4, "CM" = 1000 - 100 = 900.
    s is always a valid numeral between 1 and 3999.

Example:
    s = "III"      ->  3
    s = "LVIII"    ->  58
    s = "MCMXCIV"  ->  1994   (1000 + 900 + 90 + 4)

You'll need: indexes (page 6), for and range (page 8),
             a dictionary to look values up (page 9)

Run this file:  python3 39-0013-roman-to-integer.py
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (("III",), 3),
    (("LVIII",), 58),
    (("MCMXCIV",), 1994),
    (("IV",), 4),
    (("MMMCMXCIX",), 3999),
]

for inputs, expected in tests:
    got = Solution().romanToInt(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Put the seven letter values in a dictionary.
# Hint 2: Walk the string with an index i, so you can also look at the
#         next letter, s[i + 1]. Be careful not to go past the end.
# Hint 3: If the next letter is bigger than this one, subtract this
#         letter's value. Otherwise add it.
