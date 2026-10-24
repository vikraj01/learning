# Dictionaries

After this page you'll be able to store "this goes with that" pairs, count things, and remember where you saw something.

## The contacts app on your phone

Your phone's contacts app doesn't store numbers in a numbered row. You don't think "Mum is contact number 37". You type **Mum**, and the phone finds her number straight away.

Each entry is a pair: a **name** and the **number** that goes with it. The name is how you look things up.

Python has the same thing. It's called a **dictionary** (`dict` for short). You'll also hear it called a **map** or a **hash map**, because it maps each name to its value. All three words mean the same thing here.

- The thing you look up by (the name) is the **key**.
- The thing you get back (the number) is the **value**.
- A key and its value together are a **key-value pair**.

## Making one and reading from it

Curly brackets. Each pair is written `key: value`, with commas between pairs.

```python
contacts = {"Mum": "98100 11111", "Vikash": "98200 22222"}
print(contacts["Mum"])
print(len(contacts))
```

You'll see:

```
98100 11111
2
```

- `contacts["Mum"]` looks up the key `"Mum"` and gives you its value. Same square brackets as a list, but you put a **key** inside, not a position.
- `len` counts the pairs.

The lookup is fast, however big the dictionary gets. Your phone doesn't read every contact to find Mum, and neither does Python. That speed is why dictionaries show up in so many LeetCode answers.

Keys are usually strings or numbers. Values can be anything: numbers, strings, lists.

## A key that isn't there: `get`

If you ask for a key that doesn't exist, Python stops with an error:

```python
print(contacts["Riya"])
```

```
KeyError: 'Riya'
```

**`get`** is the safe way to ask. If the key isn't there, it gives you `None`, or a default value that you choose:

```python
print(contacts.get("Mum"))
print(contacts.get("Riya"))
print(contacts.get("Riya", "not saved"))
```

```
98100 11111
None
not saved
```

Remember `.get(key, 0)`. You'll use it for counting in a moment.

## Adding and changing

Put a value in with `=`. If the key is new, the pair is added. If the key is already there, its value is replaced.

```python
contacts["Riya"] = "98300 33333"     # new key: added
contacts["Mum"] = "98100 99999"      # old key: updated
print(contacts)
```

```
{'Mum': '98100 99999', 'Vikash': '98200 22222', 'Riya': '98300 33333'}
```

A dictionary can't hold the same key twice. Like your phone, there's one entry per name.

## Is this key in it? `in`

```python
print("Riya" in contacts)
print("98300 33333" in contacts)
```

```
True
False
```

`in` checks the **keys** only. `"98300 33333"` is a value, not a key, so the answer is `False`.

## Looping over a dictionary

A plain `for` loop gives you each key:

```python
for name in contacts:
    print(name)
```

```
Mum
Vikash
Riya
```

**`.items()`** gives you each key and its value together. Name both, like with `enumerate`:

```python
for name, number in contacts.items():
    print(name, "->", number)
```

```
Mum -> 98100 99999
Vikash -> 98200 22222
Riya -> 98300 33333
```

There's also **`.keys()`** for only the keys and **`.values()`** for only the values. For example, `max(counts.values())` gives the biggest value.

## Pattern: counting things

This is the dictionary pattern you'll use most. How many times does each letter appear in `"banana"`?

```python
counts = {}
for ch in "banana":
    counts[ch] = counts.get(ch, 0) + 1
print(counts)
print(counts["a"])
```

```
{'b': 1, 'a': 3, 'n': 2}
3
```

The middle line does all the work. Read it as: "look up how many `ch` I've counted so far (0 if this is the first one), add 1, and store it back."

```
 ch    counts.get(ch, 0)   counts after this step
 b     0                   {'b': 1}
 a     0                   {'b': 1, 'a': 1}
 n     0                   {'b': 1, 'a': 1, 'n': 1}
 a     1                   {'b': 1, 'a': 2, 'n': 1}
 n     1                   {'b': 1, 'a': 2, 'n': 2}
 a     2                   {'b': 1, 'a': 3, 'n': 2}
```

Two dictionaries are equal (`==`) when they have the same pairs, in any order. So two words have the same letters, the same number of times, exactly when their counts are equal.

```python
print({"a": 1, "b": 2} == {"b": 2, "a": 1})
```

```
True
```

## Pattern: have I seen this before, and where?

Here the key is a **value from the list**, and the dictionary's value is the **index** where you saw it. You walk through the list once, and at every step you can ask "have I met this number already? Where?"

Find the first number that appears twice, and both of its positions:

```python
nums = [5, 3, 8, 3, 1]
seen = {}
for i, n in enumerate(nums):
    if n in seen:
        print(f"{n} was seen before at index {seen[n]}, and again at index {i}")
        break
    seen[n] = i
print(seen)
```

```
3 was seen before at index 1, and again at index 3
{5: 0, 3: 1, 8: 2}
```

```
 i   n   n in seen?   seen afterwards
 0   5   no           {5: 0}
 1   3   no           {5: 0, 3: 1}
 2   8   no           {5: 0, 3: 1, 8: 2}
 3   3   YES, at 1    stop
```

Notice the order inside the loop: **check first, then remember**. If you stored `n` before checking, you'd always "find" the number you had stored a moment ago.

This is the idea behind **Two Sum**, the first problem in the next practice stage. There, the question at each step changes slightly: not "have I seen *this* number?" but "have I seen the number that would *complete* my answer?"

## A shortcut: `Counter`

Counting is so common that Python has a ready-made counter. It lives in a toolbox called `collections`, so you **import** it first (bring it into your file):

```python
from collections import Counter

print(Counter("banana"))
```

```
Counter({'a': 3, 'n': 2, 'b': 1})
```

A `Counter` works like a dictionary, but asking for a missing key gives `0` instead of a `KeyError`. Write the counting loop yourself until it feels easy. Then use `Counter` when you want to save time. LeetCode allows the import.

## Try it

Run `examples/09-dictionaries.py`:

```bash
python3 examples/09-dictionaries.py
```

Then change the word it counts, and add a new contact.

## Common mistakes

**Reading a key that isn't there.**

```python
counts = {}
counts["a"] += 1
```

```
KeyError: 'a'
```

`counts["a"] += 1` means `counts["a"] = counts["a"] + 1`, and the right-hand side reads `counts["a"]`, which doesn't exist yet. That's why the counting pattern uses `counts.get(ch, 0) + 1`.

**Expecting `in` to search the values.** `in` only looks at keys. To check values, use `x in contacts.values()`.

## Check yourself

1. `ages = {"Tanvi": 20, "Vikash": 25}`. What do `ages["Tanvi"]` and `ages.get("Riya", 0)` give?
2. Count the letters of `"apple"` in your head, the way the counting pattern does. What's the final dictionary?
3. In the "seen before" pattern, what goes in the key and what goes in the value?

## Next

Practise counting and looking things up: **Stage 5** in the LeetCode list (`leetcode-list.pdf`).
