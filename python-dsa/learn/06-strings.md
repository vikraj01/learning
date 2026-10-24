# Strings

After this page you'll be able to pick letters out of text, cut pieces from it, and change it with Python's ready-made tools.

## A necklace of letter beads

Think of a word as a necklace of beads, one letter on each bead. The beads are in a fixed order, and you can count them: first bead, second bead, and so on.

In Python, text is called a **string** (a string of letters, like a string of beads). You've met it already: it's the `str` type, text inside quotes.

```python
word = "python"
greeting = 'hello'     # single quotes work too
```

## Index: one letter at a time

Every letter has a position number, called its **index**. Python starts counting at **0**, not 1.

```
 word = "python"

   p    y    t    h    o    n
   0    1    2    3    4    5      <- index from the front
  -6   -5   -4   -3   -2   -1      <- index from the back
```

Put the index in square brackets to get that letter:

```python
word = "python"
print(word[0])
print(word[5])
print(word[-1])
print(word[-2])
print(len(word))
```

You'll see:

```
p
n
n
o
6
```

- `word[0]` is the first letter.
- A **negative index** counts from the back: `word[-1]` is always the last letter, `word[-2]` the one before it.
- **`len()`** (short for length) tells you how many letters there are. Spaces count as letters too.

Notice: the last index is `5`, but the length is `6`. The last index is always `len(word) - 1`, because counting starts at 0.

## Slicing: cut out a piece

A **slice** is a piece of the string. You write `[start:stop]`. You get the letters from `start` up to, **but not including**, `stop`.

```python
word = "python"
print(word[0:3])
print(word[2:5])
print(word[2:])
print(word[:4])
print(word[::-1])
```

You'll see:

```
pyt
tho
thon
pyth
nohtyp
```

- `word[0:3]` gives index 0, 1, 2. Not 3.
- Leave out the start and Python starts at the beginning. Leave out the stop and it goes to the end.
- `word[::-1]` is the string **backwards**. The third number is the **step**: how far to move each time. `-1` means "walk backwards, one letter at a time". You'll use this one a lot.

## Is this piece inside? `in`

`in` asks "is this text somewhere in that text?" The answer is `True` or `False`.

```python
word = "python"
print("th" in word)
print("z" in word)
```

```
True
False
```

## Methods: tools that come with every string

A **method** is a tool that belongs to a value. You use it with a dot: `value.method()`. Every string comes with these:

```python
name = "  Tanvi Kumar  "
print(name.lower())
print(name.upper())
print(name.strip())
```

```
  tanvi kumar  
  TANVI KUMAR  
Tanvi Kumar
```

- **`lower()`** makes every letter small. **`upper()`** makes every letter capital.
- **`strip()`** removes spaces from both ends (not from the middle).

```python
ip = "1.1.1.1"
print(ip.replace(".", "[.]"))
print("hello".find("l"))
print("hello".find("z"))
```

```
1[.]1[.]1[.]1
2
-1
```

- **`replace(old, new)`** swaps every `old` piece for `new`.
- **`find(piece)`** gives the index where `piece` first appears. If it isn't there, you get `-1`.

Two methods answer yes/no questions about the letters:

```python
print("2024".isdigit())
print("20a4".isdigit())
print("abc123".isalnum())
print("a,b".isalnum())
```

```
True
False
True
False
```

- **`isdigit()`**: is every character a digit (0 to 9)?
- **`isalnum()`**: is every character a letter or a digit? ("alnum" is short for alphabet + number.) A comma or a space makes it `False`.

## Split a sentence into words, and join them back

**`split()`** cuts a string into words wherever there are spaces.

```python
sentence = "fly me   to the moon"
words = sentence.split()
print(words)
print(words[-1])
print(len(words))
```

```
['fly', 'me', 'to', 'the', 'moon']
moon
5
```

The thing in square brackets is a **list**: many values kept in order. Lists are the next page. For now, notice that the same index tricks work on it: `words[-1]` is the last word, and `len(words)` counts the words.

Also notice: the extra spaces between "me" and "to" disappeared. `split()` with nothing in the brackets handles any number of spaces.

You can split on something else too, like a comma: `"a,b,c".split(",")` gives `['a', 'b', 'c']`.

**`join()`** does the opposite. It glues a list of strings together, with the string before the dot in between:

```python
print(" ".join(words))
print("-".join(words))
```

```
fly me to the moon
fly-me-to-the-moon
```

## You can't change a string, only make a new one

You can't swap one bead on a string. Try:

```python
word = "python"
word[0] = "j"
```

```
TypeError: 'str' object does not support item assignment
```

Strings can't be changed in place. Instead, build a **new** string from pieces:

```python
word = "python"
new_word = "j" + word[1:]
print(new_word)
print(word)
```

```
jython
python
```

The same is true for methods. `lower()`, `replace()` and the others give you a new string. The old one stays as it was:

```python
s = "hello"
s.upper()
print(s)
s = s.upper()
print(s)
```

```
hello
HELLO
```

The first `s.upper()` made `"HELLO"` and then threw it away, because nothing kept it. To keep it, put it back in the box: `s = s.upper()`.

## Numbers to text and back: `str()` and `int()`

- **`str(x)`** turns a number into text.
- **`int(x)`** turns text made of digits into a number.

Why would you want this? Text has tools that numbers don't. You can't reverse the number `123`, but you can reverse the text `"123"`:

```python
n = 123
print(str(n))
print(str(n)[::-1])
print(int("42") + 1)
print(len(str(98765)))
```

```
123
321
43
5
```

`len(str(98765))` is a quick way to count the digits in a number.

## f-strings: put values inside text

An **f-string** is a string with an `f` before the quotes. Anything inside `{ }` is worked out and dropped into the text.

```python
name = "Tanvi"
age = 20
print(f"{name} is {age} years old")
print(f"{name} has {len(name)} letters")
print(f"Next year: {age + 1}")
```

```
Tanvi is 20 years old
Tanvi has 5 letters
Next year: 21
```

This is the easiest way to mix text and numbers in one line.

## Try it

Run `examples/06-strings.py`:

```bash
python3 examples/06-strings.py
```

Then change the word at the top to your own name and run it again. Predict each line before you look.

## Common mistakes

**Asking for an index that doesn't exist.** `"python"` has indexes 0 to 5, so:

```python
word = "python"
print(word[6])
```

```
IndexError: string index out of range
```

It means "there's no letter at that position". The last index is `len(word) - 1`.

**Adding text and a number.**

```python
print("Age: " + 20)
```

```
TypeError: can only concatenate str (not "int") to str
```

**Concatenate** means "join together". Python won't join text and a number with `+`. Use `"Age: " + str(20)`, or an f-string: `f"Age: {20}"`.

**Forgetting to keep the new string.** `s.replace("a", "b")` on its own line changes nothing you can see, and there's no error. Write `s = s.replace("a", "b")`.

## Check yourself

1. `fruit = "banana"`. What are `fruit[1]`, `fruit[-2]` and `fruit[1:4]`?
2. What does `str(-121)[::-1]` give? Is it the same as `str(-121)`?
3. What does `"a b c".split()` give, and how would you join it back with no spaces at all?

## Next

Time to use this on real problems: **Stage 2** in the LeetCode list (`leetcode-list.pdf`).
