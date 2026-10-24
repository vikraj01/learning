# Lists

After this page you'll be able to keep many values in one place, in order, and change them.

## A shelf of numbered boxes

Picture a shelf with a row of boxes. Each box holds one thing, and each box has a number painted under it, starting at 0. You can look in any box, swap what's inside, add a box at the end, or take one away.

That shelf is a **list**. Most LeetCode problems hand you a list, usually called `nums`. When the problem says `nums: List[int]`, it means "a list of whole numbers".

## Making a list, and reading from it

Square brackets, with commas between the items:

```python
nums = [4, 8, 15, 16, 23]
```

```
 nums = [4, 8, 15, 16, 23]

  +----+----+----+----+----+
  |  4 |  8 | 15 | 16 | 23 |
  +----+----+----+----+----+
     0    1    2    3    4      <- index
    -5   -4   -3   -2   -1      <- negative index
```

Everything you learned about strings works here: index, negative index, `len`, slicing.

```python
nums = [4, 8, 15, 16, 23]
print(nums[0])
print(nums[-1])
print(len(nums))
print(nums[1:3])
print(nums[::-1])
```

You'll see:

```
4
23
5
[8, 15]
[23, 16, 15, 8, 4]
```

A list can hold any kind of value: numbers, strings, `True`/`False`, even other lists. The `split()` from the last page gave you a list of strings.

## Changing an item

Here's the big difference from strings. A list **can** be changed in place. Put a new value in a box:

```python
nums = [4, 8, 15, 16, 23]
nums[0] = 99
print(nums)
```

```
[99, 8, 15, 16, 23]
```

## Adding and taking away: `append`, `insert`, `pop`

```python
fruits = ["apple", "mango"]
fruits.append("kiwi")
print(fruits)
fruits.insert(0, "banana")
print(fruits)
```

```
['apple', 'mango', 'kiwi']
['banana', 'apple', 'mango', 'kiwi']
```

- **`append(x)`** adds `x` at the end. This is the one you'll use most.
- **`insert(i, x)`** puts `x` at index `i` and pushes everything after it one box along.

```python
last = fruits.pop()
print(last)
print(fruits)
first = fruits.pop(0)
print(first)
print(fruits)
```

```
kiwi
['banana', 'apple', 'mango']
banana
['apple', 'mango']
```

- **`pop()`** takes the last item off the list and gives it to you.
- **`pop(i)`** takes the item at index `i`.

## Is it on the shelf? `in`

```python
print("mango" in fruits)
print("grape" in fruits)
```

```
True
False
```

## Joining and repeating lists: `+` and `*`

```python
print([1, 2] + [3, 4])
print([0] * 5)
print([1, 2] * 3)
```

```
[1, 2, 3, 4]
[0, 0, 0, 0, 0]
[1, 2, 1, 2, 1, 2]
```

`+` puts two lists end to end. `*` repeats a list. `[0] * 5` is a handy way to make a list of five zeros.

## Sorting: `sort()` and `sorted()`

There are two ways to sort, and the difference matters.

**`sort()`** sorts the list itself. The old order is gone.

```python
marks = [70, 45, 90, 60]
marks.sort()
print(marks)
```

```
[45, 60, 70, 90]
```

**`sorted()`** leaves the list alone and gives you a **new**, sorted list.

```python
marks = [70, 45, 90, 60]
ordered = sorted(marks)
print(ordered)
print(marks)
```

```
[45, 60, 70, 90]
[70, 45, 90, 60]
```

For biggest first, add `reverse=True` in the brackets: `sorted(marks, reverse=True)` gives `[90, 70, 60, 45]`. The same works with `marks.sort(reverse=True)`.

**The trap:** `sort()` changes the list but gives back nothing. Remember `None` from page 4, the value of "nothing came back"?

```python
marks = [70, 45, 90, 60]
result = marks.sort()
print(result)
```

```
None
```

So never write `marks = marks.sort()`. That sorts the list, then throws it away and puts `None` in the box. Either write `marks.sort()` on its own line, or `marks = sorted(marks)`.

## Quick answers: `sum`, `max`, `min`, `reverse`

```python
marks = [70, 45, 90, 60]
print(sum(marks))
print(max(marks))
print(min(marks))
marks.reverse()
print(marks)
```

```
265
90
45
[60, 90, 45, 70]
```

- **`sum`** adds everything up. **`max`** gives the biggest, **`min`** the smallest.
- **`reverse()`** flips the list itself, back to front. Like `sort()`, it changes the list and returns `None`.

## Lists inside lists

A list can hold other lists. Think of a shelf where each box holds a smaller shelf.

```python
accounts = [[1, 2, 3], [3, 2, 1], [5, 5, 5]]
print(accounts[1])
print(accounts[1][2])
print(len(accounts))
print(sum(accounts[2]))
```

```
[3, 2, 1]
1
3
15
```

```
 accounts =  [ [1, 2, 3],  [3, 2, 1],  [5, 5, 5] ]
                  0            1            2

 accounts[1]     ->  [3, 2, 1]
 accounts[1][2]  ->  [3, 2, 1][2]  ->  1
```

Read `accounts[1][2]` left to right: first take box 1 (a whole list), then box 2 inside that.

## A function that changes a list changes it for everyone

When you pass a list to a function, the function gets the **same** shelf, not a copy. If it changes the shelf, the caller sees the change.

```python
def double_first(nums):
    nums[0] = nums[0] * 2

my_list = [5, 6, 7]
double_first(my_list)
print(my_list)
```

```
[10, 6, 7]
```

The function returned nothing, but `my_list` changed.

This matters on LeetCode. Some problems say **"Do not return anything, modify nums in-place"**. **In place** means "change the list you were given, don't make a new one". LeetCode then looks at your list, not at what you returned.

One catch. Changing the boxes changes the caller's list. Putting a whole new list in the name does **not**:

```python
def reverse_wrong(nums):
    nums = nums[::-1]     # a NEW list, only inside this function

def reverse_right(nums):
    nums.reverse()        # changes the list itself

a = [1, 2, 3]
reverse_wrong(a)
print(a)
reverse_right(a)
print(a)
```

```
[1, 2, 3]
[3, 2, 1]
```

`nums = ...` inside a function makes the name `nums` point at a new shelf. The caller's shelf is untouched. For in-place problems, use things that change the list itself: `nums[i] = ...`, `append`, `pop`, `sort()`, `reverse()`.

## Try it

Run `examples/07-lists.py`:

```bash
python3 examples/07-lists.py
```

Then add your own list of five numbers and print its biggest, smallest and total.

## Common mistakes

**An index past the end.** `[4, 8, 15]` has indexes 0, 1, 2:

```python
nums = [4, 8, 15]
print(nums[3])
```

```
IndexError: list index out of range
```

It means "there's no box with that number". The last index is `len(nums) - 1`. This is the error you'll see most often with lists.

**Keeping the result of `sort()`.**

```python
marks = [3, 1]
marks = marks.sort()
print(marks[0])
```

```
TypeError: 'NoneType' object is not subscriptable
```

`marks` is now `None`, and you can't use `[0]` on `None`. ("Subscriptable" means "you can use square brackets on it".)

## Check yourself

1. `nums = [2, 7, 11, 15]`. What are `nums[-1]` and `nums[1:3]`?
2. After `x = [3, 1, 2]` and `y = sorted(x)`, what is in `x`, and what is in `y`?
3. `grid = [[1, 2], [3, 4]]`. How do you get the `3`?

## Next

Practise with lists: [Practice stage 3: lists](../practice/README.md#stage-3-lists).
