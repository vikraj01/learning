# How a LeetCode problem looks

After this page you'll be able to read a LeetCode problem, understand the code it gives you, solve a practice file on your laptop, and submit it on LeetCode.

## A workbook with an answer checker

Remember maths workbooks with the answers at the back? You'd solve a question, then flip to the back to check.

**LeetCode** (leetcode.com) is a website full of programming questions, called **problems**, with a checker built in. You write a function, press a button, and LeetCode runs your function on lots of inputs and tells you if every answer was right. Companies use these problems in interviews, and they're a very good way to practise.

You know enough Python now to solve your first ones.

## What a problem page looks like

Open [2235. Add Two Integers](https://leetcode.com/problems/add-two-integers/). The page has two halves:

```
┌─────────────────────────────────┬─────────────────────────────────────┐
│ 2235. Add Two Integers   Easy   │  Python3 ▾                          │
│                                 │                                     │
│ Given two integers num1 and     │  class Solution:                    │
│ num2, return the sum of the     │      def sum(self, num1: int,       │
│ two integers.                   │              num2: int) -> int:     │
│                                 │                                     │
│ Example 1:                      │                                     │
│   Input: num1 = 12, num2 = 5    │                                     │
│   Output: 17                    │                                     │
│                                 │                                     │
│ Example 2:                      ├─────────────────────────────────────┤
│   Input: num1 = -10, num2 = 4   │  Testcase  |  Test Result           │
│   Output: -6                    │                                     │
│                                 │                                     │
│ Constraints:                    │                                     │
│   -100 <= num1, num2 <= 100     │             [ Run ]   [ Submit ]    │
└─────────────────────────────────┴─────────────────────────────────────┘
```

On the left, the problem:

- **Description**: what your function gets and what it must return. Read it twice.
- **Examples**: some inputs and the right output for each. Work through one on paper before writing code.
- **Constraints**: the limits on the inputs. Here, both numbers are between -100 and 100. Later, constraints tell you things like "the list is never empty", which saves you worrying about it.

On the right, the code:

- A **language** menu. Pick **Python3** (not "Python", which is an old version).
- The **code editor**, with the start of a function already written for you. This is called the **template**. You fill in the inside.
- **Run** tries your code on the examples only. Use it as often as you like.
- **Submit** runs your code on all of LeetCode's hidden tests (often hundreds) and gives the final result.

Two words you'll see in problems: an **integer** is a whole number (an `int`), and an **array** is a list of values (you'll learn lists on page 7). Also, LeetCode writes `true` and `false` in small letters, because it shares the text with other languages. In Python they're always `True` and `False`.

## `class Solution`: the box your function lives in

Here's the template again, the way it looks in a file:

```python
class Solution:
    def sum(self, num1: int, num2: int) -> int:
```

You know `def` from page 4. Two new things:

- **`class Solution:`** is a box that LeetCode puts your function in. Every problem has it. You don't need to understand classes to solve these problems. Leave that line exactly as it is, and write your function indented inside it.
- **`self`** is always the first parameter. LeetCode fills it in by itself. Ignore it for now. You never pass anything for it, and you won't use it in these problems.

So, with `self` set aside, this is a function named `sum` that takes two inputs, `num1` and `num2`. Exactly like `add(a, b)` on page 4.

## Type hints: labels on the boxes

The `: int` and `-> int` parts are **type hints**. They're labels saying what kind of value goes in and what kind comes out:

```
def sum(self, num1: int, num2: int) -> int:
                    ───        ───     ───
                     │          │       └── it returns an int
                     │          └────────── num2 is an int
                     └───────────────────── num1 is an int
```

Python doesn't check them. They're there to tell **you** what to expect. Read them first, every time. `-> int` means your answer must be a whole number, `-> bool` means `True` or `False`, `-> str` means text.

Later problems use list types like this:

```python
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
```

- **`list[int]`** means "a list of whole numbers". So `nums` is a list of ints, and the function returns a list of ints.
- **`list[str]`** is a list of strings, and **`list[list[int]]`** is a list of lists (a grid; that's lesson 12).
- Older solutions you find online write `List[int]` with a capital L and a line `from typing import List` at the top. It means the same thing; that's the older way of writing it.

## Solve your first problem on your laptop

Every problem in `../practice/` is a Python file with the template, some tests, and hints. Open `../practice/1-numbers-and-if/01-2235-add-two-integers.py`. It looks like this:

```python
"""
2235. Add Two Integers  (Easy)
https://leetcode.com/problems/add-two-integers/

In plain words:
    You get two whole numbers, num1 and num2. Return their sum.
    The numbers can be negative.

Example:
    num1 = 12, num2 = 5   ->  17
    num1 = -10, num2 = 4  ->  -6

You'll need: + (page 2), return (page 4)

Run this file:  python3 01-2235-add-two-integers.py
"""


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        # your code here
        pass


# ---------- tests: you don't need to change anything below ----------
...
```

- The top part, between the `"""` marks, explains the problem in plain words and says which pages you need.
- **`pass`** means "do nothing". It's a placeholder, because Python doesn't allow a function with no steps at all. You'll replace it.
- Below the tests line is code that checks your answer. You don't need to read or change it. (It uses things from later pages.)
- At the very bottom are **hints**. Read them only if you're stuck.

### 1. Run it before solving

In the terminal, from the `python-dsa` folder, go to the stage folder and run the file:

```bash
cd practice/1-numbers-and-if
python3 01-2235-add-two-integers.py
```

```
✗ (12, 5) -> got None but expected 17
✗ (-10, 4) -> got None but expected -6
✗ (0, 0) -> got None but expected 0
✗ (-3, -7) -> got None but expected -10
```

Each line is one test. Read the first one: with inputs `12` and `5`, your function returned `None` (nothing, because of `pass`), but the right answer is `17`. A **✗** means wrong. That's expected; you haven't written anything yet.

### 2. Write the answer

Replace the two lines `# your code here` and `pass` with:

```python
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2
```

Keep the indentation: `return` sits 8 spaces in, inside `def`, which is inside `class`.

### 3. Run it again

```bash
python3 01-2235-add-two-integers.py
```

```
✓ (12, 5) -> 17
✓ (-10, 4) -> -6
✓ (0, 0) -> 0
✓ (-3, -7) -> -10
```

Every line is **✓**. Solved.

### What a wrong answer looks like

Try `print` instead of `return`, the trap from page 4:

```python
        print(num1 + num2)
```

```
17
✗ (12, 5) -> got None but expected 17
-6
✗ (-10, 4) -> got None but expected -6
0
✗ (0, 0) -> got None but expected 0
-10
✗ (-3, -7) -> got None but expected -10
```

The right numbers appear on screen (`17`, `-6`, `0`, `-10`), but the tests still fail, because the function returned `None`. LeetCode would mark this wrong too. Put `return` back.

A wrong calculation looks like this, for example with `return num1 - num2`:

```
✗ (12, 5) -> got 7 but expected 17
✗ (-10, 4) -> got -14 but expected -6
✓ (0, 0) -> 0
✗ (-3, -7) -> got 4 but expected -10
```

"got 7 but expected 17" tells you exactly which input failed and what you returned. Work through that input by hand to find the mistake. Notice that `(0, 0)` passed by luck (`0 - 0` is also `0`). One ✓ doesn't mean the code is right; you need every line to be ✓.

## Submit on LeetCode

Once every line shows ✓:

1. Open the problem on LeetCode (the link is at the top of the file) and sign in.
2. Check the language menu says **Python3**.
3. Copy only the `class Solution` part from your file: from `class Solution:` down to your `return` line. Not the tests, not the hints.
4. Paste it into LeetCode's editor, replacing what's there.
5. Press **Run**. It tries the examples. You should see your output match the expected output.
6. Press **Submit**.

You'll see one of these:

- **Accepted** (green): every hidden test passed. Done.
- **Wrong Answer**: one of the hidden tests failed. LeetCode shows that input, your output, and the expected output. Work that input through by hand, fix your code, and submit again.
- **Runtime Error**: your code crashed, with an error message like the ones you've seen. Read the last line, as on page 1.

Wrong answers are normal, and nobody sees them but you. Submitting several times is fine.

## Try it

From the `learn` folder, run `examples/05-how-leetcode-looks.py`:

```bash
python3 examples/05-how-leetcode-looks.py
```

```
8
-6
✓ 4 -> 8
✓ -3 -> -6
✓ 0 -> 0
```

It's a made-up problem ("return `n` doubled") in the LeetCode shape, with a small checker built only from pages 1 to 4. Change `return n * 2` to `return n * 3` and see which lines turn into ✗. Then try `print(n * 2)` and look at what "got" says.

## Common mistakes

**Forgetting the indentation inside `class Solution`.** If `def` isn't pushed in under `class Solution:`, you'll see:

```
IndentationError: expected an indented block after class definition on line 1
```

`def` goes 4 spaces in. The lines inside `def` go 8 spaces in.

**Leaving `pass` and getting `None`.** If every test says `got None`, your function isn't returning anything. Check that you replaced `pass` and used `return`, not `print`.

**Renaming the function.** LeetCode calls the function by its exact name (`sum` here). If you change it to `add`, LeetCode can't find it. Keep the name and the parameters exactly as given.

## Check yourself

1. What's the difference between **Run** and **Submit** on LeetCode?
2. In `def isPowerOfTwo(self, n: int) -> bool:`, what goes in and what must come out?
3. Your file shows `got None but expected 5`. What's the most likely mistake?

## Next

Time to practise. Solve the problems in **Stage 1** of the practice list (`leetcode-list.pdf`), in order. Add Two Integers is one of them, and you've already solved it above.
