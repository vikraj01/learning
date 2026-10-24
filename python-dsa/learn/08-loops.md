# Loops

After this page you'll be able to repeat work with `for` and `while`, and you'll know the four loop patterns that solve most easy LeetCode problems.

This is the most important page so far. Take it slowly, one section at a time, and run every example.

## A playlist, one song at a time

A music app plays a playlist like this: take the first song, play it. Take the next song, play it. Keep going until there are no songs left.

A **loop** is the same idea in code: "for each thing in this group, do this". You write the work once, and Python repeats it for every item.

## `for`: do something for each item

```python
songs = ["Kesariya", "Tum Hi Ho", "Ilahi"]
for song in songs:
    print("Now playing:", song)
print("Playlist over")
```

You'll see:

```
Now playing: Kesariya
Now playing: Tum Hi Ho
Now playing: Ilahi
Playlist over
```

How to read it:

1. `for song in songs:` means "take each item of `songs`, one at a time, and call it `song`".
2. The indented lines under it are the **body** of the loop. They run once per item, like the body of an `if`.
3. The first time round, `song` is `"Kesariya"`. The second time, `"Tum Hi Ho"`. Then `"Ilahi"`.
4. When there are no items left, the loop ends and Python carries on with the first line that isn't indented.

Each time round the loop is called an **iteration**. You can pick any name instead of `song`. Pick one that says what the item is.

## Looping over a string

A string is a row of letters, so a `for` loop walks through it letter by letter:

```python
for letter in "cat":
    print(letter)
```

```
c
a
t
```

## `range`: counting numbers

Sometimes you don't have a list; you want the numbers 0, 1, 2, ... **`range`** makes them.

```python
print(list(range(5)))
print(list(range(2, 6)))
print(list(range(0, 10, 2)))
print(list(range(4, -1, -1)))
```

```
[0, 1, 2, 3, 4]
[2, 3, 4, 5]
[0, 2, 4, 6, 8]
[4, 3, 2, 1, 0]
```

(`list(...)` turns the range into a list, only so you can see the numbers. In a loop you don't need it.)

- **`range(n)`**: 0 up to n, but **not** n. So `range(5)` is five numbers, 0 to 4.
- **`range(a, b)`**: from a up to, but not including, b. Same rule as slicing.
- **`range(a, b, step)`**: jump by `step` each time. A negative step counts down. `range(4, -1, -1)` counts 4, 3, 2, 1, 0 (it stops before -1).

In a loop:

```python
for i in range(3):
    print("Hello", i)
```

```
Hello 0
Hello 1
Hello 2
```

`i` is the usual name for a counting number like this (short for "index").

## Index and item: `range(len(nums))` and `enumerate`

Looping with `for n in nums` gives you each **item**, but not its position. Sometimes you need the position too: to change `nums[i]`, to look at the next item `nums[i + 1]`, or to return where something was.

`range(len(nums))` gives you every index of the list:

```python
nums = [10, 20, 30]
for i in range(len(nums)):
    print(i, nums[i])
```

```
0 10
1 20
2 30
```

`len(nums)` is 3, so `range(3)` gives 0, 1, 2: exactly the indexes.

**`enumerate`** does the same job more neatly. It hands you two things each time round, the index and the item, and you give each one a name:

```python
nums = [10, 20, 30]
for i, n in enumerate(nums):
    print(i, n)
```

```
0 10
1 20
2 30
```

Use whichever reads more clearly to you.

## The four loop patterns

Almost every easy LeetCode problem is one of these four shapes, or two of them together. Learn the shapes and you'll recognise them everywhere.

Each one has the same three parts: **set up** a variable before the loop, **update** it inside the loop, **use** it after the loop.

### 1. Build a result list

Start with an empty list, `append` to it each time round.

```python
nums = [1, 2, 3, 4]
doubled = []
for n in nums:
    doubled.append(n * 2)
print(doubled)
```

```
[2, 4, 6, 8]
```

The same works for building a string: start with `""` and add to it.

```python
word = "hello"
shout = ""
for ch in word:
    shout += ch.upper()
print(shout)
```

```
HELLO
```

### 2. Running total

Start at 0, add each item.

```python
nums = [3, 1, 4, 1, 5]
total = 0
for n in nums:
    total += n
    print("added", n, "-> total is", total)
print(total)
```

```
added 3 -> total is 3
added 1 -> total is 4
added 4 -> total is 8
added 1 -> total is 9
added 5 -> total is 14
14
```

(`total += n` is short for `total = total + n`, from page 2.) `sum(nums)` gives the same answer, but this pattern lets you see the total *at each step*, and that's what some problems want.

### 3. Counter

Start at 0, add 1 each time something is true.

```python
nums = [3, 8, 5, 6, 2]
count = 0
for n in nums:
    if n % 2 == 0:
        count += 1
print(count)
```

```
3
```

Three even numbers: 8, 6 and 2.

### 4. Best so far

Start with the first item as the "best", and replace it whenever you meet something better.

```python
nums = [3, 8, 5, 9, 2]
best = nums[0]
for n in nums:
    if n > best:
        best = n
print(best)
```

```
9
```

```
 n:      3    8    5    9    2
 best:   3    8    8    9    9     <- best after looking at n
```

`max(nums)` does this for you. You still need the pattern, because problems often want the best of something you work out as you go, not the best item in the list. "Best" can also mean smallest: flip `>` to `<`.

## `while`: repeat as long as something is true

A `for` loop goes through a group of things. A **`while`** loop keeps going **as long as** a condition is `True`. Like stirring tea *while* the sugar hasn't dissolved: you don't know in advance how many stirs.

Halve a number until it reaches zero, and count the steps:

```python
n = 20
steps = 0
while n > 0:
    n = n // 2
    steps += 1
    print("n is now", n)
print("steps:", steps)
```

```
n is now 10
n is now 5
n is now 2
n is now 1
n is now 0
steps: 5
```

Python checks `n > 0` before each iteration. When `n` reaches 0, the check is `False` and the loop stops.

### Taking a number apart, digit by digit

From page 2: `% 10` gives the last digit, and `// 10` removes it. Put those in a `while` loop and you get every digit:

```python
n = 472
while n > 0:
    digit = n % 10
    print("digit:", digit)
    n = n // 10
```

```
digit: 2
digit: 7
digit: 4
```

```
 n      n % 10   n // 10
 472    2        47
 47     7        4
 4      4        0      <- n is 0, loop stops
```

The digits come out from the back. You'll use this whenever a problem talks about "the digits of a number".

**Careful:** if the condition never becomes `False`, the loop runs forever. If your program seems stuck, press **Ctrl+C** to stop it, then check that something inside the loop moves you towards the end (here, `n = n // 2`).

## `break` and `continue`

- **`break`** stops the loop straight away.
- **`continue`** skips the rest of this iteration and moves on to the next item.

```python
nums = [4, 7, 9, -2, 5]
for n in nums:
    if n < 0:
        print("Found a negative:", n)
        break
    print("checked", n)
```

```
checked 4
checked 7
checked 9
Found a negative: -2
```

The `5` is never checked. Once you've found what you were looking for, there's no need to keep going.

```python
for n in [1, 2, 3, 4, 5]:
    if n % 2 == 0:
        continue
    print(n)
```

```
1
3
5
```

For even numbers, `continue` jumps back to the top before the `print`.

## A loop inside a loop: every pair

Some problems need every **pair** of items: item 0 with item 1, item 0 with item 2, and so on. Put one loop inside another. Start the inner loop one step after the outer one, so `j` is always bigger than `i`:

```python
nums = [5, 6, 7]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        print(i, j, "->", nums[i], nums[j])
```

```
0 1 -> 5 6
0 2 -> 5 7
1 2 -> 6 7
```

Starting `j` at `i + 1` means you never pair an item with itself, and never count the same pair twice (0 with 1, and then 1 with 0).

## A shorter way: list comprehensions

Pattern 1 (build a result list) is so common that Python has a one-line way to write it, called a **list comprehension**:

```python
nums = [1, 2, 3, 4]
print([n * 2 for n in nums])
print([n for n in nums if n % 2 == 0])
```

```
[2, 4, 6, 8]
[2, 4]
```

Read the first one as "`n * 2`, for each `n` in `nums`". The second keeps only the items where the `if` is true.

You'll see these in other people's solutions. Write the long way until it feels easy; then try the short way.

## Try it

Run `examples/08-loops.py`:

```bash
python3 examples/08-loops.py
```

It has all four patterns, `while`, `break` and pairs. Change the lists and predict the output before you run it.

## Common mistakes

**Forgetting to indent the body.**

```python
for n in [1, 2]:
print(n)
```

```
IndentationError: expected an indented block after 'for' statement on line 1
```

The lines that belong to the loop must be indented (4 spaces), like under an `if`.

**Using the item as if it were an index.**

```python
nums = [10, 20, 30]
for n in nums:
    print(nums[n])
```

```
IndexError: list index out of range
```

`n` is the item (10, 20, 30), not the position. `nums[10]` doesn't exist. Either print `n`, or loop with `range(len(nums))` if you need positions.

**Looking one step too far.** With `for i in range(len(nums))`, the last `i` is the last index. So `nums[i + 1]` goes past the end on the last iteration, and you get the same `IndexError`. If you need `nums[i + 1]`, loop with `range(len(nums) - 1)`.

## Check yourself

1. Which numbers does `range(1, 10, 3)` give?
2. Write the four lines that count how many letters in `"banana"` are `"a"`. Which pattern is it?
3. What does this print, and why does it stop?

    ```python
    n = 1
    while n < 20:
        n = n * 3
    print(n)
    ```

## Next

This is the biggest practice stage, and where most of your learning happens: **Stage 4** in the LeetCode list (`leetcode-list.pdf`).
