# Functions

After this page you'll be able to write a function that takes inputs and returns an answer, and you'll know why `return` is not the same as `print`.

## A recipe card

Think of a recipe card for chai. It has a name ("Chai"), a list of what you need to bring (tea leaves, milk, sugar), and steps. Once the card is written, anyone can say "make chai" with whatever milk and sugar they have, and get a cup of chai back.

A **function** is a recipe card in Python. You write the steps once, give them a name, and then use them as often as you like with different inputs. Every LeetCode answer you write will be a function.

## Writing one: `def`

```python
def add(a, b):
    return a + b
```

Read it piece by piece:

```
def add(a, b):        <- def = "define a function". Its name is add.
    return a + b      <- the step: work out a + b and hand it back
```

- **`def`** means "I'm writing a new function".
- **`add`** is its name. Same naming rules as variables.
- **`a` and `b`** are its **parameters**: the empty boxes for the inputs. They get filled in each time the function is used.
- The **colon** and the **indented** lines work like `if` on page 3. Indented lines are the function's steps.
- **`return`** hands an answer back to whoever asked.

Running this file does nothing visible. Writing a recipe card doesn't make any chai. You have to use it.

## Using one: calling

Using a function is called **calling** it. Write its name with the inputs in brackets:

```python
def add(a, b):
    return a + b

total = add(2, 3)
print(total)
print(add(10, 20))
```

```
5
30
```

When Python reaches `add(2, 3)`:

```
add(2, 3)
     │  │
     ▼  ▼
def add(a, b):        a = 2, b = 3
    return a + b      2 + 3 = 5, hand 5 back
     │
     ▼
total = 5             add(2, 3) is replaced by the 5 it returned
```

The values you pass in (`2` and `3`) are called **arguments**. They fill the parameters in order: first one into `a`, second into `b`.

You've been calling functions since page 1: `print(...)`, `type(...)` and `round(...)` are all functions that come with Python.

## `print` and `return` are different

This is the most important part of the page. It trips up almost every beginner, and on LeetCode it's the difference between a right answer and a wrong one.

- **`print`** shows something on the screen, for a person to read. The program can't use it afterwards.
- **`return`** hands a value back to the code that called the function. The program can store it, do maths with it, or check it.

Think of asking a friend to add up a bill. If they **shout** the total across the room (print), you heard it, but you have nothing in your hand. If they **write it on a slip and give it to you** (return), you can keep it, add a tip to it, or pass it on.

Here are two functions that look almost the same:

```python
def add_and_print(a, b):
    print(a + b)

def add_and_return(a, b):
    return a + b

x = add_and_print(2, 3)
y = add_and_return(2, 3)
print("x is", x)
print("y is", y)
```

```
5
x is None
y is 5
```

What happened, line by line:

1. `x = add_and_print(2, 3)` ran the function. It printed `5` on the screen. Then it ended without returning anything. So `x` got **`None`**.
2. `y = add_and_return(2, 3)` ran the function. It printed nothing. It returned `5`, so `y` got `5`.
3. The last two lines show what's in each box.

**`None`** is Python's word for "nothing". A function with no `return` line gives back `None`.

Now try to use the answers:

```python
print(add_and_return(2, 3) * 10)
```

```
50
```

```python
print(add_and_print(2, 3) * 10)
```

```
5
Traceback (most recent call last):
  ...
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
```

The second one printed `5` (from inside the function), then crashed. It got `None` back, and `None * 10` makes no sense. The `5` on the screen looked like an answer, but the program never got it.

**Why this matters for LeetCode.** LeetCode doesn't read your screen. It calls your function and checks what it **returns**. If you `print` the right answer and don't `return` it, LeetCode gets `None` and marks you wrong. So:

- Use **`return`** for the answer.
- Use `print` only to look at things while you're working something out.

## `return` ends the function

As soon as Python reaches a `return`, it hands the value back and leaves the function. Lines after it don't run:

```python
def say_hi():
    return "hi"
    print("you'll never see this")

print(say_hi())
```

```
hi
```

This is useful with `if`.

## Returning True or False

A function can return a bool. Here's the even/odd check from pages 2 and 3 as a function:

```python
def is_even(n):
    if n % 2 == 0:
        return True
    return False

print(is_even(4))
print(is_even(7))
```

```
True
False
```

- For `4`: `4 % 2 == 0` is `True`, so it returns `True` and leaves. The last line never runs.
- For `7`: the `if` is `False`, so Python skips it and reaches `return False`.

You don't need an `else` here, because `return` already left the function. Many LeetCode problems ask "return true if ...", and they look exactly like this.

## One function calling another

A function can use another function, the way a recipe for chai biscuits might say "first make chai (see the chai card)":

```python
def is_even(n):
    if n % 2 == 0:
        return True
    return False

def is_odd(n):
    return not is_even(n)

print(is_odd(7))
```

```
True
```

`is_odd(7)` calls `is_even(7)`, which returns `False`, and `not False` is `True`.

## Try it

From the `learn` folder, run `examples/04-functions.py`:

```bash
python3 examples/04-functions.py
```

```
5
30
50
5
x is None
y is 5
True
False
True
2 15
```

Then open it and:

1. Write a function `square(n)` that returns `n * n`. Print `square(9)`.
2. Change `add_and_return` to use `print` instead of `return`. What does `y is` show now?
3. Write `is_positive(n)` that returns `True` when `n` is more than `0`.

## Common mistakes

**Printing instead of returning.** No error message, which makes it sneaky. The answer appears on screen, but the function gives back `None`. If you ever see `None` where you expected a value, look for a missing `return`.

**Giving the wrong number of inputs.**

```python
def add(a, b):
    return a + b

print(add(2))
```

```
TypeError: add() missing 1 required positional argument: 'b'
```

`add` has two parameters, `a` and `b`, but got only one value. `2` went into `a`, and `b` had nothing. Pass one value for each parameter: `add(2, 3)`.

**Calling a function before the `def` line.** Python reads top to bottom, so the `def` must come first. Otherwise you'll get a `NameError`, like a typo.

## Check yourself

1. A function has `print(a * b)` but no `return`. What does it give back?
2. Why does LeetCode need `return` and not `print`?
3. In `is_even`, why is there no `else` before `return False`?

## Next

You now know enough Python for your first LeetCode problems. Next, see what a LeetCode problem looks like and solve one: [How a LeetCode problem looks](05-how-leetcode-looks.md).
