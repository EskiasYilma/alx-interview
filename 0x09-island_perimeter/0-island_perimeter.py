#!/usr/bin/python3
"""
Returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    A function that Returns the perimeter of the island described in grid
    """
    if not grid:
        return 0

    p = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                p += 4
                if i > 0 and grid[i - 1][j] == 1:
                    p -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:
                    p -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    p -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:
                    p -= 1
    return p
