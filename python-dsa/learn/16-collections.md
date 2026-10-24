# The collections toolbox

After this page you'll be able to count and group things with less code, and use a queue that serves things in the order they arrived.

## Better kitchen tools

You can grate a carrot with a knife. It works, but a grater is faster and you're less likely to cut yourself. Python's **`collections`** is a drawer of better tools for jobs you already do with dictionaries and lists.

You met one on page 9: `Counter`. This page covers three:

```python
from collections import defaultdict, Counter, deque
```

That one line brings all three into your file. LeetCode allows it.

## `defaultdict`: a dictionary that fills in missing keys

### `defaultdict(int)` for counting

Here's the counting pattern from page 9:

```python
counts = {}
for ch in "banana":
    counts[ch] = counts.get(ch, 0) + 1
print(counts)
```

```
{'b': 1, 'a': 3, 'n': 2}
```

The `.get(ch, 0)` is there because the first time you meet a letter, it isn't a key yet. A **`defaultdict`** takes care of that for you:

```python
from collections import defaultdict

counts = defaultdict(int)
for ch in "banana":
    counts[ch] += 1
print(counts)
print(counts["a"])
```

```
defaultdict(<class 'int'>, {'b': 1, 'a': 3, 'n': 2})
3
```

When you ask a `defaultdict` for a key that isn't there, it doesn't stop with `KeyError`. It **adds** the key with a starting value, then carries on. The thing in the brackets says what the starting value is:

| You write | Starting value for a new key |
| --- | --- |
| `defaultdict(int)` | `0` |
| `defaultdict(list)` | `[]`, an empty list |
| `defaultdict(set)` | `set()`, an empty set |

So `counts[ch] += 1` works even for a brand-new letter: it starts at 0, then adds 1.

When printed, it shows `defaultdict(<class 'int'>, ...)` first. Everything else works like a normal dictionary: `in`, `.items()`, `len`, looping. If you want it to print like a normal dictionary, wrap it in `dict(...)`:

```python
print(dict(counts))
```

```
{'b': 1, 'a': 3, 'n': 2}
```

### `defaultdict(list)` for grouping

Put words into groups by their first letter. With a plain dictionary, you'd have to make each empty list yourself before appending:

```python
words = ["apple", "banana", "avocado", "cherry", "blueberry"]

groups = {}
for w in words:
    first = w[0]
    if first not in groups:
        groups[first] = []
    groups[first].append(w)
print(groups)
```

```
{'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
```

With `defaultdict(list)`, a new key starts as an empty list, so you can `append` straight away:

```python
groups = defaultdict(list)
for w in words:
    groups[w[0]].append(w)
print(dict(groups))
```

```
{'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
```

Same answer, three lines shorter.

### Grouping pairs: students by section

Often the data comes as pairs: here, each student and their section. Group the names by section:

```python
students = [("Tanvi", "10A"), ("Riya", "10B"), ("Aman", "10A"), ("Kabir", "10C"), ("Zoya", "10B")]

by_section = defaultdict(list)
for name, section in students:
    by_section[section].append(name)

for section in sorted(by_section):
    print(section, "->", by_section[section])
```

```
10A -> ['Tanvi', 'Aman']
10B -> ['Riya', 'Zoya']
10C -> ['Kabir']
```

- `for name, section in students:` unpacks each pair, like tuples on page 10.
- The key is what you group **by** (the section). The value is the list of everything in that group (the names).
- `sorted(by_section)` gives the keys in order, so the sections print as 10A, 10B, 10C.

This "group by" shape comes up a lot: words by their first letter, numbers by whether they're even or odd, words by their sorted letters.

### `defaultdict(set)`

Same idea, but each new key starts as an empty set. Use it when you don't want repeats. Here's a sign-in sheet where Tanvi signed in twice on Monday:

```python
sign_ins = [("Tanvi", "Mon"), ("Riya", "Mon"), ("Tanvi", "Mon"), ("Tanvi", "Wed")]

as_lists = defaultdict(list)
as_sets = defaultdict(set)
for name, day in sign_ins:
    as_lists[name].append(day)
    as_sets[name].add(day)

print(dict(as_lists))
print(dict(as_sets))
```

```
{'Tanvi': ['Mon', 'Mon', 'Wed'], 'Riya': ['Mon']}
{'Tanvi': {'Mon', 'Wed'}, 'Riya': {'Mon'}}
```

The list for Tanvi holds `'Mon'` twice. The set holds each day once. (A set has no order, so your run may show `{'Wed', 'Mon'}` instead. Both are the same set.) Notice it's `.add` for a set and `.append` for a list.

## `Counter`: counting in one line

`Counter` counts everything in a string or a list, and gives you a few extra tools.

```python
from collections import Counter

c = Counter("mississippi")
print(c)
print(c["s"])
print(c["z"])
print(c.most_common(2))
print(Counter([3, 1, 3, 3, 2]))
```

```
Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
4
0
[('i', 4), ('s', 4)]
Counter({3: 3, 1: 1, 2: 1})
```

- `c["s"]` reads a count, like a dictionary.
- `c["z"]` is `0`, not an error. A letter that never appeared has count 0. (Unlike `defaultdict`, reading a missing key does **not** add it.)
- **`most_common(k)`** gives the `k` most common items, biggest first, as a list of `(item, count)` tuples. Without a number, `most_common()` gives all of them in that order.

### Same letters? Compare two Counters

Two words are **anagrams** when they use exactly the same letters, the same number of times ("listen" and "silent"). Two Counters are equal (`==`) when every count matches:

```python
print(Counter("listen") == Counter("silent"))
print(Counter("apple") == Counter("plea"))
```

```
True
False
```

"plea" has one `p`, "apple" has two, so they're not equal.

### What's missing? Subtract two Counters

Say you need the letters of `"banana"` and you have the letters `"bnaxa"`. Which letters are you short of?

```python
need = Counter("banana")
have = Counter("bnaxa")
print(need - have)
print(have - need)
print(Counter("ab") - Counter("abc"))
```

```
Counter({'a': 1, 'n': 1})
Counter({'x': 1})
Counter()
```

`need - have` takes away the counts. Anything that drops to 0 or below is left out of the answer. So `need - have` shows only what you're short of: one more `a` and one more `n`. If you're short of nothing, you get an empty `Counter()`, which counts as `False` in an `if`.

## `deque`: a queue with two open ends

### A queue at a ticket counter

At a ticket counter, new people join at the **back**, and the person at the **front** is served first. First in, first out. That's a **queue**: the opposite of the pile of plates (the stack) on page 11, where the last one in was the first one out.

A **`deque`** (say "deck"; short for "double-ended queue") is a list-like row where you can add and remove at **both** ends quickly.

```python
from collections import deque

q = deque([1, 2, 3])
q.append(4)
q.appendleft(0)
print(q)
print(q.popleft())
print(q.pop())
print(q)
print(q[0], len(q))
```

```
deque([0, 1, 2, 3, 4])
0
4
deque([1, 2, 3])
1 3
```

```
            appendleft(x)                 append(x)
                 │                            │
                 ▼                            ▼
   front ──►  [ 0,   1,   2,   3,   4 ]  ◄── back
                 │                            │
                 ▼                            ▼
             popleft()                      pop()
```

| Method | What it does |
| --- | --- |
| `append(x)` | add `x` at the back (join the queue) |
| `popleft()` | take from the front (serve the next person) |
| `appendleft(x)` | add `x` at the front |
| `pop()` | take from the back |

For a queue, you use `append` and `popleft`. Indexing with `q[0]`, `len(q)` and `while q:` all work like a list.

### Why not a list?

A list can do `pop(0)` (page 7). It gives the right answer, but on a big list it's slow. A list keeps its items in numbered boxes. Take the item out of box 0, and every other item has to shift one box to the left so the list starts at 0 again. With 100,000 items, that's 99,999 moves for every single `pop(0)`. A deque doesn't renumber anything, so `popleft()` takes the same short time however long the queue is.

On LeetCode, a slow answer fails with **Time Limit Exceeded**. So: for a stack, a list is fine. For a queue, use a deque.

### `maxlen`: keep only the last few

`deque(maxlen=3)` holds at most 3 items. When it's full and you `append`, the oldest item falls off the front:

```python
recent = deque(maxlen=3)
for n in [1, 2, 3, 4, 5]:
    recent.append(n)
print(recent)
```

```
deque([3, 4, 5], maxlen=3)
```

Handy for "the last k things" problems.

## Putting it together: a ticket counter

Here's a counter where three people are waiting. Each person buys **one** ticket per turn. If they need more, they go to the back of the queue and wait again. Each item in the queue is a tuple: `(name, tickets still needed)`.

```python
queue = deque([("Tanvi", 2), ("Riya", 1), ("Aman", 3)])
turn = 0

while queue:
    name, needed = queue.popleft()
    turn += 1
    needed -= 1
    print("turn", turn, ":", name, "buys a ticket, needs", needed, "more")
    if needed > 0:
        queue.append((name, needed))
    print("        waiting now:", list(queue))
```

```
turn 1 : Tanvi buys a ticket, needs 1 more
        waiting now: [('Riya', 1), ('Aman', 3), ('Tanvi', 1)]
turn 2 : Riya buys a ticket, needs 0 more
        waiting now: [('Aman', 3), ('Tanvi', 1)]
turn 3 : Aman buys a ticket, needs 2 more
        waiting now: [('Tanvi', 1), ('Aman', 2)]
turn 4 : Tanvi buys a ticket, needs 0 more
        waiting now: [('Aman', 2)]
turn 5 : Aman buys a ticket, needs 1 more
        waiting now: [('Aman', 1)]
turn 6 : Aman buys a ticket, needs 0 more
        waiting now: []
```

The mechanics, one piece at a time:

1. **Set up.** `deque([...])` starts the queue with three tuples in it. The first one is the front.
2. **`while queue:`** keeps going until nobody is left. An empty deque counts as `False`, like an empty list.
3. **Out of the front:** `queue.popleft()` takes the first tuple, and `name, needed = ...` unpacks it (page 10).
4. **Back in at the back:** if they still need tickets, `queue.append((name, needed))` puts them behind everyone already waiting. Notice the double brackets: the outer pair is the call to `append`, the inner pair makes the tuple.

So everyone gets a turn before anyone gets a second turn. Riya needs only one ticket, so after her first turn she leaves for good. Aman needs three, so he's the last to finish, on turn 6.

## Try it

Run `examples/16-collections.py`:

```bash
python3 examples/16-collections.py
```

Add a person to the ticket queue, or give Riya 4 tickets to buy, and predict the order of turns before you run it.

## Common mistakes

**Reading a missing key in a `defaultdict` adds it.**

```python
counts = defaultdict(int)
counts["a"] += 1
if counts["z"] == 0:
    print("no z")
print(dict(counts))
```

```
no z
{'a': 1, 'z': 0}
```

Just looking at `counts["z"]` created the key `"z"`. If you then loop over the dictionary or use `len`, `"z"` is there too. To check without adding, use `in`: `"z" in counts`.

**Putting a list in a set.**

```python
seen = set()
seen.add([1, 2])
```

```
TypeError: unhashable type: 'list'
```

**Unhashable** means "can't be used as a set item or a dictionary key". Lists can change, so Python won't let them in. Use a tuple: `seen.add((1, 2))`.

**Taking from an empty queue.**

```python
q = deque()
q.popleft()
```

```
IndexError: pop from an empty deque
```

Use `while queue:` so you only take from the queue while there's something in it.

**Using `list.pop(0)` for a queue.** It gives the right answer, so nothing warns you. On a big input it can make LeetCode say **Time Limit Exceeded**. Use a `deque` and `popleft()`.

## Check yourself

1. What does `Counter("hello")["l"]` give? And `Counter("hello")["x"]`?
2. You group `["cat", "cow", "dog"]` by first letter with `defaultdict(list)`. What's in the dictionary at the end?
3. A deque holds `[5, 6, 7]`. You run `append(8)` and then `popleft()`. What comes out, and what's left?

## Next

Practise: **Stage 12** in the LeetCode list (`leetcode-list.pdf`).
