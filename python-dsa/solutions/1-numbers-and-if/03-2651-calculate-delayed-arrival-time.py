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
        total = arrivalTime + delayedTime  # the hour, if the clock never went back to 0
        return total % 24                  # remove full days: keep what's left over after 24


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

# ---------- how this works ----------
#
# Add the delay to the arrival hour. If the total reaches 24 or more, we've
# gone past midnight. % 24 gives the remainder after dividing by 24, which is
# exactly the hour on the clock.
#
# Example: arrivalTime = 22, delayedTime = 3
#   total = 22 + 3   ->  25
#   25 % 24          ->  1   (24 fits once, 1 is left over)
#   so the train arrives at 1 o'clock.
#
# If total is less than 24, % 24 leaves it alone: 20 % 24 is 20.
#
# Another way: with if. The total is never more than 47, so subtracting 24
# once is enough:
#     if total >= 24:
#         return total - 24
#     return total
