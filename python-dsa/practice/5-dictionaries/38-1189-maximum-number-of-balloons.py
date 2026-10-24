"""
1189. Maximum Number of Balloons  (Easy)
https://leetcode.com/problems/maximum-number-of-balloons/

In plain words:
    You get a string text (only lowercase letters).
    You want to spell the word "balloon" as many times as you can,
    using each letter of text at most once.
    Return how many times you can spell it.
    Careful: "balloon" needs two "l"s and two "o"s.

Example:
    text = "nlaebolko"         ->  1
    text = "loonbalxballpoon"  ->  2
    text = "leetcode"          ->  0

You'll need: // (page 2), min and append (page 7),
             counting with a dictionary, .get and .items() (page 9)

Run this file:  python3 38-1189-maximum-number-of-balloons.py
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    (("nlaebolko",), 1),
    (("loonbalxballpoon",), 2),
    (("leetcode",), 0),
    (("balloonballoon",), 2),
    (("balon",), 0),
]

for inputs, expected in tests:
    got = Solution().maxNumberOfBalloons(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Count the letters in text.
# Hint 2: If you have 4 "l"s, they're enough for 4 // 2 = 2 balloons.
# Hint 3: For each letter of "balloon", work out how many balloons that
#         letter alone allows (count // how many one balloon needs).
#         The smallest of those numbers is the answer.
