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
        cheapest = prices[0]  # cheapest price seen so far
        best = 0              # best profit seen so far (0 = don't trade)

        for price in prices:
            if price < cheapest:
                cheapest = price          # a better day to have bought
            profit = price - cheapest     # if we sold today
            if profit > best:
                best = profit

        return best


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

# ---------- how this works ----------
#
# Pattern: BEST-SO-FAR, twice. cheapest is the lowest price so far (the
# best day to have bought); best is the biggest profit so far. One pass
# through the days is enough.
#
# Walk through prices = [7, 1, 5, 3, 6, 4]:
#   day 0, price 7: cheapest 7, profit 0, best 0
#   day 1, price 1: cheapest 1, profit 0, best 0
#   day 2, price 5: cheapest 1, profit 4, best 4
#   day 3, price 3: cheapest 1, profit 2, best 4
#   day 4, price 6: cheapest 1, profit 5, best 5
#   day 5, price 4: cheapest 1, profit 3, best 5
#   return 5
#
# Because cheapest only ever looks backwards, we never "buy" after we
# "sell". In [2, 4, 1] the 1 comes last, so it can't be used: answer 2.
#
# Another way: two nested loops trying every buy day and every later sell
# day (like problem 26) also works, but on LeetCode's long lists it's too
# slow. This one-pass way is the one to remember.
