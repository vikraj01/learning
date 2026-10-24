# Page 3: If and else
# Run me with:  python3 03-if-else.py

# A comparison is a question. The answer is True or False.
print(5 > 3)      # True
print(5 == 3)     # False  ( == asks "are these equal?")
print(5 != 3)     # True   ( != asks "are these different?")

# and / or / not
age = 20
print(age >= 18 and age < 60)   # True: both are true
print(age < 10 or age > 60)     # False: neither is true
print(not age > 18)             # False: flips True to False

# if / elif / else: Python checks from the top and runs the first match.
marks = 72

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Try again")

# Even or odd
number = 7

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# Indented lines belong to the if. The last line is not indented,
# so it runs every time, whatever the if decided.
print("Done")

# Try changing things:
#   1. Set marks to 95, then 50, then 10. Predict each grade first.
#   2. Set number to 0. Is 0 even?
#   3. Remove the 4 spaces before one print, run it, and read the error.
