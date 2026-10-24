"""
121. Best Time to Buy and Sell Stock  (Easy)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

In plain words:
    You get a list prices, where prices[i] is a share's price on day i.
    You may buy once and sell once, and you must buy before you sell (on
    a later day). Return the biggest profit (sell price minus buy price)
    you can make. If no deal makes money, return 0.

Example:
    prices = [7, 1, 5, 3, 6, 4]  ->  5
    buy on day 1 at 1, sell on day 4 at 6: 6 - 1 = 5

You'll need: for over a list (page 8), if (page 3), indexing (page 7)

Run this file:  python3 31-0121-best-time-to-buy-and-sell-stock.py
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (input, expected answer)
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([2, 4, 1], 2),
    ([3, 8, 1, 6], 5),
    ([1], 0),
]

for prices, expected in tests:
    got = Solution().maxProfit(prices)
    if got == expected:
        print("✓", prices, "->", got)
    else:
        print("✗", prices, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Pretend you're living through the days one by one. On each day,
#         ask: "if I sold today, what's the best I could have done?"
# Hint 2: To answer that, you only need the cheapest price from the days
#         so far, not the whole list.
# Hint 3: Keep two variables: cheapest so far, and best profit so far. Each
#         day: update cheapest if today is lower, then check
#         today - cheapest against best.
