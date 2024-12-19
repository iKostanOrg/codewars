"""
Solution for -> Line Safari - Is that a line?...

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

from kyu_3.line_safari_is_that_a_line.walker_class import Walker


def line(grid: list) -> bool:
    """
    You are given a grid.

    You simply need to return true/false if you
    can detect a one and only one "valid" line joining those points.
    :param grid: which always includes exactly two end-points indicated by X
    :return: true/false
    """
    if x_counter(grid) != 2:
        return False

    if not assert_x_has_rout(grid):
        return False

    walker = Walker(grid)
    while not walker.is_done:
        walker.move()

    if walker.position == 'X':
        return True

    return False


def assert_x_has_rout(grid: list) -> bool:
    """
    Make sure x has a valid route.

    :param grid:
    :return:
    """
    counter: int = 0
    for row_i, row in enumerate(grid):

        if counter == 2:
            break

        for col_i, char in enumerate(row):
            if char == 'X':
                temp = []
                # up
                if row_i >= 1 and grid[row_i - 1][col_i] in 'X|+':
                    temp.append(True)
                # down
                if row_i + 1 < len(grid) and grid[row_i + 1][col_i] in 'X|+':
                    temp.append(True)
                # left
                if col_i >= 1 and row[col_i - 1] in 'X+-':
                    temp.append(True)
                # right
                if col_i + 1 < len(row) and row[col_i + 1] in 'X+-':
                    temp.append(True)

                if len(temp) != 1:
                    return False

    return True


def x_counter(grid: list) -> int:
    """
    Counter number of X.

    :param grid: list
    :return: int
    """
    counter: int = sum(row.count('X') for row in grid)
    return counter
