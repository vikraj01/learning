# Page 4: Functions
# Run me with:  python3 04-functions.py

# def makes a function. a and b are its parameters (the inputs).
# return hands the answer back to whoever called it.
def add(a, b):
    return a + b

# Calling the function: put real values in the brackets.
total = add(2, 3)
print(total)             # 5
print(add(10, 20))       # 30
print(add(2, 3) * 10)    # 50: the returned 5 can be used in more maths


# print versus return
def add_and_print(a, b):
    print(a + b)         # shows 5 on the screen, but gives nothing back

def add_and_return(a, b):
    return a + b         # gives 5 back, shows nothing

x = add_and_print(2, 3)  # this line prints 5
y = add_and_return(2, 3) # this line prints nothing
print("x is", x)         # x is None: nothing came back
print("y is", y)         # y is 5


# A function that returns True or False
def is_even(n):
    if n % 2 == 0:
        return True
    return False         # only reached when the if was not true

print(is_even(4))        # True
print(is_even(7))        # False


# One function can call another
def is_odd(n):
    return not is_even(n)

print(is_odd(7))         # True


# Minutes to "hours, minutes" using two small functions
def hours(minutes):
    return minutes // 60

def leftover_minutes(minutes):
    return minutes % 60

print(hours(135), leftover_minutes(135))   # 2 15

# Try changing things:
#   1. Write a function square(n) that returns n * n. Print square(9).
#   2. Change add_and_return to use print instead. What does "y is" show now?
#   3. Write is_positive(n) that returns True when n is bigger than 0.
