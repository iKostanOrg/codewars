"""
Solution for -> Sudoku Solution Validator.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def valid_solution(board: list) -> bool:
    """
    Sudoku solution validator.

    A function that accepts a 2D array representing a Sudoku board,
    and returns true if it is a valid solution, or false otherwise.
    :param board: list
    :return: bool
    """
    return all([check_horizontally(board),
                check_vertically(board),
                check_sub_grids(board)])


def check_horizontally(board: list) -> bool:
    """
    Test horizontally.

    :param board: list
    :return: bool
    """
    for row in board:
        if sorted(row) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    return True


def check_vertically(board: list) -> bool:
    """
    Test vertically.

    :param board:
    :return:
    """
    i: int = 0
    while i < 9:
        col: list = []
        for row in board:
            col.append(row[i])
        if sorted(col) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
        i += 1
    return True


def check_sub_grids(board: list) -> bool:
    """
    Test each of the nine 3x3 sub-grids.

    (also known as blocks)
    :param board: list
    :return: bool
    """
    sub_grids: list = [
        board[0][:3] + board[1][:3] + board[2][:3],
        board[0][3:6] + board[1][3:6] + board[2][3:6],
        board[0][6:] + board[1][6:] + board[2][6:],

        board[3][:3] + board[4][:3] + board[5][:3],
        board[3][3:6] + board[4][3:6] + board[5][3:6],
        board[3][6:] + board[4][6:] + board[5][6:],

        board[6][:3] + board[7][:3] + board[8][:3],
        board[6][3:6] + board[7][3:6] + board[8][3:6],
        board[6][6:] + board[7][6:] + board[8][6:],
    ]

    for row in sub_grids:
        if sorted(row) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False

    return True
