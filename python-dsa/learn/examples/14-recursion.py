# Page 14: Recursion
# Run me with:  python3 14-recursion.py

from functools import cache


# A function that calls itself. Base case first, then the smaller step.
def countdown(n):
    if n == 0:              # base case: the doll that doesn't open
        print("Go!")
        return
    print(n)
    countdown(n - 1)        # smaller step: n gets closer to 0

countdown(3)


# Watch the calls go down, then the answers come back up
def factorial(n, depth):
    pad = "    " * depth
    print(pad + f"factorial({n}) starts")
    if n == 1:
        print(pad + "base case: return 1")
        return 1
    answer = n * factorial(n - 1, depth + 1)
    print(pad + f"factorial({n}) returns {answer}")
    return answer

print(factorial(4, 0))      # 24


# A helper inside a LeetCode-style method
class Solution:
    def countEvens(self, nums: list[int]) -> int:
        count = 0

        def visit(i):
            nonlocal count          # remove this line to see UnboundLocalError
            if i == len(nums):
                return
            if nums[i] % 2 == 0:
                count += 1
            visit(i + 1)

        visit(0)
        return count

    def findEvens(self, nums: list[int]) -> list[int]:
        found = []                  # collect into a list: no nonlocal needed

        def visit(i):
            if i == len(nums):
                return
            if nums[i] % 2 == 0:
                found.append(nums[i])
            visit(i + 1)

        visit(0)
        return found

print(Solution().countEvens([4, 7, 2, 8]))   # 3
print(Solution().findEvens([4, 7, 2, 8]))    # [4, 2, 8]


# How many calls does fib make, without and with @cache?
def count_calls(n):
    calls = 0

    def fib(k):
        nonlocal calls
        calls += 1
        if k < 2:
            return k
        return fib(k - 1) + fib(k - 2)

    print(f"plain:  fib({n}) = {fib(n)}, using {calls} calls")


def count_calls_cached(n):
    calls = 0

    @cache                          # remember every answer
    def fib(k):
        nonlocal calls
        calls += 1
        if k < 2:
            return k
        return fib(k - 1) + fib(k - 2)

    print(f"cached: fib({n}) = {fib(n)}, using {calls} calls")

count_calls(20)
count_calls_cached(20)

# Try changing things:
#   1. Change countdown(n - 1) to countdown(n - 2) and call countdown(3). What goes wrong?
#   2. Call factorial(6, 0) and follow the trace.
#   3. Try count_calls(25) and count_calls_cached(25).
