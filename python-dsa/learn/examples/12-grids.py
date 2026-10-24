# Page 12: Grids
# Run me with:  python3 12-grids.py

# A grid is a list of rows. grid[r][c]: row first, then column.
grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
rows = len(grid)        # 3  (how many rows)
cols = len(grid[0])     # 4  (how many columns)
print("rows:", rows, "cols:", cols)
print(grid[1][2])       # 7

# Print it as a grid, one row per line
for row in grid:
    for value in row:
        print(value, end=" ")
    print()

# Sum of every row, then of every column
for r in range(rows):
    print("row", r, "sum:", sum(grid[r]))
for c in range(cols):
    total = 0
    for row in grid:
        total += row[c]
    print("col", c, "sum:", total)

# A fresh grid of zeros, the right way (each row is a new list)
seen = [[0] * cols for _ in range(rows)]
seen[0][0] = 1
print(seen)             # only one cell changed

# A real copy: copy every row
copy = [row[:] for row in grid]
copy[0][0] = 99
print(copy[0], grid[0])  # the original is untouched

# The four neighbours of (r, c), skipping the ones outside the grid
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
r, c = 1, 2
for dr, dc in directions:
    nr = r + dr
    nc = c + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        print(f"neighbour ({nr}, {nc}) holds {grid[nr][nc]}")
    else:
        print(f"({nr}, {nc}) is outside the grid")

# Transpose: rows become columns
flipped = [list(col) for col in zip(*grid)]
print(flipped)          # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# A grid of strings, as LeetCode often gives it
board = ["#..", ".#.", "..#"]
walls = 0
for row in board:
    for ch in row:
        if ch == "#":
            walls += 1
print("walls:", walls)  # 3

# Try changing things:
#   1. Set r, c = 0, 0 (a corner). Which neighbours are outside?
#   2. Add a fourth row to grid. Do the sums still work?
#   3. Make seen with [[0] * cols] * rows instead. What happens to seen?
