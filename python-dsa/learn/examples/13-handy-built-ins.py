# Page 13: Handy built-ins
# Run me with:  python3 13-handy-built-ins.py

import math

# Letters are numbers: ord and chr
print(ord("a"), chr(97))                 # 97 a
word = "hello"
counts = [0] * 26                        # box 0 is 'a', box 25 is 'z'
for ch in word:
    counts[ord(ch) - ord("a")] += 1
for i in range(26):
    if counts[i] > 0:
        print(chr(ord("a") + i), counts[i])

# Infinity as a start value for "smallest so far"
prices = [7, 1, 5, 3]
cheapest = float("inf")
for p in prices:
    if p < cheapest:
        cheapest = p
print("cheapest:", cheapest)             # 1

# abs and divmod
print(abs(3 - 10))                       # 7  (distance between 3 and 10)
hours, minutes = divmod(135, 60)
print(hours, "h", minutes, "min")        # 2 h 15 min

# // rounds down, int(a / b) chops towards zero
print(-7 // 2, int(-7 / 2))              # -4 -3

# zip and enumerate(start=1)
names = ["Tanvi", "Riya", "Aman"]
marks = [82, 95, 82]
for name, mark in zip(names, marks):
    print(name, mark)
for place, name in enumerate(names, start=1):
    print(place, name)

# Sorting with key= and lambda
pairs = list(zip(names, marks))          # [('Tanvi', 82), ('Riya', 95), ('Aman', 82)]
print(sorted(pairs, key=lambda p: p[1]))            # by marks, low to high
print(sorted(pairs, key=lambda p: (-p[1], p[0])))   # marks high to low, then name A-Z
print(max(pairs, key=lambda p: p[1]))               # the top scorer

words = ["kiwi", "banana", "fig"]
print(sorted(words, key=len))            # shortest first

# any and all
print(any([m > 90 for m in marks]))      # True: someone scored above 90
print(all([m > 80 for m in marks]))      # True: everyone scored above 80

# Build a string with a list, then join once
parts = []
for ch in "Hi, Tanvi!":
    if ch.isalpha():
        parts.append(ch.lower())
print("".join(parts))                    # hitanvi

# count, and a few from math
print("banana".count("a"))               # 3
print(math.gcd(12, 18), math.sqrt(16), math.ceil(7 / 2))   # 6 4.0 4

# Try changing things:
#   1. Count the letters of your own name with the 26-box list.
#   2. Sort words by their last letter with a lambda.
#   3. Change marks so two people tie for the top. Which one does max pick?
