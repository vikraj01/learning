# Sets and tuples

After this page you'll be able to keep a collection with no repeats, check "have I seen this?" fast, and keep two values together as a pair.

This page has two small tools. Both are simpler than lists and dictionaries, and both show up often in LeetCode answers.

## Part 1: sets

### A guest list

Think of the guest list at the door of a wedding. Each name is on it once: writing "Tanvi" twice doesn't make two Tanvis. Nobody cares what order the names were written in. The only question the guard asks is: **"Is this name on the list?"** And the answer has to come fast.

That's a **set**: a collection where

- every item appears **only once** (no duplicates),
- there's **no order** (no index, no "first item"),
- checking `in` is **fast**, like looking up a key in a dictionary.

### Making a set

Turn a list into a set, and the repeats disappear:

```python
nums = [3, 1, 3, 2, 1, 3]
unique = set(nums)
print(unique)
print(len(nums))
print(len(unique))
```

You'll see:

```
{1, 2, 3}
6
3
```

`len(set(nums))` is the quick way to count **how many different** things there are. If it's smaller than `len(nums)`, something was repeated.

A set is written with curly brackets, like a dictionary, but with single items instead of `key: value` pairs.

### Adding, removing, checking

Start an empty set with `set()`, then use **`add`** and **`remove`**:

```python
guests = set()
guests.add("Tanvi")
guests.add("Riya")
guests.add("Tanvi")
print(len(guests))
print("Riya" in guests)
print("Aman" in guests)
guests.remove("Riya")
print("Riya" in guests)
```

```
2
True
False
False
```

Adding `"Tanvi"` a second time changed nothing. She was already on the list.

Why use a set instead of a list for "have I seen this?" Both can answer `x in ...`. A list checks its items one by one, so a long list is slow to search. A set jumps straight to the answer, like a dictionary does. On LeetCode, with big inputs, that difference can decide whether your answer passes.

A string can become a set of its letters: `set("hello")` has 4 items (`h`, `e`, `l`, `o`), because the two `l`s count once.

### Comparing two sets: `&`, `|`, `-`

```python
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a & b)
print(a | b)
print(a - b)
```

```
{3, 4}
{1, 2, 3, 4, 5}
{1, 2}
```

```
 a = {1, 2, 3, 4}        b = {3, 4, 5}

   only in a    in both    only in b
     1  2        3  4         5

 a & b  ->  {3, 4}             in both
 a | b  ->  {1, 2, 3, 4, 5}    in either
 a - b  ->  {1, 2}             in a, not in b
```

- **`a & b`** ("and"): items in **both**.
- **`a | b`** ("or"): items in **either** one.
- **`a - b`**: items in `a` that are **not** in `b`.

If a problem wants a list back, turn the set into one with `list(...)`: `list(a & b)` gives `[3, 4]`.

## Part 2: tuples

### A fixed pair

Think of a map location: latitude and longitude. They always go together, and you never change one half on its own. Or a date of birth: day, month, year.

A **tuple** is a small group of values kept together that **can't be changed** once made. You write it with round brackets:

```python
point = (3, 4)
print(point[0])
print(point[1])
print(len(point))
```

```
3
4
2
```

Indexing works like a list. Changing doesn't:

```python
point[0] = 10
```

```
TypeError: 'tuple' object does not support item assignment
```

Same as strings. If you need it different, make a new tuple.

### Unpacking: one name per value

You can take a tuple apart into separate variables in one line. This is called **unpacking**:

```python
point = (3, 4)
x, y = point
print(x)
print(y)
```

```
3
4
```

The first value goes into the first name, the second into the second.

You've done this already without knowing it. `enumerate` and `.items()` hand you a tuple each time round, and `for i, n in ...` unpacks it:

```python
for pair in enumerate(["a", "b"]):
    print(pair)
```

```
(0, 'a')
(1, 'b')
```

### Swapping two values

Swap two variables in one line:

```python
a = 1
b = 2
a, b = b, a
print(a, b)
```

```
2 1
```

Python first makes the tuple `(b, a)`, which is `(2, 1)`, and then unpacks it into `a` and `b`. You'll use this to swap two items in a list too: `nums[i], nums[j] = nums[j], nums[i]`.

### Returning two values from a function

A function can only `return` one thing. But that one thing can be a tuple, so you can hand back two answers at once:

```python
def smallest_and_biggest(nums):
    return min(nums), max(nums)

low, high = smallest_and_biggest([4, 9, 1, 7])
print(low)
print(high)
```

```
1
9
```

`return min(nums), max(nums)` returns the tuple `(1, 9)`, and the caller unpacks it.

## Try it

Run `examples/10-sets-and-tuples.py`:

```bash
python3 examples/10-sets-and-tuples.py
```

Then change the lists and predict what `&`, `|` and `-` will give.

## Common mistakes

**`{}` is an empty dictionary, not an empty set.**

```python
print(type({}))
print(type(set()))
```

```
<class 'dict'>
<class 'set'>
```

For an empty set, always write `set()`.

**Using an index on a set.**

```python
s = {1, 2, 3}
print(s[0])
```

```
TypeError: 'set' object is not subscriptable
```

A set has no order, so there's no "item 0". If you need positions, use a list.

**Removing something that isn't there.** `guests.remove("Aman")` when Aman isn't on the list gives `KeyError: 'Aman'`. Check with `in` first.

**Unpacking into the wrong number of names.** `x, y = (1, 2, 3)` gives `ValueError: too many values to unpack (expected 2)`. You need one name per value.

## Check yourself

1. What is `len(set([7, 7, 7, 1]))`?
2. `a = {"x", "y"}` and `b = {"y", "z"}`. What are `a & b` and `a - b`?
3. After `p = 5`, `q = 8`, `p, q = q, p`, what are `p` and `q`?

## Next

Practise with sets: [Practice stage 6: sets and tuples](../practice/README.md#stage-6-sets-and-tuples).
