# Python notebooks

Each notebook is one lesson: an explanation, code you run yourself, then tasks and a quiz that checks your answers.

Do them in order. Each one only uses what the ones before it taught. The early ones are short; the harder ideas (loops, dictionaries, recursion) get more time and more tasks.

| # | Notebook | You'll be able to |
| --- | --- | --- |
| 1 | `01-run-python.ipynb` | run code, print things, read an error |
| 2 | `02-variables-and-numbers.ipynb` | store values and do maths, including `//` and `%` |
| 3 | `03-if-else.ipynb` | make your code choose |
| 4 | `04-functions.ipynb` | write a function that returns an answer |
| 5 | `05-how-leetcode-looks.ipynb` | read `class Solution` and solve your first problems |
| 6 | `06-strings.ipynb` | work with text: index, slice, split, join |
| 7 | `07-lists.ipynb` | keep many values in order and change them |
| 8 | `08-loops.ipynb` | repeat work with `for` and `while` |
| 9 | `09-loop-patterns.ipynb` | sum, count, find the biggest, build a list, check every pair |
| 10 | `10-dictionaries.ipynb` | store and look up values by name |
| 11 | `11-counting-and-seen-before.ipynb` | count things and remember what you've seen (Two Sum) |
| 12 | `12-sets-and-tuples.ipynb` | remove duplicates, keep pairs together |
| 13 | `13-two-pointers.ipynb` | walk a list from both ends at once |
| 14 | `14-stacks.ipynb` | use a stack (valid brackets and more) |
| 15 | `15-grids.ipynb` | work with rows and columns |
| 16 | `16-handy-built-ins.ipynb` | use Python's ready-made tools, sort by your own rule |
| 17 | `17-recursion.ipynb` | write a function that calls itself |
| 18 | `18-recursion-in-practice.ipynb` | use recursion in real problems, and make it fast |
| 19 | `19-classes-and-design.ipynb` | write your own class and "design" problems |
| 20 | `20-linked-lists-and-trees.ipynb` | walk a linked list and a tree |
| 21 | `21-collections.ipynb` | use `defaultdict`, `Counter` and `deque` |
| 22 | `22-heapq-and-bisect.ipynb` | keep the smallest on top, find a place in a sorted list |

## Practice sets

The tasks inside the notebooks are warm-ups. The **practice sets** are the real workout: harder problems that mix several ideas, with edge cases to think about and hints folded away. Do each one when you reach its checkpoint.

| Set | Do it after | What it works on |
| --- | --- | --- |
| `P1-numbers-and-functions.ipynb` | notebook 5 | maths with `//` and `%`, many branches, functions using functions |
| `P2-strings-lists-loops.ipynb` | notebook 9 | text, lists and loops together |
| `P3-dictionaries-and-sets.ipynb` | notebook 12 | counting, grouping, lookups, reports |
| `P4-pointers-stacks-grids.ipynb` | notebook 16 | stacks, grids, sorting by your own rules |
| `P5-recursion-classes-collections.ipynb` | notebook 22 | recursion, your own classes, `deque`, `Counter`, heaps |
| `P6-mini-projects.ipynb` | everything | four small projects built step by step |

Give each problem 20–30 minutes before you open a hint. A problem that takes you an hour is a good problem.

Answers are in `solutions/`. Try each task yourself first.

## Start the notebooks

### The first time only

1. Install **uv**. It's a tool that installs Python and everything the notebooks need, so you don't have to do it by hand.

   On Linux or Mac, in a terminal:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   On Windows, in PowerShell:

   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

   Close the terminal and open a new one, so it finds `uv`.

2. Get this repo, if you don't have it yet:

   ```bash
   git clone https://github.com/vikraj01/learning.git
   ```

### Every time

Go into this folder and start Jupyter:

```bash
cd learning/python-dsa/notebooks
make
```

No `make` on your laptop? This does the same thing, from the same folder:

```bash
uv run jupyter lab --notebook-dir=.
```

The first time it downloads a few things, so give it a minute. Then your browser opens with the list of notebooks on the left. Double-click `01-run-python.ipynb` to open it.

Keep the terminal open while you work. Closing it stops Jupyter.

### When you're done

1. Save with **Ctrl + S**.
2. In the terminal, press **Ctrl + C**, then type `y` and press Enter.

## Getting new notebooks

When new notebooks are added, get them with:

```bash
git pull
```
