# Grids

After this page you'll be able to read, loop over, build and copy a **grid** (a list of lists), and look at the cells around any cell.

Many LeetCode problems hand you a grid: a map of land and water, a game board, a picture made of numbers. All of it is the list-inside-a-list from page 7. This page shows the Python you need to work with one comfortably.

## Seats in a cinema

Your cinema ticket says **row 2, seat 5**. Rows go down the hall, one behind the other. Seats go across each row. Two numbers, and you know exactly where to sit.

A grid is the same. Each cell has a **row** number (which line, going down) and a **column** number (which position along that line, going across). A grid of numbers is also called a **matrix**; LeetCode uses both words.

## Making a grid by hand

A grid is a list, and each item is one row (itself a list):

```python
grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(grid[0])
print(grid[1][2])
print(grid[2][0])
```

You'll see:

```
[1, 2, 3, 4]
7
9
```

Writing one row per line is only for your eyes; Python reads it the same as `[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]`.

```
              col 0   col 1   col 2   col 3
            +-------+-------+-------+-------+
   row 0    |   1   |   2   |   3   |   4   |
            +-------+-------+-------+-------+
   row 1    |   5   |   6   |   7   |   8   |
            +-------+-------+-------+-------+
   row 2    |   9   |  10   |  11   |  12   |
            +-------+-------+-------+-------+

   grid[1][2]  ->  row 1, then col 2  ->  7
```

**`grid[r][c]`**: row first, then column. Always in that order. Read it left to right, like on page 7: `grid[1]` is the whole row `[5, 6, 7, 8]`, and `[2]` picks box 2 inside it.

`r` and `c` are the usual short names for a row number and a column number.

## How big is it? Rows and columns

```python
grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
rows = len(grid)
cols = len(grid[0])
print(rows)
print(cols)
```

```
3
4
```

- **`len(grid)`** counts the items of the outer list. Each item is a row, so this is the **number of rows**.
- **`len(grid[0])`** is the length of the first row: the **number of columns**. Every row has the same length, so the first one is enough.

You'll write these two lines at the top of almost every grid problem.

## Changing a cell

Same as any list: put a new value in the box.

```python
grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
grid[1][2] = 0
print(grid)
```

```
[[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 11, 12]]
```

## Looping over a grid

### By value: row by row, then cell by cell

A plain `for` loop over the grid gives you one row at a time:

```python
grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for row in grid:
    print(row)
```

```
[1, 2, 3, 4]
[5, 6, 7, 8]
[9, 10, 11, 12]
```

Put a second loop inside to reach every cell:

```python
grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for row in grid:
    for value in row:
        print(value, end=" ")
    print()
```

```
1 2 3 4 
5 6 7 8 
9 10 11 12 
```

Two small `print` tricks here. Normally `print` ends with a new line. **`end=" "`** makes it end with a space instead, so the values stay on one line. And `print()` with nothing inside only ends the line, so each row starts on a new line.

### By index: when you need to know where you are

If you need `r` and `c` (to change a cell, or to look at its neighbours), loop over the indexes with `range`, like page 8:

```python
grid = [[1, 2, 3], [4, 5, 6]]
rows = len(grid)
cols = len(grid[0])
for r in range(rows):
    for c in range(cols):
        print(f"grid[{r}][{c}] is {grid[r][c]}")
```

```
grid[0][0] is 1
grid[0][1] is 2
grid[0][2] is 3
grid[1][0] is 4
grid[1][1] is 5
grid[1][2] is 6
```

The outer loop picks a row. The inner loop walks across that row. So you read the grid like a page of a book: left to right, then down to the next line.

## Sum of a row, sum of a column

A row is a list, so `sum` works on it straight away:

```python
grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(sum(grid[1]))
```

```
26
```

A column isn't stored as one list. It's spread across the rows: one value from each. So go down the rows and pick box `c` from each:

```python
grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
c = 2
total = 0
for row in grid:
    total += row[c]
print(total)
print(sum([row[c] for row in grid]))
```

```
21
21
```

```
              col 2
   [ 1,  2,  [3],  4 ]
   [ 5,  6,  [7],  8 ]      3 + 7 + 11 = 21
   [ 9, 10, [11], 12 ]
```

The second line is the same thing as a list comprehension (page 8): "`row[c]`, for each `row` in `grid`", then add them up.

## Making an empty grid the right way

Often you need a fresh grid of zeros, the same size as another one, to fill in as you go. This is the line to remember:

```python
rows = 2
cols = 3
board = [[0] * cols for _ in range(rows)]
print(board)
board[0][0] = 5
print(board)
```

```
[[0, 0, 0], [0, 0, 0]]
[[5, 0, 0], [0, 0, 0]]
```

Read it as: "make a new row `[0] * cols`, once for each number in `range(rows)`". Changing one cell changed only that cell, as it should.

**What's `_`?** It's an ordinary variable name, made of one underscore. By habit, programmers use `_` for a value they have to name but never use. Here the loop runs `rows` times, but we don't care whether it's time 0, 1 or 2. `_` says "I don't need this number". It works in a normal loop too:

```python
for _ in range(3):
    print("hi")
```

```
hi
hi
hi
```

### The trap: `[[0] * cols] * rows`

This looks like it should do the same job. It doesn't.

```python
bad = [[0] * 3] * 2
print(bad)
bad[0][0] = 5
print(bad)
```

```
[[0, 0, 0], [0, 0, 0]]
[[5, 0, 0], [5, 0, 0]]
```

You changed one cell, and **two** changed. Why?

`[0] * 3` makes **one** row. Then `* 2` doesn't make a second row; it puts the **same** row in the outer list twice. Both "rows" are one shelf with two labels on it:

```
  bad = [[0] * 3] * 2                 board = [[0] * 3 for _ in range(2)]

  bad[0] ──┐                          board[0] ──>  [ 0, 0, 0 ]
           ├──>  [ 0, 0, 0 ]          board[1] ──>  [ 0, 0, 0 ]
  bad[1] ──┘
                                      two separate rows ✓
  one row, seen twice ✗
```

It's the same idea as page 7, where a function got the **same** list, not a copy. The comprehension runs `[0] * cols` again on every turn, so each row is a new list.

`[0] * cols` on its own (one row of numbers) is fine. The trap is only when you use `*` to repeat a **list of lists**.

## Copying a grid

The same "same shelf" idea bites when copying. A plain `=` gives the grid a second name, not a copy:

```python
grid = [[1, 2], [3, 4]]
same = grid
same[0][0] = 99
print(grid)
```

```
[[99, 2], [3, 4]]
```

And `grid[:]`, which copies a normal list, isn't enough either. It makes a new outer list, but the rows inside are still the old ones:

```python
grid = [[1, 2], [3, 4]]
half = grid[:]
half[0][0] = 99
print(grid)
```

```
[[99, 2], [3, 4]]
```

To really copy, copy **every row**:

```python
grid = [[1, 2], [3, 4]]
copy = [row[:] for row in grid]
copy[0][0] = 99
print(copy)
print(grid)
```

```
[[99, 2], [3, 4]]
[[1, 2], [3, 4]]
```

`row[:]` copies one row (page 7's slicing). The comprehension does it for each row. Now the original is safe.

## The four neighbours of a cell

Many grid problems say "a cell is connected to the cells **up, down, left and right** of it". These are its four **neighbours**.

From cell `(r, c)`:

```
                 (r-1, c)
                    up
                     |
   (r, c-1)  left ─ (r, c) ─ right  (r, c+1)
                     |
                   down
                 (r+1, c)
```

Moving up means "row minus 1, same column". Down is "row plus 1". Left and right change the column. Write those four moves in a list of tuples, called **directions**. Each tuple is (change in row, change in column):

```python
grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
rows = len(grid)
cols = len(grid[0])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
r, c = 1, 2
for dr, dc in directions:
    nr = r + dr
    nc = c + dc
    print(f"({nr}, {nc}) holds {grid[nr][nc]}")
```

```
(0, 2) holds 3
(2, 2) holds 11
(1, 1) holds 6
(1, 3) holds 8
```

- `for dr, dc in directions` unpacks each tuple (page 10). `dr` is "change in row", `dc` "change in column".
- `nr` and `nc` are the **new row** and **new column**: the neighbour's position.

```
              col 0   col 1   col 2   col 3
   row 0        1       2      [3]      4
   row 1        5      [6]    ( 7 )    [8]       ( ) is the cell (1, 2)
   row 2        9      10     [11]     12        [ ] are its neighbours
```

One loop instead of four nearly identical blocks of code.

### Is it inside the grid?

Cell `(1, 2)` is in the middle, so all four neighbours exist. A cell on the edge has neighbours that fall **off** the grid. Always check before you look:

```python
grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
rows = len(grid)
cols = len(grid[0])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
r, c = 0, 0
for dr, dc in directions:
    nr = r + dr
    nc = c + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        print(f"({nr}, {nc}) holds {grid[nr][nc]}")
    else:
        print(f"({nr}, {nc}) is outside the grid")
```

```
(-1, 0) is outside the grid
(1, 0) holds 5
(0, -1) is outside the grid
(0, 1) holds 2
```

`0 <= nr < rows` is a **chained comparison**. It means `0 <= nr and nr < rows`: "`nr` is between 0 and the last row". Python lets you write it the way you'd write it in maths:

```python
x = 5
print(0 <= x < 10)
print(0 <= -1 < 10)
```

```
True
False
```

**Why the check matters even without an error.** You'd expect `grid[-1]` to crash. It doesn't: `-1` is a negative index (page 7), so it quietly gives you the **last** row.

```python
grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(grid[-1][0])
```

```
9
```

So without the check, the cell above row 0 would wrongly be "9", from the bottom of the grid. No error, just a wrong answer. Check first, every time.

## Turning a grid on its side: `zip(*grid)`

To **transpose** a grid means to turn its rows into columns: row 0 becomes column 0, and so on.

First, a new tool. **`zip`** takes several lists and walks through them together, pairing the first items, then the second items, and so on:

```python
print(list(zip([1, 2, 3], ["a", "b", "c"])))
```

```
[(1, 'a'), (2, 'b'), (3, 'c')]
```

(`list(...)` is there so you can see the result, like with `range` on page 8. You'll see more of `zip` on the next page.)

Now the transpose:

```python
grid = [[1, 2, 3], [4, 5, 6]]
print(list(zip(*grid)))
print([list(col) for col in zip(*grid)])
```

```
[(1, 4), (2, 5), (3, 6)]
[[1, 4], [2, 5], [3, 6]]
```

The `*` in front of `grid` hands each row to `zip` as a separate list. So `zip(*grid)` here means `zip([1, 2, 3], [4, 5, 6])`. `zip` then takes the first item of each row (a column!), then the second item of each row, and so on.

```
   grid                      zip(*grid)

   [ 1, 2, 3 ]               (1, 4)
   [ 4, 5, 6 ]      ->       (2, 5)
                             (3, 6)

   2 rows, 3 cols            3 rows, 2 cols
```

`zip` gives tuples. If the problem wants lists back, turn each one into a list, as in the second line.

## A grid of strings

LeetCode often gives a board as a list of strings, one string per row:

```python
board = ["#..", ".#.", "..#"]
print(board[1])
print(board[1][1])
print(len(board), len(board[0]))
count = 0
for row in board:
    for ch in row:
        if ch == "#":
            count += 1
print(count)
```

```
.#.
#
3 3
3
```

```
           col 0  col 1  col 2
   row 0     #      .      .
   row 1     .      #      .
   row 2     .      .      #
```

Reading works exactly like a grid of lists: `board[r][c]`, `len(board)`, `len(board[0])`. A string is a row of letters (page 6), so indexing into it gives one character.

**Changing** a cell doesn't work, because strings can't be changed (page 6):

```python
board = ["#..", ".#.", "..#"]
board[0][1] = "#"
```

```
TypeError: 'str' object does not support item assignment
```

If you need to change cells, turn each row into a list of letters first. `list("#..")` gives `['#', '.', '.']`. When you're done, `"".join(...)` (page 6) glues each row back into a string:

```python
board = ["#..", ".#.", "..#"]
cells = [list(row) for row in board]
print(cells)
cells[0][1] = "#"
print(["".join(row) for row in cells])
```

```
[['#', '.', '.'], ['.', '#', '.'], ['.', '.', '#']]
['##.', '.#.', '..#']
```

## Try it

Run `examples/12-grids.py`:

```bash
python3 examples/12-grids.py
```

It prints a grid, its row and column sums, a copy, and the neighbours of a cell. Change `r` and `c` to a corner cell and predict which neighbours will be "outside" before you run it.

## Common mistakes

**A row or column that doesn't exist.**

```python
grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(grid[3][0])
```

```
IndexError: list index out of range
```

There are 3 rows, so the last one is row 2. Same rule as any list: the last index is the length minus 1.

**Mixing up rows and columns.** This grid has 3 rows and 4 columns. Looping over `range(cols)` to pick rows goes one row too far:

```python
grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
rows = len(grid)
cols = len(grid[0])
for r in range(cols):
    print(grid[r][0])
```

```
1
5
9
IndexError: list index out of range
```

On a square grid this mistake hides, because rows and cols are equal. Test with a grid that isn't square. And remember: `r` goes with `rows`, `c` goes with `cols`, and it's always `grid[r][c]`.

**Making a grid with `[[0] * cols] * rows`.** No error at all, but every row is the same row. Use `[[0] * cols for _ in range(rows)]`.

## Check yourself

1. `grid = [[7, 8], [9, 10], [11, 12]]`. How many rows and columns? What is `grid[2][1]`?
2. In the 3-row, 4-column grid at the top of this page, which cells are the neighbours of `(2, 3)`, the bottom-right corner? Which of the four directions fall outside?
3. Why does `[[0] * 3] * 2` go wrong when you change a cell, and what do you write instead?

## Next

Practise: **Stage 8** in the LeetCode list (`leetcode-list.pdf`).
