# Variables and numbers

After this page you'll be able to store values under a name and do maths with them, including the two operators LeetCode loves: `//` and `%`.

## A labelled box

Think of a box with a label stuck on it. The label says `age`, and inside the box is `20`. Later you can ask "what's in the `age` box?" and get `20` back. You can also take the old thing out and put something new in.

In Python, that box is called a **variable**. You make one with `=`:

```python
age = 20
print(age)
```

```
20
```

- `age` is the **name** (the label).
- `20` is the **value** (what's inside).
- `=` means "put this value into this box". It is not "equals" like in maths. Read `age = 20` as "age gets 20".

Names can use letters, numbers and `_`, but can't start with a number and can't have spaces. `my_age` is fine. `my age` and `2age` are not.

## Kinds of values

Values come in different kinds. Python calls the kind of a value its **type**. Four you'll use all the time:

```python
age = 20             # int: a whole number
price = 49.5         # float: a number with a decimal point
name = "Tanvi"       # str: text, always inside quotes
is_raining = False   # bool: True or False, nothing else
```

- **int** (short for integer) is a whole number: `20`, `0`, `-7`.
- **float** is a number with a decimal point: `49.5`, `3.0`.
- **str** (short for string) is text: `"Tanvi"`, `"hello"`. You'll learn much more about strings on page 6.
- **bool** (short for boolean) is either `True` or `False`. Capital T and F. You'll use these a lot on the next page.

`type()` tells you which kind a value is:

```python
print(type(age))
print(type(price))
print(type(name))
print(type(is_raining))
```

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

## Maths

```python
print(7 + 2)    # add
print(7 - 2)    # subtract
print(7 * 2)    # multiply
print(7 / 2)    # divide
print(7 // 2)   # divide, keep only the whole part
print(7 % 2)    # remainder: what's left over
print(7 ** 2)   # power: 7 times 7
```

```
9
5
14
3.5
3
1
49
```

Brackets work like in school maths: `(2 + 3) * 4` is `20`, while `2 + 3 * 4` is `14`.

### `/` always gives a float

```python
print(10 / 2)
```

```
5.0
```

Even when it divides evenly, `/` gives `5.0`, not `5`. That `.0` matters on LeetCode: if a problem wants a whole number back, use `//`, not `/`.

### `//` and `%`: sharing sweets

You have 7 sweets and 2 friends. Each friend gets 3 (that's `7 // 2`), and 1 sweet is left over (that's `7 % 2`).

```
  7 sweets, 2 friends

  friend 1:  ● ● ●
  friend 2:  ● ● ●
  left over: ●

  7 // 2  ->  3   (how many each)
  7 %  2  ->  1   (how many left)
```

- **`//`** is **floor division**: how many whole times it fits.
- **`%`** is **modulo** (say "mod"): what's left over.

They show up everywhere. Some everyday uses:

**Minutes into hours and minutes.** A film is 135 minutes long:

```python
minutes = 135
print(minutes // 60, "hours and", minutes % 60, "minutes")
```

```
2 hours and 15 minutes
```

**Even or odd.** An even number splits into 2 with nothing left over:

```python
print(14 % 2)
print(7 % 2)
```

```
0
1
```

`% 2` gives `0` for even numbers and `1` for odd ones. Remember this; it's on the next page.

**The last digit of a number.** Splitting by 10, the leftover is the last digit. And `// 10` drops the last digit:

```python
number = 1234
print(number % 10)
print(number // 10)
```

```
4
123
```

```
   1 2 3 | 4
   ─────   ─
     │     └── 1234 %  10  ->  4     (the last digit)
     └──────── 1234 // 10  ->  123   (everything except the last digit)
```

You'll use this pair to take numbers apart, digit by digit, later on.

## Updating a box

You can put a new value in a box. Python works out the right side first, then puts the answer in the box:

```python
score = 10
score = score + 1
print(score)
```

```
11
```

`score = score + 1` reads as "take what's in score, add 1, put it back in score". Because this is so common, there's a short way to write it:

```python
score += 5     # same as  score = score + 5
print(score)
```

```
16
```

`-=`, `*=` and `//=` work the same way.

## Rounding

`round(value, places)` rounds a float to that many places after the decimal point:

```python
print(7 / 3)
print(round(7 / 3, 2))
```

```
2.3333333333333335
2.33
```

Without the second number, `round` gives a whole number: `round(7 / 3)` is `2`.

## Try it

From the `learn` folder, run `examples/02-variables-and-numbers.py`:

```bash
python3 examples/02-variables-and-numbers.py
```

```
20 49.5 Tanvi False
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
9
5
14
3.5
3
1
49
2 hours and 15 minutes
0
1
4
123
11
16
2.33
```

Then change things in it. Set `minutes` to `200` and `number` to `9876`. Guess the output before you run it.

## Common mistakes

**Adding text and a number.**

```python
print("5" + 3)
```

```
TypeError: can only concatenate str (not "int") to str
```

A **TypeError** means the kinds don't fit together. `"5"` is text (it has quotes), `3` is a number, and Python won't add text to a number. Remove the quotes: `5 + 3` is `8`.

**Dividing by zero.**

```python
print(10 / 0)
```

```
ZeroDivisionError: division by zero
```

Same as in maths: you can't split something into zero groups. You get a `ZeroDivisionError` with `//` and `%` by zero too.

**Using a box before making it.** `print(total)` before any `total = ...` line gives `NameError: name 'total' is not defined`, the same error as a typo on page 1.

## Check yourself

1. What do `17 // 5` and `17 % 5` give?
2. How can you tell if a number is even, using `%`?
3. What does `10 / 5` print, and why isn't it `2`?

## Next

Next your programs will make choices: [If and else](03-if-else.md).
