"""
412. Fizz Buzz  (Easy)
https://leetcode.com/problems/fizz-buzz/

In plain words:
    You get a number n. Make a list of strings, one for every number
    from 1 to n (both included):
      - "FizzBuzz" if the number divides by 3 and by 5,
      - "Fizz" if it divides by 3 only,
      - "Buzz" if it divides by 5 only,
      - otherwise the number itself, as a string ("7", not 7).
    Return the list.

Example:
    n = 5  ->  ["1", "2", "Fizz", "4", "Buzz"]

You'll need: for and range (page 8), % (page 2), if/elif/else (page 3), str() (page 6), append (page 7)

Run this file:  python3 15-0412-fizz-buzz.py
"""

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------

tests = [
    # (input, expected answer)
    (3, ["1", "2", "Fizz"]),
    (5, ["1", "2", "Fizz", "4", "Buzz"]),
    (15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
          "11", "Fizz", "13", "14", "FizzBuzz"]),
    (1, ["1"]),
]

for n, expected in tests:
    got = Solution().fizzBuzz(n)
    if got == expected:
        print("✓", n, "->", got)
    else:
        print("✗", n, "-> got", got, "but expected", expected)

# ---------- hints: read only if you're stuck ----------
#
# Hint 1: Start with an empty list, answer = [], and add one string to it
#         for every number. Return it at the end.
# Hint 2: range(1, n + 1) walks 1, 2, ..., n. "Divides by 3" means
#         number % 3 == 0.
# Hint 3: Check the "divides by 3 and by 5" case FIRST, then 3, then 5,
#         then else. Use str(number) for the plain numbers.
