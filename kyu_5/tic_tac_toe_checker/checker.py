"""
Solution for -> Tic-Tac-Toe Checker
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""
from typing import Any


def is_solved(board) -> int:
    """
    Checks whether the board's current state is solved:
    -1 if the board is not yet finished (there are empty spots),
    1 if "X" won,
    2 if "O" won,
    0 if it's a cat's game (i.e. a draw).

    :param board: list
    :return: -1, 0, 1, or 2
    """
    rows = check_rows(board)
    if rows:
        return rows

    cols = check_cols(board)
    if cols:
        return cols

    diagonals = check_diagonals(board)
    if diagonals:
        return diagonals

    for row in board:
        if 0 in row:
            return -1

    return 0


def check_diagonals(board) -> int | None:
    """
    Check board by diagonal
    :param board: list
    :return: 1, 2, or None
    """
    i: int = 0
    temp: set = set()
    for row in board:
        temp.add(row[i])
        i += 1

    if len(temp) == 1:
        return temp.pop()

    i = 2
    temp: set = set()
    for row in board:
        temp.add(row[i])
        i -= 1

    if len(temp) == 1:
        return temp.pop()

    return None


def check_cols(board) -> int | None:
    """
    Check board by column
    :param board: list
    :return: 1, 2, or None
    """
    for i in range(0, len(board)):
        temp = set()
        for row in board:
            temp.add(row[i])

        if len(temp) == 1:
            return temp.pop()

    return None


def check_rows(board: list) -> int | None:
    """
    Check board by row
    :param board: list
    :return: 1, 2, or None
    """
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return None
