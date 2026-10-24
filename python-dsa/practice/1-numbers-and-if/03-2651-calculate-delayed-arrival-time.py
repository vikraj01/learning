"""
2651. Calculate Delayed Arrival Time  (Easy)
https://leetcode.com/problems/calculate-delayed-arrival-time/

In plain words:
    A train should arrive at hour arrivalTime (on a 24-hour clock, 0 to 23).
    It is late by delayedTime hours. Return the hour it actually arrives.
    After 23 the clock goes back to 0, so 24 o'clock is 0.

    arrivalTime is between 1 and 23. delayedTime is between 1 and 24.

Example:
    arrivalTime = 15, delayedTime = 5   ->  20
    arrivalTime = 13, delayedTime = 11  ->  0   (13 + 11 = 24, which is 0 o'clock)

You'll need: + and % (page 2), return (page 4)

Run this file:  python3 03-2651-calculate-delayed-arrival-time.py
"""


class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (inputs, expected answer)
    ((15, 5), 20),
    ((13, 11), 0),
    ((23, 24), 23),
    ((22, 3), 1),
]

for inputs, expected in tests:
    got = Solution().findDelayedArrivalTime(*inputs)
    if got == expected:
        print("✓", inputs, "->", got)
    else:
        print("✗", inputs, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Add the two numbers first. What goes wrong when the total is 24 or more?
# Hint 2: A clock 'wraps around': 25 o'clock is 1, 24 o'clock is 0. Which operator
#         from page 2 gives you the remainder after dividing?
# Hint 3: Add them, then take the remainder after dividing by 24 (that's % 24).
