#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def valid_solution(board: list) -> bool:
    """
    A function validSolution/ValidateSolution/valid_solution()
    that accepts a 2D array representing a Sudoku board,
    and returns true if it is a valid solution, or false otherwise
    :param board:
    :return:
    """
    return all([check_horizontally(board),
                check_vertically(board),
                check_sub_grids(board)])


def check_horizontally(board: list) -> bool:
    """
    test horizontally
    :param board:
    :return:
    """

    for row in board:
        if sorted(row) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    return True


def check_vertically(board: list) -> bool:
    """
    test vertically
    :param board:
    :return:
    """

    i = 0
    while i < 9:
        col = []
        for row in board:
            col.append(row[i])
        if sorted(col) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
        i += 1
    return True


def check_sub_grids(board: list) -> bool:
    """
    test each of the nine 3x3 sub-grids
    (also known as blocks)
    :param board:
    :return:
    """

    sub_grids = [
        board[0][0:3] + board[1][0:3] + board[2][0:3],
        board[0][3:6] + board[1][3:6] + board[2][3:6],
        board[0][6:] + board[1][6:] + board[2][6:],

        board[3][0:3] + board[4][0:3] + board[5][0:3],
        board[3][3:6] + board[4][3:6] + board[5][3:6],
        board[3][6:] + board[4][6:] + board[5][6:],

        board[6][0:3] + board[7][0:3] + board[8][0:3],
        board[6][3:6] + board[7][3:6] + board[8][3:6],
        board[6][6:] + board[7][6:] + board[8][6:],
    ]

    for row in sub_grids:
        if sorted(row) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False

    return True
