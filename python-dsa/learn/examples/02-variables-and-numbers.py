# Page 2: Variables and numbers
# Run me with:  python3 02-variables-and-numbers.py

# A variable is a labelled box. The = puts a value in the box.
age = 20
price = 49.5
name = "Tanvi"
is_raining = False

print(age, price, name, is_raining)

# type() tells you what kind of value is in the box.
print(type(age))         # int: a whole number
print(type(price))       # float: a number with a decimal point
print(type(name))        # str: text
print(type(is_raining))  # bool: True or False

# The maths operators
print(7 + 2)    # 9
print(7 - 2)    # 5
print(7 * 2)    # 14
print(7 / 2)    # 3.5   ( / always gives a float)
print(7 // 2)   # 3     ( // whole times it fits, drops the rest)
print(7 % 2)    # 1     ( % what's left over)
print(7 ** 2)   # 49    ( ** to the power of)

# Minutes to hours and minutes
minutes = 135
print(minutes // 60, "hours and", minutes % 60, "minutes")

# Even or odd: an even number has nothing left over when split by 2
print(14 % 2)   # 0, so 14 is even
print(7 % 2)    # 1, so 7 is odd

# The last digit, and the number without its last digit
number = 1234
print(number % 10)    # 4
print(number // 10)   # 123

# Updating a box
score = 10
score = score + 1
print(score)    # 11
score += 5
print(score)    # 16

# Rounding
print(round(7 / 3, 2))   # 2.33

# Try changing things:
#   1. Set minutes to 200. What do you expect before you run it?
#   2. Set number to 9876. What are the last digit and the rest?
#   3. Is 1001 even or odd? Check with % 2.
