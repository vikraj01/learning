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

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # your code here
        pass


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

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: A for loop over accounts gives you one customer (one inner list)
#         each time round.
# Hint 2: sum(customer) is that customer's wealth.
# Hint 3: Keep a variable for the biggest wealth seen so far. If this
#         customer beats it, replace it.
