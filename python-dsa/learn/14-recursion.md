# Recursion

After this page you'll be able to write a function that calls itself, put a helper function inside a LeetCode method, and know what to do when Python says `RecursionError` or `UnboundLocalError`.

## Russian dolls

You've seen Russian dolls (matryoshka): open a doll, and there's a smaller doll inside. Open that one, and there's a smaller one again. You keep going until you reach the tiny doll in the middle, which doesn't open. Then you're done.

Every step is the same job ("open this doll") on a **smaller** doll. And there's a **last** doll that stops it all.

A function that calls itself works the same way. This is called **recursion**. Each call does a small part of the work and hands a smaller version of the problem to another call of the same function. One small case is answered straight away, and that stops it.

## A function that calls itself

```python
def countdown(n):
    if n == 0:
        print("Go!")
        return
    print(n)
    countdown(n - 1)

countdown(3)
```

You'll see:

```
3
2
1
Go!
```

`countdown(3)` prints 3, then calls `countdown(2)`. That prints 2 and calls `countdown(1)`, which prints 1 and calls `countdown(0)`. And `countdown(0)` prints "Go!" and returns without calling anything. Every call is a smaller doll, and `countdown(0)` is the one that doesn't open.

## The two parts every recursive function needs

1. **The base case**: the small case you answer straight away, without calling yourself. Here, `n == 0`. It's the tiny doll.
2. **The smaller step**: call yourself on a **smaller** problem. Here, `countdown(n - 1)`. Each call must get closer to the base case.

Write the base case first, at the top of the function. Then ask: "if a call on a smaller input already gave me the right answer, how do I finish the job?"

## Returning answers

Most of the time the function **returns** something, and each call builds its answer from the smaller call's answer.

### Sum of a list

The sum of `[3, 1, 4]` is "the first item, plus the sum of the rest". The rest is a smaller list. The sum of an empty list is 0: that's the base case.

```python
def total(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + total(nums[1:])

print(total([3, 1, 4]))
```

```
8
```

`nums[1:]` is the list without its first item (slicing, page 7), so every call gets a shorter list until it's empty.

### Factorial

The **factorial** of 4, written 4!, is `4 × 3 × 2 × 1 = 24`. Notice that `4!` is `4 × 3!`, and `3!` is `3 × 2!`. Each one is "this number times the factorial of the one below". The base case: `1!` is 1.

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(4))
print(factorial(5))
```

```
24
120
```

## Watching the calls stack up

How does `factorial(4)` work out 24? It can't multiply until it knows `factorial(3)`. So it **waits**, and `factorial(3)` starts. That one waits for `factorial(2)`, and so on, down to the base case. Then the answers come back up, one at a time.

Here's the same function with prints added, so you can watch. `depth` counts how deep we are, only so each level is pushed further right (`"    " * depth` is 4 spaces repeated `depth` times):

```python
def factorial(n, depth):
    pad = "    " * depth
    print(pad + f"factorial({n}) starts")
    if n == 1:
        print(pad + "base case: return 1")
        return 1
    answer = n * factorial(n - 1, depth + 1)
    print(pad + f"factorial({n}) returns {answer}")
    return answer

print(factorial(4, 0))
```

```
factorial(4) starts
    factorial(3) starts
        factorial(2) starts
            factorial(1) starts
            base case: return 1
        factorial(2) returns 2
    factorial(3) returns 6
factorial(4) returns 24
24
```

The same thing as a picture:

```
  going down (each call waits)            coming back up (answers return)

  factorial(4) = 4 * factorial(3)  ....   4 * 6  = 24   <- final answer
     factorial(3) = 3 * factorial(2) ...  3 * 2  = 6
        factorial(2) = 2 * factorial(1)   2 * 1  = 2
           factorial(1) = 1  ─────────────────┘
           (base case: stop going down)
```

Remember the pile of plates from page 11? Python keeps the waiting calls in a pile just like that, called the **call stack**. Each new call goes on top. When a call returns, it's taken off the top, and the call underneath carries on from where it was waiting. The last call to start is the first to finish.

## Two calls at once: Fibonacci

The **Fibonacci** numbers start 0, 1, and then each one is the sum of the two before it: 0, 1, 1, 2, 3, 5, 8, 13, ... So `fib(n)` is `fib(n - 1) + fib(n - 2)`. The first two, `fib(0)` is 0 and `fib(1)` is 1, are the base case.

```python
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(1))
print(fib(2))
print(fib(10))
```

```
1
1
55
```

This function calls itself **twice**. Those two calls each call twice, and so on. That's fine for small `n`, but it repeats a lot of work. You'll see how much, and the fix, further down.

## When there's no base case: `RecursionError`

Leave out the base case, and the calls never stop going down:

```python
def factorial(n):
    return n * factorial(n - 1)

print(factorial(4))
```

The error message is long. The end of it looks like this:

```
  File ".../factorial.py", line 2, in factorial
    return n * factorial(n - 1)
               ^^^^^^^^^^^^^^^^
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
```

`factorial(4)` called `factorial(3)`, then 2, 1, 0, -1, -2, ... with nothing to stop it. Python allows about 1000 waiting calls on the pile. After that it gives up with **`RecursionError`**: "too many calls inside calls". "Previous line repeated 996 more times" is the same call, again and again.

When you see this error, look at two things: is there a base case, and does every call really get closer to it?

## A helper function inside a LeetCode method

On LeetCode, your code lives inside `class Solution`. The usual way to write recursion there is to put a small **helper** function **inside** the method, and call it once to start things off.

A made-up LeetCode-style problem: return the sum of `nums`. Here's the recursive way, with a helper that adds up from index `i` to the end:

```python
class Solution:
    def sumList(self, nums: list[int]) -> int:
        def add_from(i):
            if i == len(nums):
                return 0
            return nums[i] + add_from(i + 1)

        return add_from(0)

print(Solution().sumList([3, 1, 4]))
```

```
8
```

Things to notice:

- `def add_from(i):` is written **inside** `sumList`, indented one more level. It only exists inside `sumList`.
- The helper uses `nums` without it being passed in. A function defined inside another one can **read** the outer function's variables.
- The helper carries an index `i` instead of slicing the list. That's the usual style: the list stays the same, and `i` moves.
- The helper doesn't need `self`. Only the method on `Solution` has `self`.
- `return add_from(0)` starts the recursion at index 0 and returns its answer.

In other people's solutions, this helper is very often called **`dfs`**, short for **depth-first search**: "go as deep as you can before coming back", which is exactly what the calls above do. The name doesn't matter to Python. `dfs`, `helper`, `add_from` all work the same.

### Changing an outer variable: `nonlocal`

Now count the even numbers, with a counter that the helper adds to:

```python
class Solution:
    def countEvens(self, nums: list[int]) -> int:
        count = 0

        def visit(i):
            if i == len(nums):
                return
            if nums[i] % 2 == 0:
                count += 1
            visit(i + 1)

        visit(0)
        return count

print(Solution().countEvens([4, 7, 2, 8]))
```

```
UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
```

Reading an outer variable is fine. **Changing** one is different. When a function puts a new value in a name (`count += 1` means `count = count + 1`), Python decides that `count` is the helper's own, new, **local** variable (one that belongs only to this function). That local `count` has no value yet, so `count + 1` fails.

**`nonlocal count`** at the top of the helper says: "`count` isn't mine; I mean the one in the function outside".

```python
class Solution:
    def countEvens(self, nums: list[int]) -> int:
        count = 0

        def visit(i):
            nonlocal count
            if i == len(nums):
                return
            if nums[i] % 2 == 0:
                count += 1
            visit(i + 1)

        visit(0)
        return count

print(Solution().countEvens([4, 7, 2, 8]))
```

```
3
```

Rule of thumb: if the helper does `name = ...` or `name += ...` to an outer variable, it needs `nonlocal name`.

## Two styles: return the answer up, or collect into a list

There are two common ways for recursion to produce its answer. You'll see both in solutions.

**Style 1: return the answer up.** Each call returns its part, and the caller adds them together. No outer variable, so no `nonlocal`:

```python
class Solution:
    def countEvens(self, nums: list[int]) -> int:
        def evens_from(i):
            if i == len(nums):
                return 0
            rest = evens_from(i + 1)
            if nums[i] % 2 == 0:
                return 1 + rest
            return rest

        return evens_from(0)

print(Solution().countEvens([4, 7, 2, 8]))
```

```
3
```

**Style 2: collect into a list.** Make an empty list outside the helper, and let the helper `append` to it:

```python
class Solution:
    def findEvens(self, nums: list[int]) -> list[int]:
        found = []

        def visit(i):
            if i == len(nums):
                return
            if nums[i] % 2 == 0:
                found.append(nums[i])
            visit(i + 1)

        visit(0)
        return found

print(Solution().findEvens([4, 7, 2, 8]))
```

```
[4, 2, 8]
```

No `nonlocal` here. `found.append(...)` changes the list itself; it never puts a new value in the name `found`. Same idea as page 7: changing the boxes is fine, replacing the whole shelf is not.

Use style 1 when the answer is one value built from smaller answers (a sum, a count, a biggest). Use style 2 when you're gathering many things along the way.

## `@cache`: remembering answers

Back to Fibonacci, which calls itself twice. How many calls does it really make? Here's `fib` as a helper with a call counter (using `nonlocal`, from above):

```python
def count_calls(n):
    calls = 0

    def fib(k):
        nonlocal calls
        calls += 1
        if k < 2:
            return k
        return fib(k - 1) + fib(k - 2)

    answer = fib(n)
    print(f"fib({n}) = {answer}, using {calls} calls")

count_calls(10)
count_calls(20)
count_calls(25)
```

```
fib(10) = 55, using 177 calls
fib(20) = 6765, using 21891 calls
fib(25) = 75025, using 242785 calls
```

Almost a quarter of a million calls for `fib(25)`. That's because it works out the same small answers again and again: `fib(25)` asks for `fib(24)` and `fib(23)`, but `fib(24)` also asks for `fib(23)`, and so on all the way down.

The fix: write each answer down the first time, and look it up after that. Like keeping a notebook of sums you've already done. Python has this ready-made. It's called **`cache`** and lives in the **`functools`** toolbox:

```python
from functools import cache

def count_calls(n):
    calls = 0

    @cache
    def fib(k):
        nonlocal calls
        calls += 1
        if k < 2:
            return k
        return fib(k - 1) + fib(k - 2)

    answer = fib(n)
    print(f"fib({n}) = {answer}, using {calls} calls")

count_calls(10)
count_calls(20)
count_calls(25)
```

```
fib(10) = 55, using 11 calls
fib(20) = 6765, using 21 calls
fib(25) = 75025, using 26 calls
```

Same answers. 26 calls instead of 242785.

The only change is the line **`@cache`** right above `def fib`. A line starting with `@` above a `def` is called a **decorator**: it adds an extra behaviour to the function. `@cache` gives the function a memory. The first time `fib(k)` is asked for, it works out the answer and saves it. Every time after that, it hands back the saved answer straight away, without running the function again.

It works because `fib(23)` always gives the same answer, so it's safe to remember it. On LeetCode, `from functools import cache` is allowed; put it at the top.

## How deep can it go?

Python allows about 1000 calls waiting on the pile at once:

```python
import sys

print(sys.getrecursionlimit())
```

```
1000
```

If a problem's input is so big that your recursion goes deeper than that (for example, a list of 5000 items handled one call per item), you can raise the limit with `sys.setrecursionlimit(10000)` at the top of your file. You'll rarely need it in easy problems.

## Try it

Run `examples/14-recursion.py`:

```bash
python3 examples/14-recursion.py
```

It has countdown, the factorial trace, a helper inside `class Solution`, and the `@cache` call count. Change the numbers, and try removing the `nonlocal` line to see the error for yourself.

## Common mistakes

**No base case, or a step that doesn't get smaller.** Both give the `RecursionError` above. Writing `countdown(n)` instead of `countdown(n - 1)` is the same problem: every call has the same `n`, so it prints `3` again and again and never reaches 0.

**Forgetting `return` in front of the recursive call.**

```python
def factorial(n):
    if n == 1:
        return 1
    n * factorial(n - 1)

print(factorial(3))
```

```
TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
```

The last line works out `n * factorial(n - 1)` and then throws it away, so `factorial(2)` returns `None` (page 4). Then `factorial(3)` tries `3 * None`, and that's the error. It should be `return n * factorial(n - 1)`.

**Calling a `Solution` method by its bare name.** LeetCode's Fibonacci problem is a method named `fib` inside `class Solution`:

```python
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

print(Solution().fib(5))
```

```
NameError: name 'fib' is not defined. Did you mean: 'self.fib'?
```

A method lives inside the class, so on its own the name `fib` means nothing. Python's suggestion is right: call it as `self.fib(n - 1)`. Or use a helper function inside the method, as above; a helper is called by its plain name.

## Check yourself

1. In `total(nums)` above, what is the base case, and what makes each call's list smaller?
2. Why does `count += 1` inside a helper need `nonlocal count`, but `found.append(x)` doesn't need `nonlocal found`?
3. `fib(30)` without `@cache` makes over a million calls. With `@cache`, roughly how many?

## Next

Practise: **Stage 10** in the LeetCode list (`leetcode-list.pdf`).
