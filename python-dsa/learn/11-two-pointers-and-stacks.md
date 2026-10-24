# Two pointers and stacks

After this page you'll be able to walk through a list with two positions at once, and use a list as a stack to match things up.

These aren't new Python. They're two **techniques**: ways of using the lists, loops and indexes you already know. Many easy LeetCode problems are one of these two in disguise.

## Part 1: two pointers

### Two fingers on a list

Lay a row of cards on a table and put one finger on the first card and one on the last. Compare the two cards, do something, then move one or both fingers inwards. Stop when the fingers meet.

A **pointer** here is a variable that holds an index: it "points" at one box of the list. **Two pointers** means two such variables, moving through the same list.

There are two common ways to move them:

1. **From both ends towards the middle.**
2. **Both from the start, at different speeds**: one reads every item, the other only moves when it writes something.

### From both ends: reverse a list in place

Swap the first and last items, then the second and second-last, and so on, until the pointers meet.

```python
def reverse_in_place(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

letters = ["a", "b", "c", "d", "e"]
reverse_in_place(letters)
print(letters)
```

You'll see:

```
['e', 'd', 'c', 'b', 'a']
```

Step by step (`L` is `left`, `R` is `right`):

```
 [ a, b, c, d, e ]
   L           R       swap a and e, move both inwards

 [ e, b, c, d, a ]
      L     R          swap b and d, move both inwards

 [ e, d, c, b, a ]
         L
         R             left is not < right: stop
```

The swap line is the tuple swap from page 10. The list is changed in place, so it works for "modify the list, return nothing" problems. Notice `while left < right`: the loop stops when the fingers meet in the middle. The middle item doesn't need to move.

### From both ends: is it a palindrome?

A **palindrome** reads the same forwards and backwards, like "racecar". Compare the two ends; if they ever differ, it's not one.

```python
def is_palindrome(word):
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("racecar"))
print(is_palindrome("rocket"))
```

```
True
False
```

```
 r a c e c a r
 L           R      r == r, move in
   L       R        a == a, move in
     L   R          c == c, move in
       LR           pointers met: it's a palindrome ✓

 r o c k e t
 L         R        r != t: not a palindrome ✗ (stop at once)
```

`word[::-1] == word` gives the same answer. The two-pointer way is worth knowing because it can stop early, and because it bends to fit harder problems (for example, skipping characters you don't care about).

### Slow and fast: a "write" pointer and a "read" pointer

Now both pointers start at the left.

- The **read** pointer looks at every item, one by one.
- The **write** pointer marks the next box to fill with an item you want to **keep**. It only moves when you keep something.

Everything you keep gets packed to the front of the list, in the same order. Example: keep only the positive numbers, in place, and return how many you kept.

```python
def keep_positives(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] > 0:
            nums[write] = nums[read]
            write += 1
    return write

nums = [3, -1, 4, -5, 9]
k = keep_positives(nums)
print(k)
print(nums[:k])
print(nums)
```

```
3
[3, 4, 9]
[3, 4, 9, -5, 9]
```

Step by step (`W` is `write`, `R` is `read`):

```
 [ 3, -1,  4, -5,  9 ]
   W
   R                     3 > 0: keep. copy to W's box, W moves on

 [ 3, -1,  4, -5,  9 ]
       W
       R                 -1: skip. only R moves

 [ 3, -1,  4, -5,  9 ]
       W   R             4 > 0: keep. copy 4 to W's box, W moves on

 [ 3,  4,  4, -5,  9 ]
           W   R         -5: skip

 [ 3,  4,  4, -5,  9 ]
           W       R     9 > 0: keep. copy 9 to W's box, W moves on

 [ 3,  4,  9, -5,  9 ]
               W         R has finished. W is 3: three items kept
```

The first `k` boxes hold the answer. Whatever is left after them doesn't matter (here, `-5, 9` are leftovers).

This one shape solves a whole family of problems. Only two things change: **what you keep** (positives here; it could be "not zero", or "different from the last one I kept"), and **what you do after the loop** with the leftover boxes. You'll meet three of these in the next practice stage.

## Part 2: stacks

### A pile of plates

Think of a pile of clean plates. You put a new plate **on top**. When you need one, you take it **from the top**. You never pull one out from the middle. The last plate you put on is the first one you take off.

That's a **stack**. In Python, a plain list works as a stack:

| Plates | Stack word | Python |
| --- | --- | --- |
| put a plate on top | **push** | `stack.append(x)` |
| take the top plate | **pop** | `stack.pop()` |
| look at the top plate | **peek** | `stack[-1]` |
| no plates left? | **empty** | `len(stack) == 0` |

```python
plates = []
plates.append("red")
plates.append("blue")
plates.append("green")
print(plates)
print(plates[-1])
top = plates.pop()
print(top)
print(plates)
print(len(plates) == 0)
```

```
['red', 'blue', 'green']
green
green
['red', 'blue']
False
```

The end of the list is the top of the pile. `append` and `pop` both work at the end, so they always deal with the top.

(In other people's code you'll see `if not stack:` for "is the stack empty?". An empty list counts as `False`, so `not stack` is `True` when it's empty. It means the same as `len(stack) == 0`.)

### Matching brackets

When is a string of brackets correct? Every opening bracket needs a closing bracket of the **same kind**, and they have to close in the right order: the most recently opened one closes first. "Most recent first" is exactly what a stack does.

The idea:

- Opening bracket `(` `[` `{`: **push** it. It's waiting for its partner.
- Closing bracket: the top of the stack must be its partner. If it is, **pop** it (that pair is done). If it isn't, or the stack is empty, the string is wrong.
- At the end, the stack must be **empty**. Anything left was never closed.

Walk through `"([])"`:

```
 ch    kind       what happens                         stack after
 (     opening    push                                 ['(']
 [     opening    push                                 ['(', '[']
 ]     closing    top is '[', the partner of ']': pop  ['(']
 )     closing    top is '(', the partner of ')': pop  []
 end              stack is empty                       valid ✓
```

And two that go wrong:

```
 "(]"
 (     opening    push                                 ['(']
 ]     closing    top is '(', not the partner of ']'   not valid ✗

 "(("
 (     opening    push                                 ['(']
 (     opening    push                                 ['(', '(']
 end              stack is not empty                   not valid ✗
```

Here's the same idea in code for the simplest case, round brackets only:

```python
def round_brackets_ok(s):
    stack = []
    for ch in s:
        if ch == "(":
            stack.append(ch)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

print(round_brackets_ok("(()())"))
print(round_brackets_ok("(()"))
print(round_brackets_ok("())("))
```

```
True
False
False
```

With three kinds of bracket, you also have to check that the top is the right **partner** before popping. Working that out is your first problem in the next stage. (Hint: a dictionary from page 9 is a neat way to say "the partner of `)` is `(`".)

## Try it

Run `examples/11-two-pointers-and-stacks.py`:

```bash
python3 examples/11-two-pointers-and-stacks.py
```

It prints the pointers at every step, so you can watch them move. Change the lists and the strings and see what happens.

## Common mistakes

**Popping from an empty stack.**

```python
stack = []
stack.pop()
```

```
IndexError: pop from empty list
```

There's no plate to take. Before you `pop` (or peek with `stack[-1]`), check the stack isn't empty. In bracket problems, an empty stack when a closing bracket arrives means the answer is "not valid", not a crash.

**Starting `right` at `len(nums)`.** The last index is `len(nums) - 1`. Starting at `len(nums)` gives `IndexError: list index out of range` on the first step.

**Forgetting to move a pointer.** If nothing inside the `while` changes `left` or `right`, the loop never ends. Press **Ctrl+C** and check that every path through the loop moves at least one pointer.

## Check yourself

1. For `[1, 2, 3, 4]`, which pairs of items does the reverse loop swap, and when does it stop?
2. In the write/read example, why does `write` sometimes stay still while `read` moves?
3. Push `1`, push `2`, pop, push `3`. What's on the stack now, top last?

## Next

Practise: **Stage 7** in the LeetCode list (`leetcode-list.pdf`).
