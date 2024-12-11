"""
Assert Sudoku by column.

Helper method for Did I Finish my Sudoku?
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def assert_sudoku_by_column(board: list) -> bool:
    """
    Assert Sudoku by column.

    :param board: list
    :return: bool
    """
    row_length: int = len(board[0])

    for i in range(row_length):
        col: set = {row[i] for row in board}
        if len(col) != row_length:
            return False

    return True
