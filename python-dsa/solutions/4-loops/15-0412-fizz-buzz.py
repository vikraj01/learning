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

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        # range(1, n + 1) gives 1, 2, ..., n  (the end is not included, so + 1)
        for number in range(1, n + 1):
            # check "both" first, or 15 would stop at "Fizz"
            if number % 3 == 0 and number % 5 == 0:
                answer.append("FizzBuzz")
            elif number % 3 == 0:
                answer.append("Fizz")
            elif number % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(number))

        return answer


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

# ---------- how this works ----------
#
# Pattern: BUILD A RESULT LIST. Start empty, append one thing per loop
# step, return the list at the end.
#
# Walk through n = 5:
#   number 1: not 3, not 5      -> append "1"     answer = ["1"]
#   number 2: same              -> append "2"     answer = ["1", "2"]
#   number 3: 3 % 3 == 0        -> append "Fizz"
#   number 4: nothing           -> append "4"
#   number 5: 5 % 5 == 0        -> append "Buzz"  answer = ["1","2","Fizz","4","Buzz"]
#
# The order of the checks matters: 15 divides by 3 too, so if "Fizz" came
# first, 15 would never reach "FizzBuzz".
#
# Another way: build the word piece by piece.
#     word = ""
#     if number % 3 == 0: word += "Fizz"
#     if number % 5 == 0: word += "Buzz"
#     if word == "": word = str(number)
# Two plain ifs (not elif), so 15 gets both pieces.
