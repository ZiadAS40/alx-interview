#!/usr/bin/python3
"""problem solving"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented in the grid.

    Args:
    grid (list of list of int): A rectangular grid where 0
    represents water and 1 represents land.

    Returns:
    int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
