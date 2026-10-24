# If and else

After this page you'll be able to make your program choose what to do, with `if`, `elif` and `else`.

## Choices you already make

"If it's raining, take an umbrella. Otherwise, take sunglasses."

You ask a yes-or-no question (is it raining?), and the answer decides what you do next. Programs work the same way. They ask a question, get `True` or `False`, and pick a path.

## Questions with True or False answers

On page 2 you met the **bool** type: `True` or `False`. A **comparison** is a question whose answer is a bool:

```python
print(5 > 3)
print(5 < 3)
```

```
True
False
```

All the comparisons:

| Write | Means | Example | Answer |
| --- | --- | --- | --- |
| `==` | is equal to | `4 == 4` | `True` |
| `!=` | is not equal to | `4 != 4` | `False` |
| `<` | is less than | `2 < 5` | `True` |
| `>` | is more than | `2 > 5` | `False` |
| `<=` | is less than or equal to | `3 <= 3` | `True` |
| `>=` | is more than or equal to | `2 >= 5` | `False` |

They work on text too. Capitals count, so `"cat" == "Cat"` is `False`.

### `=` and `==` are different

This is the one to be careful with.

- **`=`** puts a value in a box: `age = 20` ("age gets 20").
- **`==`** asks a question: `age == 20` ("is age equal to 20?"). The answer is `True` or `False`.

```python
age = 20
print(age == 20)
print(age == 18)
```

```
True
False
```

## Joining questions: `and`, `or`, `not`

- **`and`**: `True` only if **both** sides are true. "Over 18 and under 60."
- **`or`**: `True` if **at least one** side is true. "Weekend or holiday."
- **`not`**: flips the answer. `not True` is `False`.

```python
age = 20
print(age >= 18 and age < 60)
print(age < 10 or age > 60)
print(not age > 18)
```

```
True
False
False
```

## `if`: do this only when it's true

```python
age = 20

if age >= 18:
    print("You can vote")

print("Done")
```

```
You can vote
Done
```

Look closely at the shape:

```
if age >= 18:               <- the question, then a colon
    print("You can vote")   <- 4 spaces in: runs only if the answer is True
print("Done")               <- back at the left edge: runs every time
```

- The line starts with **`if`**, then the question, then a **colon** `:`.
- The lines underneath are pushed in by 4 spaces. This is called **indentation**. Indented lines belong to the `if`, and run only when the answer is `True`.
- The first line back at the left edge is outside the `if`. It always runs.

Change `age` to `15` and run it. You'll only see `Done`.

## `else`: otherwise, do this

```python
number = 7

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
```

```
7 is odd
```

This is the even/odd check from page 2, now making a choice. `number % 2` is `1`, so `1 == 0` is `False`, so Python skips the `if` part and runs the `else` part. Exactly one of the two always runs.

## `elif`: more than two paths

**`elif`** is short for "else if". Use it when there are more than two choices:

```python
marks = 72

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Try again")
```

```
Grade B
```

Python checks from the top, one by one:

```
marks = 72

marks >= 90 ?   False  -> skip
marks >= 70 ?   True   -> print "Grade B", then skip everything below
marks >= 50 ?   (never checked)
else            (never reached)
```

Only the **first** true one runs. That's why the order matters: `72` is also `>= 50`, but Python stopped at `>= 70`.

## Try it

From the `learn` folder, run `examples/03-if-else.py`:

```bash
python3 examples/03-if-else.py
```

```
True
False
True
True
False
False
Grade B
7 is odd
Done
```

Then set `marks` to `95`, then `50`, then `10`, and `number` to `0`. Predict each answer before you run it.

## Common mistakes

**Forgetting to indent.**

```python
age = 20
if age >= 18:
print("adult")
```

```
IndentationError: expected an indented block after 'if' statement on line 2
```

An **IndentationError** means the spaces at the start of a line are wrong. Here Python saw an `if` and expected the next line to be pushed in. Add 4 spaces before `print`.

Too many spaces is also an error. A line indented when nothing asked for it gives `IndentationError: unexpected indent`. In Python, spaces at the start of a line have meaning. Most editors add 4 spaces when you press Tab.

**Using `=` instead of `==`.**

```python
if age = 18:
```

```
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

Python noticed you used "put in a box" where a question belongs. Use `==`. (Ignore the `:=` it mentions; you won't need it.)

**Forgetting the colon.** `if age >= 18` with no `:` at the end gives `SyntaxError: expected ':'`.

## Check yourself

1. What's the difference between `x = 5` and `x == 5`?
2. With `marks = 95`, which grade prints? Why doesn't `Grade B` also print?
3. What does `10 > 3 and 2 > 5` give?

## Next

Next you'll package steps into your own reusable recipes: [Functions](04-functions.md).
