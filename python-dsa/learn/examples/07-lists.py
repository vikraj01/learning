# Page 7: Lists
# Run me with:  python3 07-lists.py

nums = [4, 8, 15, 16, 23]

# Reading: same as strings
print(nums[0])        # 4
print(nums[-1])       # 23
print(len(nums))      # 5
print(nums[1:3])      # [8, 15]

# Changing a box (strings can't do this, lists can)
nums[0] = 99
print(nums)           # [99, 8, 15, 16, 23]

# Adding and taking away
nums.append(42)       # add at the end
print(nums)           # [99, 8, 15, 16, 23, 42]
top = nums.pop()      # take the last one off
print(top, nums)      # 42 [99, 8, 15, 16, 23]
nums.insert(1, 7)     # put 7 at index 1
print(nums)           # [99, 7, 8, 15, 16, 23]
print(15 in nums)     # True

# + joins lists, * repeats them
print([1, 2] + [3])   # [1, 2, 3]
print([0] * 4)        # [0, 0, 0, 0]

# sort() changes the list. sorted() gives a new one.
marks = [70, 45, 90, 60]
print(sorted(marks))  # [45, 60, 70, 90]
print(marks)          # [70, 45, 90, 60]  (unchanged)
marks.sort()
print(marks)          # [45, 60, 70, 90]  (changed)
print(marks.sort())   # None  (sort gives nothing back)

# Quick answers
print(sum(marks), max(marks), min(marks))   # 265 90 45

# The two biggest are at the end after sorting
print(marks[-1], marks[-2])                 # 90 70

# Lists inside lists
accounts = [[1, 2, 3], [3, 2, 1], [5, 5, 5]]
print(accounts[1][2])     # 1   (box 1, then box 2 inside it)
print(sum(accounts[2]))   # 15


# A function that changes a list changes it for the caller too
def add_zero(nums):
    nums.append(0)

my_list = [1, 2, 3]
add_zero(my_list)
print(my_list)            # [1, 2, 3, 0]

# Try changing things:
#   1. Make a list of your three favourite foods. Add a fourth with append.
#   2. Make the list [1, 2, 3] twice in a row: [1, 2, 3, 1, 2, 3]. Two ways!
#   3. Write  marks = marks.sort()  then  print(marks). What do you get, and why?
