# Page 10: Sets and tuples
# Run me with:  python3 10-sets-and-tuples.py

# --- Sets: no repeats, no order, fast "in" ---

nums = [3, 1, 3, 2, 1, 3]
unique = set(nums)
print(unique)                    # {1, 2, 3}
print(len(nums), len(unique))    # 6 3
print(len(unique) < len(nums))   # True: something was repeated

guests = set()                   # empty set (NOT {}, that's a dict)
guests.add("Tanvi")
guests.add("Riya")
guests.add("Tanvi")              # already there: nothing changes
print(len(guests))               # 2
print("Riya" in guests)          # True
guests.remove("Riya")
print("Riya" in guests)          # False

# "Have I seen this before?" with a set
seen = set()
for n in [4, 7, 2, 7, 9]:
    if n in seen:
        print("repeat:", n)      # repeat: 7
        break
    seen.add(n)

# Different letters in a word
print(len(set("hello")))         # 4   (h, e, l, o)

# Comparing two sets
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a & b)                     # {3, 4}           in both
print(a | b)                     # {1, 2, 3, 4, 5}  in either
print(a - b)                     # {1, 2}           in a, not in b
print(list(a & b))               # [3, 4]           back to a list

# --- Tuples: fixed groups that can't change ---

point = (3, 4)
print(point[0])                  # 3
x, y = point                     # unpacking
print(x, y)                      # 3 4

# Swap two values
left = "L"
right = "R"
left, right = right, left
print(left, right)               # R L

# Swap two items in a list
letters = ["a", "b", "c"]
letters[0], letters[2] = letters[2], letters[0]
print(letters)                   # ['c', 'b', 'a']


# Return two values at once
def smallest_and_biggest(nums):
    return min(nums), max(nums)

low, high = smallest_and_biggest([4, 9, 1, 7])
print(low, high)                 # 1 9

# Try changing things:
#   1. How many different letters are in your full name? Use set and len.
#   2. Make a set of your friends and a set of Vikash's friends. Who's in both?
#   3. Write a function that returns a number's last digit AND the rest
#      (% 10 and // 10), then unpack both answers.
