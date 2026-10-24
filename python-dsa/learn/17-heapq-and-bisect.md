# heapq and bisect

After this page you'll be able to always get the smallest (or biggest) item out fast with `heapq`, and find where a value belongs in a sorted list with `bisect`.

Two small tools from Python's standard library. Neither needs installing; you `import` them.

## Part 1: `heapq`, a smallest-first pile

### A hospital emergency room

At a ticket counter, people are served in the order they arrived (the queue from page 16). In a hospital emergency room, they aren't. Each patient gets an urgency number, and whoever is most urgent is seen next, whenever they arrived. New patients keep arriving; each time a doctor is free, the most urgent one goes in.

A **heap** works like that. You can put items in at any time, and when you take one out, you always get the **smallest**. Python's heap tools live in a module called **`heapq`** ("heap queue"):

```python
import heapq
```

`import heapq` brings in the whole module, so you write its name in front of each tool: `heapq.heappush(...)`. (That's the difference from `from collections import deque` on page 16, where you name the tool once and then use it on its own.)

### Push, pop, peek

A heap is a **normal Python list**. You start with an empty one and use `heapq`'s functions on it:

```python
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 8)
heapq.heappush(heap, 3)
print(heap)
print(heap[0])
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heap)
```

You'll see:

```
[1, 3, 8, 5]
1
1
3
[5, 8]
```

| What | How | Time it takes |
| --- | --- | --- |
| put an item in | `heapq.heappush(heap, x)` | fast |
| take the smallest out | `heapq.heappop(heap)` | fast |
| look at the smallest, without taking it | `heap[0]` | instant |
| how many items | `len(heap)` | instant |

### It looks unsorted. That's fine.

Look at the first `print`: `[1, 3, 8, 5]`. That's not sorted (8 comes before 5). A heap doesn't keep the whole list in order, because that would be slow. It keeps only **just enough** order to promise one thing: **`heap[0]` is always the smallest**. Each time you push or pop, `heapq` moves a few items around to keep that promise.

So don't read `heap[1]`, `heap[2]` or `heap[-1]` and expect them to mean anything. Only `heap[0]`, and only what `heappop` gives you.

Pop everything, and the items come out in sorted order:

```python
heap = []
for n in [5, 1, 8, 3, 9, 2]:
    heapq.heappush(heap, n)
print(heap)

while heap:
    print(heapq.heappop(heap), end=" ")
print()
```

```
[1, 3, 2, 5, 9, 8]
1 2 3 5 8 9 
```

(`end=" "` makes `print` put a space at the end instead of starting a new line, so the numbers stay on one line. The empty `print()` finishes the line.)

### `heapify`: turn a whole list into a heap

If you already have a list, you don't need to push the items one by one. **`heapq.heapify`** rearranges the list itself into a heap:

```python
nums = [7, 2, 9, 4, 1]
heapq.heapify(nums)
print(nums)
print(nums[0])
```

```
[1, 2, 9, 4, 7]
1
```

Like `sort()` on page 7, `heapify` changes the list in place and returns `None`. So write `heapq.heapify(nums)` on its own line, never `nums = heapq.heapify(nums)`.

### Biggest first: the minus trick

`heapq` only does smallest-first. To get the **biggest** first, store every number with a minus sign. The biggest number becomes the smallest negative, so it comes out first. Put the minus back when you take it out.

```python
nums = [7, 2, 9, 4, 1]
heap = []
for n in nums:
    heapq.heappush(heap, -n)
print(heap)
print(-heapq.heappop(heap))
print(-heapq.heappop(heap))
print(-heap[0])
```

```
[-9, -4, -7, -2, -1]
9
7
4
```

```
 numbers:        7    2    9    4    1
 stored as:     -7   -2   -9   -4   -1
 smallest stored:              -9   ->  out comes -9  ->  put the minus back: 9
```

### Tuples: `(priority, item)`

In the emergency room, you want to know **who** is next, not only their urgency number. Push a tuple: the number first, then the thing it belongs to.

```python
patients = []
heapq.heappush(patients, (2, "Riya"))
heapq.heappush(patients, (1, "Aman"))
heapq.heappush(patients, (3, "Tanvi"))
heapq.heappush(patients, (1, "Kabir"))

while patients:
    urgency, name = heapq.heappop(patients)
    print(urgency, name)
```

```
1 Aman
1 Kabir
2 Riya
3 Tanvi
```

Tuples are compared **item by item**, from the left. Python compares the first items; only if they're equal does it look at the second items:

```python
print((1, "Kabir") < (2, "Aman"))
print((1, "Aman") < (1, "Kabir"))
print((2, 5) < (2, 3))
```

```
True
True
False
```

So the heap sorts by urgency, and a **tie** is broken by the second item. Aman and Kabir both have urgency 1, and `"Aman" < "Kabir"` (alphabetical), so Aman comes out first.

A tie-break needs the second items to be comparable. Numbers and strings are. Your own objects, like `ListNode` from page 15, are not:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

```python
heap = []
heapq.heappush(heap, (1, ListNode(10)))
heapq.heappush(heap, (1, ListNode(20)))
```

```
TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
```

Two items with the same priority, so Python tried to compare the two nodes, and it doesn't know how. The fix is to put a number that's always different in the middle, like a counter, so Python never reaches the nodes:

```python
heap = []
heapq.heappush(heap, (1, 0, ListNode(10)))
heapq.heappush(heap, (1, 1, ListNode(20)))
priority, i, node = heapq.heappop(heap)
print(priority, i, node.val)
```

```
1 0 10
```

### The k biggest or smallest: `nlargest` and `nsmallest`

When you need the few biggest or smallest items once, there's a shortcut:

```python
scores = [55, 92, 78, 99, 63, 85]
print(heapq.nlargest(3, scores))
print(heapq.nsmallest(2, scores))

words = ["kiwi", "banana", "fig", "apple"]
print(heapq.nlargest(2, words, key=len))
```

```
[99, 92, 85]
[55, 63]
['banana', 'apple']
```

`key=len` works the same way as in `sorted` (page 13): compare the words by their length.

### Keeping only the k biggest, as numbers arrive

Sometimes the numbers arrive one at a time, and after each one you need to know "what's the 3rd biggest so far?". Think of a top-3 leaderboard that only has 3 slots. When a new score arrives, put it on the board. If there are now 4, remove the **smallest** one. The board always holds the 3 biggest so far, and the smallest score on the board is the 3rd biggest overall.

A heap of size k does exactly that, and its smallest item, `heap[0]`, is the k-th biggest:

```python
k = 3
heap = []
for score in [5, 1, 9, 3, 7, 8]:
    heapq.heappush(heap, score)
    if len(heap) > k:
        heapq.heappop(heap)
    print("after", score, "-> heap", heap, "  3rd biggest so far:", heap[0])
```

```
after 5 -> heap [5]   3rd biggest so far: 5
after 1 -> heap [1, 5]   3rd biggest so far: 1
after 9 -> heap [1, 5, 9]   3rd biggest so far: 1
after 3 -> heap [3, 5, 9]   3rd biggest so far: 3
after 7 -> heap [5, 7, 9]   3rd biggest so far: 5
after 8 -> heap [7, 8, 9]   3rd biggest so far: 7
```

(For the first two scores there aren't 3 yet, so `heap[0]` is only the smallest so far.)

On LeetCode this shows up inside a "design" class (page 15), where the heap is kept on `self` between calls. For example the template for 703, Kth Largest Element in a Stream, starts with `def __init__(self, k: int, nums: list[int]):`. **`list[int]`** is the same as `List[int]` from page 5: a list of whole numbers. LeetCode now writes it in small letters, which needs no import.

## Part 2: `bisect`, finding a place in a sorted list

### Putting a book on a sorted shelf

Your books are in order of height. You get a new book. You don't check every book; you look in the middle, see whether the new one is taller or shorter, and keep halving the part of the shelf you look at. In a few looks you find its place.

That's what **`bisect`** ("cut in two") does for a **sorted** list: it tells you the index where a value **is**, or where it **would go**.

```python
import bisect

nums = [10, 20, 30, 30, 40]
print(bisect.bisect_left(nums, 30))
print(bisect.bisect_right(nums, 30))
print(bisect.bisect_left(nums, 25))
print(bisect.bisect_right(nums, 25))
print(bisect.bisect_left(nums, 5))
print(bisect.bisect_left(nums, 50))
```

```
2
4
2
2
0
5
```

Picture the gaps between the boxes. `bisect` tells you which gap the value belongs in:

```
 index:        0      1      2      3      4
            ┌──────┬──────┬──────┬──────┬──────┐
 nums:      │  10  │  20  │  30  │  30  │  40  │
            └──────┴──────┴──────┴──────┴──────┘
 gap:      0      1      2      3      4      5
                         ▲             ▲
            bisect_left(30) = 2        bisect_right(30) = 4
            (before the 30s)           (after the 30s)

 25 isn't there: it would go in gap 2 (between 20 and 30), left or right.
  5 would go first (gap 0). 50 would go last (gap 5 = len(nums)).
```

- **`bisect_left(nums, x)`**: the first index where `x` could go and keep the list sorted, **before** any items equal to `x`. Another way to say it: the index of the first item that is `>= x`.
- **`bisect_right(nums, x)`**: the same, but **after** any items equal to `x`. The index of the first item that is `> x`.
- If `x` isn't in the list, both give the same answer: where it would go.

Three handy uses:

```python
x = 30
i = bisect.bisect_left(nums, x)
print(i < len(nums) and nums[i] == x)
print(bisect.bisect_right(nums, x) - bisect.bisect_left(nums, x))
print(bisect.bisect_left(nums, 25))
```

```
True
2
2
```

1. **Is `x` in the list?** Check that `i` isn't past the end, and that the item at `i` really is `x`. (Both checks: `i` can be `len(nums)`, and `and` stops before `nums[i]` crashes.)
2. **How many times does `x` appear?** Right minus left: 4 − 2 = 2.
3. **How many items are smaller than `x`?** `bisect_left` itself: 2 items are smaller than 25.

### `insort`: put it in its place

**`bisect.insort`** finds the place and inserts the value there, so the list stays sorted:

```python
shelf = [10, 20, 30, 40]
bisect.insort(shelf, 25)
bisect.insort(shelf, 5)
print(shelf)
```

```
[5, 10, 20, 25, 30, 40]
```

**Careful:** `bisect` trusts that the list is already sorted. On an unsorted list it doesn't complain; it gives you a wrong answer.

### The same thing, by hand

What `bisect_left` does inside is a **binary search**: look at the middle, throw away the half that can't hold the answer, repeat. Here it is as a small loop, with a `print` so you can watch it:

```python
def my_bisect_left(nums, x):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        print(f"  left={left} right={right} mid={mid} nums[mid]={nums[mid]}")
        if nums[mid] < x:
            left = mid + 1      # the answer is to the right of mid
        else:
            right = mid - 1     # mid might be the answer; look left of it too
    return left

nums = [10, 20, 30, 30, 40, 50, 60]
print(my_bisect_left(nums, 30))
print(bisect.bisect_left(nums, 30))
```

```
  left=0 right=6 mid=3 nums[mid]=30
  left=0 right=2 mid=1 nums[mid]=20
  left=2 right=2 mid=2 nums[mid]=30
2
2
```

Step by step, looking for 30:

```
 index:   0   1   2   3   4   5   6
 nums:   10  20  30  30  40  50  60

 left=0 right=6 mid=3   nums[3]=30, not < 30   -> right = 2   (look in 0..2)
 left=0 right=2 mid=1   nums[1]=20, < 30       -> left = 2    (look in 2..2)
 left=2 right=2 mid=2   nums[2]=30, not < 30   -> right = 1
 left=2 > right=1: stop.  The answer is left = 2.
```

- **`mid = (left + right) // 2`**: the middle index. It must be `//` (whole-number division, page 2), because an index can't be 2.5.
- Each step throws away half of what's left. For a list of a million items, that's only about 20 steps. Checking every item would be a million.
- When the loop stops, `left` has landed on the answer: the first index whose item is `>= x`.

It agrees with `bisect.bisect_left` for a value that's missing too. 45 isn't in the list; both say it would go at index 5, between 40 and 50:

```python
print(my_bisect_left(nums, 45))
print(bisect.bisect_left(nums, 45))
```

```
  left=0 right=6 mid=3 nums[mid]=30
  left=4 right=6 mid=5 nums[mid]=50
  left=4 right=4 mid=4 nums[mid]=40
5
5
```

For a "find the target and return its index, or -1" problem, the loop is the same shape: inside it, check `nums[mid] == x` first and return `mid` as soon as you find it. You'll write that one yourself in the practice stage.

## Try it

Run `examples/17-heapq-and-bisect.py`:

```bash
python3 examples/17-heapq-and-bisect.py
```

Push your own numbers into the heap, change `k`, and try `bisect` with values that are and aren't in the list. Predict each answer before you run it.

## Common mistakes

**Popping from an empty heap.**

```python
heap = []
heapq.heappop(heap)
```

```
IndexError: index out of range
```

Same as an empty stack: check `if heap:` (or `while heap:`) before popping.

**Thinking `heap[-1]` is the biggest.**

```python
heap = []
for n in [5, 1, 8, 3]:
    heapq.heappush(heap, n)
print(heap[-1])
```

```
5
```

The biggest is 8, but `heap[-1]` is 5. Only `heap[0]` has a meaning. For biggest-first, use the minus trick.

**Forgetting `heapq.` in front.**

```python
heap = []
heappush(heap, 1)
```

```
NameError: name 'heappush' is not defined
```

With `import heapq`, every tool is written `heapq.something`.

**Using `/` for the middle.**

```python
nums = [10, 20, 30, 40]
mid = (0 + 3) / 2
print(nums[mid])
```

```
TypeError: list indices must be integers or slices, not float
```

`/` always gives a decimal (`1.5`), and an index must be a whole number. Use `//`.

## Check yourself

1. You push 6, 2, 9, 4 into an empty heap. What does `heap[0]` give? What do the first two `heappop`s give?
2. How would you get the biggest number out first with `heapq`?
3. `nums = [1, 3, 3, 3, 7]`. What do `bisect_left(nums, 3)`, `bisect_right(nums, 3)` and `bisect_left(nums, 4)` give?

## Next

Practise: **Stage 13** in the LeetCode list (`leetcode-list.pdf`).
