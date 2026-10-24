# Python for problem solving

This folder teaches you Python from zero by solving 50 easy problems.

The plan is simple: learn a little, then solve problems with it straight away. You learn Python by using it, not by reading about it.

## The two PDFs

- **[python-for-leetcode.pdf](python-for-leetcode.pdf)**: lessons 1–10 in one file, each with its example script.
- **[leetcode-list.pdf](leetcode-list.pdf)**: the 50 easy practice problems (LeetCode and GeeksforGeeks), with links, in 6 stages. Tick them off as you go.

Both are built from the files in this folder with `make pdf` (from the repo root).

## How it works

1. Read a lesson. Each one is a single idea.
2. Run the matching example in `learn/examples/` and change things in it.
3. Solve that lesson's stage in the practice list.

## Lessons

| # | Lesson | You'll be able to | Then |
| --- | --- | --- | --- |
| 1 | [Run Python](learn/01-run-python.md) | run Python, print things, write a `.py` file | |
| 2 | [Variables and numbers](learn/02-variables-and-numbers.md) | store values and do maths, including `//` and `%` | |
| 3 | [If and else](learn/03-if-else.md) | make your program choose | |
| 4 | [Functions](learn/04-functions.md) | write a function that takes inputs and returns an answer | |
| 5 | [How a LeetCode problem looks](learn/05-how-leetcode-looks.md) | read `class Solution`, run a problem on your laptop, submit | Stage 1 (problems 1–7) |
| 6 | [Strings](learn/06-strings.md) | work with text: index, slice, split, replace | Stage 2 (8–14) |
| 7 | [Lists](learn/07-lists.md) | keep many values in order and change them | Stage 3 (15–18) |
| 8 | [Loops](learn/08-loops.md) | repeat work with `for` and `while` | Stage 4 (19–35) |
| 9 | [Dictionaries](learn/09-dictionaries.md) | count things and look them up fast | Stage 5 (36–43) |
| 10 | [Sets and tuples](learn/10-sets-and-tuples.md) | remember what you've seen, keep pairs together | Stage 6 (44–50) |

## Files

- `learn/`: the lessons (`.md`) and `examples/` (one script per lesson).
- `leetcode-list.md`: the source of the practice list PDF.
- `practice/` and `solutions/`: extra files you can run on your laptop, with tests built in, for many of the problems.
- `pdf/`: the script that builds the PDFs.
