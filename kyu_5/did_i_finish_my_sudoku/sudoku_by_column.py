"""
Assert Sudoku by column
Helper method for Did I Finish my Sudoku?
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def assert_sudoku_by_column(board: list) -> bool:
    """
    Assert Sudoku by column
    :param board: list
    :return: bool
    """
    row_length: int = len(board[0])

    for i in range(0, row_length):
        col = set()
        for row in board:
            col.add(row[i])
        if len(col) != row_length:
            return False

    return True
