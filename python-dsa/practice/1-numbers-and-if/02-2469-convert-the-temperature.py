"""
2469. Convert the Temperature  (Easy)
https://leetcode.com/problems/convert-the-temperature/

In plain words:
    You get a temperature in Celsius (a decimal number, like 36.50).
    Convert it to Kelvin and to Fahrenheit, using these formulas:

        kelvin     = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00

    Return both, as a list of two numbers: [kelvin, fahrenheit].
    Answers that are off by a tiny amount (less than 0.00001) still count.

Example:
    celsius = 36.50   ->  [309.65, 97.7]
    celsius = 122.11  ->  [395.26, 251.798]

You'll need: + and * with decimal numbers (page 2), return (page 4),
          returning two values in a list written as [a, b] (page 5)

Run this file:  python3 02-2469-convert-the-temperature.py
"""

from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (celsius, expected answer)
    (36.50, [309.65, 97.7]),
    (122.11, [395.26, 251.798]),
    (0, [273.15, 32.0]),
    (-40, [233.15, -40.0]),
]

for celsius, expected in tests:
    got = Solution().convertTemperature(celsius)
    # Decimal maths can be a tiny bit off (36.5 + 273.15 may come out as
    # 309.65000000000003), so we round both answers to 5 decimal places before
    # comparing. LeetCode allows the same small difference.
    if got is not None and [round(got[0], 5), round(got[1], 5)] == expected:
        print("✓", celsius, "->", got)
    else:
        print("✗", celsius, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: The two formulas are already in the problem. Write each one as a line of
#         Python, with celsius in it.
# Hint 2: Keep each answer in its own variable, for example kelvin and fahrenheit.
# Hint 3: Return both in square brackets, Kelvin first: [kelvin, fahrenheit].
