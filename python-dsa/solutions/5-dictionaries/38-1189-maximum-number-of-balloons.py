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
        # count the letters we have
        counts = {}
        for ch in text:
            counts[ch] = counts.get(ch, 0) + 1

        # how many of each letter one "balloon" needs
        needed = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}

        # for each letter: how many balloons could this letter alone make?
        possible = []
        for letter, need in needed.items():
            possible.append(counts.get(letter, 0) // need)

        # the letter we're shortest on decides the answer
        return min(possible)


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

# ---------- how this works ----------
#
# Each letter limits how many balloons you can make. The tightest
# limit wins.
#
# text = "loonbalxballpoon"
#   b: 2 // 1 = 2   a: 2 // 1 = 2   l: 4 // 2 = 2
#   o: 4 // 2 = 2   n: 2 // 1 = 2   -> min is 2
# text = "balon": l: 1 // 2 = 0, so the answer is 0.
#
# Another way: collections.Counter(text) builds the counts for you.
