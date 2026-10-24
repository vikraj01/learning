"""
1672. Richest Customer Wealth  (Easy)
https://leetcode.com/problems/richest-customer-wealth/

In plain words:
    You get a list of customers. Each customer is a list of the money
    they have in each bank, so accounts is a list of lists.
    A customer's wealth is the total of their list.
    Return the wealth of the richest customer.

Example:
    accounts = [[1, 2, 3], [3, 2, 1]]  ->  6
    both customers have 1+2+3 = 6

You'll need: for over a list (page 8), sum and lists in lists (page 7), if (page 3)

Run this file:  python3 17-1672-richest-customer-wealth.py
"""

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richest = 0  # best wealth seen so far (money is never negative)

        for customer in accounts:
            # customer is one inner list, like [1, 2, 3]
            wealth = sum(customer)
            if wealth > richest:
                richest = wealth  # a new best: remember it

        return richest


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (input, expected answer)
    ([[1, 2, 3], [3, 2, 1]], 6),
    ([[1, 5], [7, 3], [3, 5]], 10),
    ([[2, 8, 7], [7, 1, 3], [1, 9, 5]], 17),
    ([[4]], 4),
]

for accounts, expected in tests:
    got = Solution().maximumWealth(accounts)
    if got == expected:
        print("✓", accounts, "->", got)
    else:
        print("✗", accounts, "-> got", got, "but expected", expected)

# ---------- how this works ----------
#
# Pattern: BEST-SO-FAR. Keep the best answer seen so far, and replace it
# whenever something better turns up.
#
# Walk through accounts = [[1, 5], [7, 3], [3, 5]]:
#   start:               richest = 0
#   customer [1, 5]:     wealth 6,  6 > 0   -> richest = 6
#   customer [7, 3]:     wealth 10, 10 > 6  -> richest = 10
#   customer [3, 5]:     wealth 8,  8 > 10? no, keep 10
#   return 10
#
# Another way: make a list of every customer's wealth with a list
# comprehension, then take the max.
#     return max([sum(customer) for customer in accounts])
