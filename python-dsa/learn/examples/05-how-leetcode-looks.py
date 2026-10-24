# Page 5: How a LeetCode problem looks
# Run me with:  python3 05-how-leetcode-looks.py
#
# This is the shape every LeetCode answer has, with a small made-up
# problem: "You get a number n. Return n doubled."

class Solution:                           # the box LeetCode puts your function in
    def double(self, n: int) -> int:      # self: always first, ignore it for now
        return n * 2                      # n: int  means "n is a whole number"
                                          # -> int  means "it gives back a whole number"


# How to call a function that lives inside the box:
# Solution() makes the box, .double(4) calls the function in it.
print(Solution().double(4))     # 8
print(Solution().double(-3))    # -6


# A small checker, built only from things you know (pages 1 to 4).
# The practice files do the same job with a few lines you'll learn later.
def check(n, expected):
    got = Solution().double(n)
    if got == expected:
        print("✓", n, "->", got)
    else:
        print("✗", n, "-> got", got, "but expected", expected)

check(4, 8)
check(-3, -6)
check(0, 0)

# Try changing things:
#   1. Change  return n * 2  to  return n * 3. Run it. Which lines show ✗?
#   2. Change it to  print(n * 2). What does "got" show now, and why?
#   3. Put  return n * 2  back so every line shows ✓.
