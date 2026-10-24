# Classes for LeetCode

After this page you'll be able to read LeetCode's `ListNode` and `TreeNode`, build linked lists and trees by hand to test on your laptop, and write a small class that remembers things between calls.

This page teaches only the part of classes that LeetCode needs. There's a lot more to classes; you don't need it yet.

## A blank form and filled-in forms

Think of a college admission form. The blank form says what every student must fill in: name, age. It isn't about any one student. Then each student fills in their own copy: one copy says "Tanvi, 20", another says "Riya, 19".

In Python:

- A **class** is the blank form. It says what every copy will have.
- An **object** is one filled-in copy. You can make as many as you like from one class.
- The things written on a copy (name, age) are its **attributes**.

You've been using a class since page 5 without looking inside: `class Solution:`. Now you'll write your own.

## Your first class

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Student("Tanvi", 20)
b = Student("Riya", 19)
print(a.name, a.age)
print(b.name, b.age)
```

You'll see:

```
Tanvi 20
Riya 19
```

Line by line:

1. `class Student:` starts the blank form, named `Student`. Class names start with a capital letter, by habit.
2. `def __init__(self, name, age):` is a function inside the class. A function inside a class is called a **method**. This one has a special name: `__init__` (two underscores on each side, short for "initialise", meaning "set up"). Python runs it **by itself** every time you make a new object. Its job is to fill in the form.
3. **`self`** is the copy being filled in right now. `self.name = name` means "on **this** copy, write `name` in the name box".
4. `Student("Tanvi", 20)` makes a new object. You call the class like a function. Python makes a fresh copy, runs `__init__` with `self` as that copy, `name` as `"Tanvi"` and `age` as `20`, and gives you the copy back. You never pass `self` yourself; Python does it.
5. `a.name` reads an attribute. The dot means "the `name` of `a`".

`a` and `b` are two separate copies. Changing one doesn't touch the other:

```python
a.age = 21
print(a.age)
print(b.age)
```

```
21
19
```

So now `self` in `class Solution` makes sense: LeetCode makes one `Solution()` object and calls your method on it, and `self` is that object. In normal problems you don't need it.

## Default values in `def`

One more small thing you'll meet in a moment. A parameter can have a **default value**: what it gets if the caller leaves it out.

```python
def greet(name="friend"):
    print("Hello", name)

greet("Tanvi")
greet()
```

```
Hello Tanvi
Hello friend
```

## `None`: "nothing there"

You met `None` on page 4: the value of "nothing came back". With classes it gets a new job. An attribute that holds `None` means **"there's nothing here"**: no next item, no child, empty.

`None` counts as `False` in an `if`, the same way an empty list does (page 11). So `if not x:` is `True` when `x` is `None`.

```python
x = None
print(x is None)
if not x:
    print("nothing there")
```

```
True
nothing there
```

`is None` is the usual way to compare with `None`. `if not x:` is shorter, and you'll see both in LeetCode answers.

## Linked lists: `ListNode`

### A train

Think of a train. Each coach carries passengers, and each coach is coupled to the **next** coach. There's no list of coaches anywhere: to reach coach 3, you start at the engine and walk through coach 1, then coach 2. The last coach is coupled to nothing.

A **linked list** is a train of objects. Each object is a **node**, and each node holds two things:

- **`val`**: its value (the passengers),
- **`next`**: the next node (the coupling), or `None` if it's the last one.

The first node is called the **head**. You only ever get the head; everything else you reach by following `next`.

### LeetCode's definition

At the top of every linked list problem, LeetCode shows this:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
```

It's commented out (every line starts with `#`) because LeetCode already has this class behind the scenes. It's there so you know what a node looks like. **Singly-linked** means each node only knows the next one, not the one before.

On your laptop, the class has to really exist, so remove the `#`s:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

It's a form with two boxes, `val` and `next`. Both have default values: `ListNode()` makes a node with `val` 0 and `next` `None`.

### Building `1 -> 2 -> 3` by hand

Build the train from the back, so each node can be coupled to one that already exists:

```python
third = ListNode(3)
second = ListNode(2, third)
first = ListNode(1, second)
head = first

print(head.val)
print(head.next.val)
print(head.next.next.val)
print(head.next.next.next)
```

```
1
2
3
None
```

```
 head
  │
  ▼
 ┌─────┬──────┐    ┌─────┬──────┐    ┌─────┬──────┐
 │ val │ next │    │ val │ next │    │ val │ next │
 │  1  │  ●───┼───►│  2  │  ●───┼───►│  3  │ None │
 └─────┴──────┘    └─────┴──────┘    └─────┴──────┘

 head.val             -> 1
 head.next.val        -> 2
 head.next.next.val   -> 3
 head.next.next.next  -> None   (the end of the train)
```

Read `head.next.next.val` left to right: start at `head`, go to its next node, go to that node's next node, read its value.

You can also build it from the front by setting `next` afterwards:

```python
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
print(head.next.next.val)
```

```
3
```

### Walking the list: `while node:`

You can't use `for` or `len` on a linked list. You walk it yourself, one coach at a time:

```python
node = head
while node:
    print(node.val)
    node = node.next
print("reached the end")
```

```
1
2
3
reached the end
```

```
 node     prints   node = node.next
 1        1        2
 2        2        3
 3        3        None   <- `while node:` is now False, loop stops
```

These two lines are the heart of every linked list problem:

- `while node:` means "while there **is** a node" (while `node` isn't `None`).
- `node = node.next` steps forward one coach.

Use a separate name like `node` (or `cur`, short for "current") for walking, so `head` still points at the start when you're done.

### The error you'll see most: `'NoneType' object has no attribute 'val'`

Walk one step too far, and you're holding `None`, not a node. `None` has no `val`:

```python
node = head
while node:
    node = node.next
print(node.val)
```

```
AttributeError: 'NoneType' object has no attribute 'val'
```

Read it as: "you asked for `.val` on something that is `None`". **NoneType** is the type of `None`. After the loop, `node` is `None`, because that's what stopped the loop.

The same happens on LeetCode when the list is **empty**. An empty linked list is passed to you as `head = None`, and `head.val` crashes straight away. Two ways to stay safe:

1. **Check first.** At the start of a method, `if not head: return ...` handles the empty list.
2. **Check before you look ahead.** If you need the next node's value, check that it exists: `while node and node.next:`. Python reads `and` left to right and stops at the first `False`, so when `node` is `None` it never reaches `node.next`.

```python
empty = None
if not empty:
    print("empty list, nothing to do")

node = head
while node and node.next:
    print(node.val, "is followed by", node.next.val)
    node = node.next
```

```
empty list, nothing to do
1 is followed by 2
2 is followed by 3
```

### Helpers to test on your laptop

LeetCode turns `head = [1,2,3]` into nodes for you. On your laptop you need two small helpers: one to turn a Python list into a linked list, and one to turn it back so you can print it.

```python
def build_list(values):
    head = None
    for v in values[::-1]:
        head = ListNode(v, head)
    return head

def to_list(head):
    values = []
    node = head
    while node:
        values.append(node.val)
        node = node.next
    return values

h = build_list([1, 2, 3])
print(h.val, h.next.val)
print(to_list(h))
print(build_list([]))
print(to_list(None))
```

```
1 2
[1, 2, 3]
None
[]
```

`build_list` builds from the back, like you did by hand: it goes through `[3, 2, 1]`, and each new node is coupled to everything built so far. An empty Python list gives `None`, the empty linked list.

### `ListNode | None`: "a node, or nothing"

Here's a real LeetCode template (problem 206, Reverse Linked List):

```python
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
```

**`ListNode | None`** is a type hint (page 5). Read the `|` as "or": "a `ListNode`, or `None`". It's LeetCode reminding you that `head` can be `None` (an empty list), and that you may return `None` too. It needs no import.

(Older solutions online write `Optional[ListNode]` instead. It means the same thing.)

Putting it together, here's a made-up problem, "return how many nodes the list has", in the LeetCode shape, tested with the helpers:

```python
class Solution:
    def countNodes(self, head: ListNode | None) -> int:
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        return count

print(Solution().countNodes(build_list([4, 5, 6])))
print(Solution().countNodes(build_list([])))
```

```
3
0
```

The order in the file matters: `ListNode` must be defined **above** `class Solution`, because the type hint mentions it.

## Trees: `TreeNode`

### A family tree

Think of a family tree drawn upside down, with one person at the top. Each person below has one parent above them. In a **binary tree**, each person has **at most two** children: a left one and a right one.

- Each person is a **node**.
- The one at the top is the **root**.
- A node's two children are its **left** and **right**. Either can be missing (`None`).
- A node with no children at all is a **leaf**.

### LeetCode's definition

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```

The same idea as `ListNode`, with two "next" boxes instead of one. Without the `#`s:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Building a small tree by hand

```
          4
        /   \
       2     7
      / \
     1   3
```

```python
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(root.val)
print(root.left.val)
print(root.right.val)
print(root.left.right.val)
print(root.right.left)
```

```
4
2
7
3
None
```

`root.left.right` reads "from the root, go left, then go right": that's the 3. `root.right.left` is `None`, because 7 has no children. 7, 1 and 3 are leaves.

The same tree in one line, with the children passed in as arguments:

```python
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
print(root.left.left.val)
```

```
1
```

On LeetCode, a tree is written as a list read top to bottom, left to right: this tree is `root = [4,2,7,1,3]`. Missing children appear as `null`.

### `if not root`

An empty tree is `root = None`. As with linked lists, check before you read:

```python
def describe(node):
    if not node:
        return "no node here"
    if not node.left and not node.right:
        return f"{node.val} is a leaf"
    return f"{node.val} has children"

print(describe(root))
print(describe(root.right))
print(describe(root.right.left))
```

```
4 has children
7 is a leaf
no node here
```

Tree problems use recursion (page 14), because each child is the root of a smaller tree. `if not root:` is the stopping case:

```python
def tree_sum(root):
    if not root:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)

print(tree_sum(root))
print(tree_sum(None))
```

```
17
0
```

LeetCode's tree templates use `TreeNode | None` the same way, for example `def maxDepth(self, root: TreeNode | None) -> int:`.

## A class that remembers: "design" problems

Some LeetCode problems don't ask for one function. They ask you to **design a class**, like `MyQueue` or `KthLargest`. LeetCode makes one object and then calls its methods many times, and your object has to **remember** things between calls.

Think of a scorer at a cricket match with a notebook. When the match starts, they open a fresh page (`__init__`). Every ball, they write something down. When someone asks "what's the score?", they read their notebook. The notebook is `self`.

Here's a made-up one: a scoreboard you can add scores to, and ask for the best score so far.

```python
class ScoreBoard:
    def __init__(self):
        self.scores = []

    def add(self, score: int) -> None:
        self.scores.append(score)

    def best(self) -> int:
        return max(self.scores)

    def count(self) -> int:
        return len(self.scores)

board = ScoreBoard()
board.add(40)
board.add(75)
board.add(62)
print(board.best())
print(board.count())
```

```
75
3
```

- `__init__` sets things up: an empty list, stored on the object as `self.scores`.
- Every other method reaches that same list through `self.scores`. That's how `best` sees what `add` stored.
- A plain `scores = []` inside `__init__` (without `self.`) would be forgotten as soon as `__init__` finished, like any variable inside a function.

On LeetCode, a design problem's template has the method names already written, and at the bottom a comment showing how LeetCode will use your class. For problem 232, Implement Queue using Stacks:

```python
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
```

(**Instantiated** means "an object is made from the class".) The examples are written as two lists: the method names, and the arguments for each call.

```
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]
```

Read them in columns: `MyQueue()` makes the object (`null`, nothing returned), `push(1)` returns nothing, `push(2)` returns nothing, `peek()` returns `1`, `pop()` returns `1`, `empty()` returns `false`.

## Try it

Run `examples/15-classes-for-leetcode.py`:

```bash
python3 examples/15-classes-for-leetcode.py
```

It builds a linked list and a tree, walks them, and uses a small design class. Change the values, add a node, and predict the output before you run it.

## Common mistakes

**Walking off the end of a list.** You've seen it above:

```
AttributeError: 'NoneType' object has no attribute 'val'
```

Something you thought was a node is `None`. Look at what the loop stopped on, or whether the input was empty. The same message with `'next'`, `'left'` or `'right'` means the same thing.

**Forgetting `self.` inside a method.**

```python
class Box:
    def __init__(self):
        self.items = []

    def add(self, x):
        items.append(x)

Box().add(5)
```

```
NameError: name 'items' is not defined. Did you mean: 'self.items'?
```

`items` on its own is a variable that doesn't exist. The list lives on the object, so it's `self.items`, and Python even suggests that at the end of the message.

**Forgetting `self` as the first parameter.**

```python
class Box:
    def add(x):
        print(x)

Box().add(5)
```

```
TypeError: Box.add() takes 1 positional argument but 2 were given
```

Python always passes the object as the first argument, so the method gets two (the object and `5`) but only has room for one. Every method starts with `self`.

**Not removing the `#`s on your laptop.** If `ListNode` is still commented out, you'll see `NameError: name 'ListNode' is not defined`.

## Check yourself

1. In `class ListNode`, what are the two attributes, and what does `next` hold on the last node?
2. `head` is the list `5 -> 8`. What are `head.next.val` and `head.next.next`?
3. In the `ScoreBoard` class, why is it `self.scores` and not just `scores`?

## Next

Practise: **Stage 11** in the LeetCode list (`leetcode-list.pdf`).
