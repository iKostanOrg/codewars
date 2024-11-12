"""
Assert Sudoku by row
Helper method for Did I Finish my Sudoku?
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def assert_sudoku_by_row(board: list) -> bool:
    """
    Assert Sudoku by row
    :param board: list
    :return: bool
    """
    for row in board:
        #print(row)
        if len(row) != len(set(row)) or len(row) != len(board[0]):
            return False

        for i in row:
            if not isinstance(i, int):
                return False

    return True
