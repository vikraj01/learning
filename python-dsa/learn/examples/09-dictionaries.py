# Page 9: Dictionaries
# Run me with:  python3 09-dictionaries.py

# key: value pairs, in curly brackets
contacts = {"Mum": "98100 11111", "Vikash": "98200 22222"}

print(contacts["Mum"])                    # 98100 11111  (look up by key)
print(contacts.get("Riya", "not saved"))  # not saved    (safe: no KeyError)

contacts["Riya"] = "98300 33333"          # new key: added
contacts["Mum"] = "98100 99999"           # old key: updated
print(len(contacts))                      # 3
print("Riya" in contacts)                 # True  (in checks keys)

for name, number in contacts.items():     # key and value together
    print(name, "->", number)

# Counting pattern
word = "mississippi"
counts = {}
for ch in word:
    counts[ch] = counts.get(ch, 0) + 1
print(counts)                  # {'m': 1, 'i': 4, 's': 4, 'p': 2}
print(max(counts.values()))    # 4  (the biggest count)

# Which letters appear more than once?
for ch, how_many in counts.items():
    if how_many > 1:
        print(ch, "appears", how_many, "times")

# A dictionary as a lookup table
price = {"tea": 10, "coffee": 30, "samosa": 15}
order = ["tea", "samosa", "samosa"]
total = 0
for item in order:
    total += price[item]
print("bill:", total)          # 40

# "Seen before, and where?" pattern: value -> index
nums = [5, 3, 8, 3, 1]
seen = {}
for i, n in enumerate(nums):
    if n in seen:              # check first...
        print(n, "first seen at", seen[n], "and again at", i)
        break
    seen[n] = i                # ...then remember

# The shortcut
from collections import Counter
print(Counter(word))           # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# Try changing things:
#   1. Count the letters in your own name.
#   2. Add "chai": 12 to price and put it in the order.
#   3. Change nums so no number repeats. What does the seen-before loop print now?
