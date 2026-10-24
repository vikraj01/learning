# Page 8: Loops
# Run me with:  python3 08-loops.py

nums = [3, 8, 5, 9, 2]

# for: once per item
for n in nums:
    print("item:", n)

# range(len(nums)) gives the indexes 0, 1, 2, ...
for i in range(len(nums)):
    print("index", i, "holds", nums[i])

# enumerate gives index and item together
for i, n in enumerate(nums):
    print(i, n)

# Counting down with a negative step: 4, 3, 2, 1, 0
for i in range(len(nums) - 1, -1, -1):
    print("from the back:", nums[i])

# --- The four patterns ---

# 1. Build a result list
doubled = []
for n in nums:
    doubled.append(n * 2)
print("doubled:", doubled)            # [6, 16, 10, 18, 4]

# 2. Running total
total = 0
for n in nums:
    total += n
print("total:", total)                # 27

# 3. Counter
evens = 0
for n in nums:
    if n % 2 == 0:
        evens += 1
print("even numbers:", evens)         # 2

# 4. Best so far
best = nums[0]
for n in nums:
    if n > best:
        best = n
print("biggest:", best)               # 9

# --- while ---

# Take a number apart, digit by digit
number = 472
digit_sum = 0
while number > 0:
    digit = number % 10      # last digit
    digit_sum += digit
    number = number // 10    # drop the last digit
print("sum of digits of 472:", digit_sum)   # 13

# break: stop as soon as you find it
for n in nums:
    if n > 6:
        print("first number above 6:", n)   # 8
        break

# continue: skip this one, go to the next
for n in nums:
    if n % 2 == 0:
        continue
    print("odd:", n)                        # 3, 5, 9

# Every pair (i before j)
pairs = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        pairs += 1
print("number of pairs:", pairs)            # 10

# The short way to build a list
print([n * 10 for n in nums])               # [30, 80, 50, 90, 20]
print([n for n in nums if n > 4])           # [8, 5, 9]

# Try changing things:
#   1. Count how many letters in "banana" are "a" (pattern 3, loop over a string).
#   2. Change pattern 4 to find the smallest number instead.
#   3. Count the steps to halve 100 down to 0 with a while loop.
