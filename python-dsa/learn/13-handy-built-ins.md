# Handy built-ins

After this page you'll know a set of small Python tools that turn up again and again in LeetCode answers: letter maths, infinity, sorting by your own rule, and a few more.

## The kitchen drawer

Every kitchen has a drawer of small tools: a peeler, a bottle opener, a grater. None of them is a big idea. Each does one small job, and when you need it, it saves you ten minutes.

This page is that drawer. Python comes with many small **built-in** tools (ready to use, nothing to install). You don't need to memorise them all today. Read the page once, run the example, and come back when a problem needs one of them.

## Letters are numbers underneath: `ord` and `chr`

Inside the computer, every character is stored as a number. **`ord`** gives you a character's number. **`chr`** goes the other way, from a number to its character.

```python
print(ord("a"))
print(ord("b"))
print(ord("z"))
print(chr(99))
```

You'll see:

```
97
98
122
c
```

The small letters `a` to `z` are numbered **in a row**, 97 to 122. You never need to remember 97. What matters is the trick below.

### Letter maths: position in the alphabet

Subtract `ord("a")`, and every small letter becomes its place in the alphabet, starting at 0:

```python
for ch in "abz":
    print(ch, ord(ch) - ord("a"))
```

```
a 0
b 1
z 25
```

```
 letter:   a    b    c    d   ...   y    z
 ord:      97   98   99   100 ...   121  122
 - ord(a): 0    1    2    3   ...   24   25
```

### Counting letters with a list of 26

On page 9 you counted letters with a dictionary. When a problem says "the string has only small English letters", a list of 26 zeros works too: box 0 for `a`, box 1 for `b`, and so on.

```python
counts = [0] * 26
for ch in "banana":
    counts[ord(ch) - ord("a")] += 1
print(counts)
for i in range(26):
    if counts[i] > 0:
        print(chr(ord("a") + i), counts[i])
```

```
[3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a 3
b 1
n 2
```

`ord(ch) - ord("a")` picks the box. To go back from a box number `i` to its letter, add `ord("a")` and use `chr`.

### Moving along the alphabet

```python
print(chr(ord("a") + 2))
ch = "y"
shifted = chr((ord(ch) - ord("a") + 3) % 26 + ord("a"))
print(shifted)
```

```
c
b
```

Two steps after `a` is `c`. For `y` moved 3 places, the `% 26` (page 2) wraps around past `z` back to the start: y, z, a, **b**.

## Numbers

### Infinity: a start value for "smallest so far"

On page 8 you found the best item by starting with `best = nums[0]`. Sometimes there's no good first item to start with: the list might be empty, or you're finding the best of something you work out along the way.

**`float("inf")`** is **infinity**: a number bigger than every other number. `-float("inf")` is smaller than every other number.

```python
print(float("inf"))
print(float("inf") > 10 ** 100)
print(-float("inf") < -10 ** 100)
```

```
inf
True
True
```

(`10 ** 100` is 10 to the power 100, a 1 with a hundred zeros.)

Start "smallest so far" at infinity, and the first real value always replaces it. Start "biggest so far" at minus infinity for the same reason:

```python
words = ["kiwi", "banana", "fig", "mango"]
shortest = float("inf")
longest = -float("inf")
for w in words:
    if len(w) < shortest:
        shortest = len(w)
    if len(w) > longest:
        longest = len(w)
print(shortest, longest)
```

```
3 6
```

If nothing ever replaced it (for example, the list was empty), the value is still `inf`. Check for that before returning, if the problem says something like "return -1 if there is no answer".

### `abs`: how far from zero

**`abs`** gives the **absolute value**: the number without its minus sign.

```python
print(abs(-7))
print(abs(7))
print(abs(3 - 10))
```

```
7
7
7
```

The last one is the common use: **the distance between two numbers**, whichever is bigger. 3 and 10 are 7 apart.

### `divmod`: `//` and `%` in one go

```python
print(divmod(135, 60))
hours, minutes = divmod(135, 60)
print(hours, "hours and", minutes, "minutes")
```

```
(2, 15)
2 hours and 15 minutes
```

**`divmod(a, b)`** gives the tuple `(a // b, a % b)`. Unpack it into two names (page 10).

### `//` and `%` with negative numbers

This one surprises everybody once.

```python
print(-7 / 2)
print(-7 // 2)
print(int(-7 / 2))
```

```
-3.5
-4
-3
```

`-7 / 2` is `-3.5`. Then:

- **`//` always rounds down**: towards the smaller number. Below `-3.5` on the number line is `-4`, not `-3`.
- **`int(...)`** chops off the part after the decimal point. That moves **towards zero**, so `-3.5` becomes `-3`.

```
   -4        -3.5        -3          0
  --+---------+----------+-----------+--->
    ^                    ^
    -7 // 2              int(-7 / 2)
    (round down)         (chop towards zero)
```

With positive numbers both give the same answer, so you only notice with negatives. Some LeetCode problems say "division should **truncate toward zero**". Truncate means chop. When you see that, use `int(a / b)`, not `a // b`.

`%` follows `//`, so it surprises too:

```python
print(-7 % 2)
print(-123 % 10)
print(abs(-123) % 10)
```

```
1
7
3
```

- `-7 % 2` is `1`, so the odd/even check `n % 2 == 1` still works for negative numbers in Python.
- `-123 % 10` is `7`, **not** `3`. If a problem has negative numbers and you want their digits, take `abs` first.

## Walking through lists

### `zip`: two lists side by side

You met `zip` on the grids page. It walks through two lists together, giving you one item from each:

```python
names = ["Tanvi", "Riya", "Aman"]
marks = [82, 95, 78]
for name, mark in zip(names, marks):
    print(name, mark)
```

```
Tanvi 82
Riya 95
Aman 78
```

Without `zip` you'd write `for i in range(len(names))` and then `names[i]` and `marks[i]`. `zip` saves that.

If one list is shorter, `zip` stops at the end of the shorter one:

```python
print(list(zip([1, 2, 3], [10, 20])))
```

```
[(1, 10), (2, 20)]
```

It also fits inside a list comprehension. Add two lists, box by box:

```python
a = [1, 2, 3]
b = [10, 20, 30]
print([x + y for x, y in zip(a, b)])
```

```
[11, 22, 33]
```

### `enumerate(..., start=1)`

`enumerate` counts from 0. Add `start=1` when you want to count like people do:

```python
for place, name in enumerate(["Riya", "Tanvi", "Aman"], start=1):
    print(place, name)
```

```
1 Riya
2 Tanvi
3 Aman
```

### `any` and `all`: one yes/no for a whole list

- **`any`**: is **at least one** of these `True`?
- **`all`**: are **all** of them `True`?

```python
nums = [4, -2, 7]
print(any([n < 0 for n in nums]))
print(all([n < 0 for n in nums]))
print(all([n != 0 for n in nums]))
```

```
True
False
True
```

The list comprehension makes a list of `True`/`False` (`[False, True, False]` for the first one), and `any` or `all` sums it up in one answer.

You'll often see it written without the square brackets, `any(n < 0 for n in nums)`. It gives the same answer.

## Sorting and choosing by your own rule

### `key=`: what to compare

On page 7, `sorted` put words in alphabetical order. **`key=`** lets you choose **what** to compare instead. Give it a function, and Python sorts the items by that function's answer for each one.

```python
words = ["kiwi", "banana", "fig", "mango"]
print(sorted(words))
print(sorted(words, key=len))
print(sorted(words, key=len, reverse=True))
```

```
['banana', 'fig', 'kiwi', 'mango']
['fig', 'kiwi', 'mango', 'banana']
['banana', 'mango', 'kiwi', 'fig']
```

`key=len` means "for each word, work out `len(word)`, and sort by that": 3, 4, 5, 6. Notice it's `len` with no brackets. You're handing over the tool itself, not using it.

`sort()` takes `key=` in the same way: `words.sort(key=len)` sorts the list itself.

### `lambda`: a tiny function with no name

What if no ready-made function does what you want, like "the last letter"? You could write one with `def`:

```python
def last_letter(w):
    return w[-1]

words = ["kiwi", "banana", "fig", "mango"]
print(sorted(words, key=last_letter))
print(sorted(words, key=lambda w: w[-1]))
```

```
['banana', 'fig', 'kiwi', 'mango']
['banana', 'fig', 'kiwi', 'mango']
```

The second line does the same thing in place. **`lambda`** makes a tiny function on the spot, without a name:

```
   lambda  w :  w[-1]
           │     │
           │     └── what it gives back (no "return" word needed)
           └──────── its input
```

Read `lambda w: w[-1]` as "take `w`, give back `w[-1]`". It's the same as `last_letter`, squeezed into one line. Use a lambda for a short, one-off rule; use `def` for anything longer.

### Sorting pairs by the second item

A list of (name, marks) tuples. Sort by marks:

```python
pairs = [("Tanvi", 82), ("Riya", 95), ("Aman", 82)]
print(sorted(pairs, key=lambda p: p[1]))
print(sorted(pairs, key=lambda p: p[1], reverse=True))
```

```
[('Tanvi', 82), ('Aman', 82), ('Riya', 95)]
[('Riya', 95), ('Tanvi', 82), ('Aman', 82)]
```

`p` is one pair, so `p[1]` is its marks. Tanvi and Aman both have 82; when two items tie, they keep the order they had before.

### Sorting by two things: a tuple key

"Highest marks first. If two people have the same marks, alphabetical by name." That's two rules. Tuples are compared one item at a time: the first items decide, and only if they're equal do the second items get a say.

```python
print((95, "Riya") < (82, "Aman"))
print((82, "Aman") < (82, "Tanvi"))
```

```
False
True
```

So make the key a tuple:

```python
pairs = [("Tanvi", 82), ("Riya", 95), ("Aman", 82)]
print(sorted(pairs, key=lambda p: (-p[1], p[0])))
```

```
[('Riya', 95), ('Aman', 82), ('Tanvi', 82)]
```

- `-p[1]` is minus the marks. Sorting small to big on `-95, -82, -82` puts the **biggest** marks first.
- `p[0]` is the name, small to big, so `Aman` comes before `Tanvi` when the marks tie.

You can't use `reverse=True` here, because that would flip the names too. The minus sign flips only the marks.

### `max` and `min` with `key=`

`key=` works with `max` and `min` too:

```python
words = ["kiwi", "banana", "fig", "mango"]
print(max(words, key=len))
print(min(words, key=len))
pairs = [("Tanvi", 82), ("Riya", 95), ("Aman", 82)]
print(max(pairs, key=lambda p: p[1]))
```

```
banana
fig
('Riya', 95)
```

A neat one for dictionaries: which **key** has the biggest **value**?

```python
counts = {"a": 3, "b": 1, "n": 2}
print(max(counts, key=counts.get))
```

```
a
```

Looping over a dictionary gives its keys, and `counts.get` turns each key into its value. So this is "the key whose value is biggest": the most common letter.

## Strings

### Building a string: a list, then `join`

On page 8 you built a string with `+=`. That works, but a string can't be changed (page 6), so every `+=` quietly makes a whole new string. On a long input, all that copying adds up.

The usual way: collect the pieces in a list, then glue them together once at the end with `"".join(...)`:

```python
text = "Hi, Tanvi!"
parts = []
for ch in text:
    if ch.isalpha():
        parts.append(ch.lower())
print(parts)
print("".join(parts))
```

```
['h', 'i', 't', 'a', 'n', 'v', 'i']
hitanvi
```

`append` is cheap, and `join` is done once. Use this whenever you build a string in a loop.

### `isalpha`, `isdigit`, `count`

```python
print("Tanvi".isalpha())
print("Tanvi20".isalpha())
print("2024".isdigit())
print("banana".count("a"))
print("banana".count("an"))
print([1, 2, 1, 1].count(1))
```

```
True
False
True
3
2
3
```

- **`isalpha()`**: is every character a letter? Digits, spaces and commas make it `False`. It sits next to `isdigit()` and `isalnum()` from page 6.
- **`count(x)`**: how many times does `x` appear? It works on strings (and can count a longer piece like `"an"`) and on lists.

## A few from `math`

Some tools live in the **`math`** toolbox. Import it first, like `Counter` on page 9:

```python
import math

print(math.gcd(12, 18))
print(math.sqrt(16))
print(math.sqrt(2))
print(math.ceil(7 / 2))
print(math.floor(7 / 2))
```

```
6
4.0
1.4142135623730951
4
3
```

- **`math.gcd(a, b)`**: the **greatest common divisor**, the biggest number that divides both. 6 divides 12 and 18.
- **`math.sqrt(n)`**: the **square root**. It always gives a float: `4.0`, not `4`.
- **`math.ceil`** rounds **up** to a whole number, **`math.floor`** rounds **down**. `ceil` is handy for "how many boxes do I need": 7 sweets, 2 per box, needs `math.ceil(7 / 2)`, 4 boxes.

`import math` brings in the whole toolbox, so you write `math.` in front of each tool.

## Try it

Run `examples/13-handy-built-ins.py`:

```bash
python3 examples/13-handy-built-ins.py
```

Then change the list of pairs, and sort it by name length, longest first.

## Common mistakes

**Calling the key function instead of handing it over.**

```python
words = ["kiwi", "fig"]
print(sorted(words, key=len()))
```

```
TypeError: len() takes exactly one argument (0 given)
```

`len()` with brackets tries to use `len` right now, with nothing inside. Write `key=len`, no brackets.

**Forgetting to import `math`.**

```python
print(math.sqrt(16))
```

```
NameError: name 'math' is not defined. Did you forget to import 'math'?
```

Put `import math` at the top of the file. On LeetCode too.

**`max` or `min` of an empty list.**

```python
print(max([]))
```

```
ValueError: max() iterable argument is empty
```

There's no biggest item in an empty list. If the list might be empty, check first, or use the "start at infinity" pattern.

**`ord` on more than one character.** `ord("ab")` gives `TypeError: ord() expected a character, but string of length 2 found`. `ord` takes exactly one character.

## Check yourself

1. What is `ord("d") - ord("a")`? Which box of a 26-slot count list does `"d"` go in?
2. What do `-9 // 2` and `int(-9 / 2)` give? Which one "chops towards zero"?
3. Write the `sorted` line that sorts `["bb", "a", "ccc"]` from longest to shortest.

## Next

Practise: **Stage 9** in the LeetCode list (`leetcode-list.pdf`).
