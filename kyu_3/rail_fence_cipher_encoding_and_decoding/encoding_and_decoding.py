#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan


def get_rails(string: str, n: int) -> list:
    """
    Create rails matrix.

    :param string: a string
    :param n: the number of rails
    :return: rails matrix
    """

    rails: list = list()
    while len(rails) != n:
        rails.append(list())

    row = 0
    down = True
    for char in string:

        for char_index in range(0, n):
            if char_index != row:
                rails[char_index].append("")
            else:
                rails[char_index].append(char)

        if row == n - 1 and down:
            down = False

        if row == 0 and not down:
            down = True

        if down:
            row += 1
        else:
            row -= 1

    return rails


def encode_rail_fence_cipher(string: str, n: int) -> str:
    """
    This cipher is used to encode a string by placing each character
    successively in a diagonal along a set of "rails". First start off
    moving diagonally and down. When you reach the bottom, reverse
    direction and move diagonally and up until you reach the top rail.
    Continue until you reach the end of the string. Each "rail" is then
    read left to right to derive the encoded string.

    :param string: a string
    :param n: the number of rails
    :return: the ENCODED string
    """
    rails: list = get_rails(string, n)
    return ''.join(''.join(row) for row in rails)


def decode_rail_fence_cipher(string: str, n: int) -> str:
    """
    Function/method that takes 2 arguments, an encoded string
    and the number of rails, and returns the DECODED string.

    :param string: an encoded string
    :param n: the number of rails
    :return: the DECODED string
    """
    rails: list = get_rails(''.join(['_'] * len(string)), n)

    # populate chars from string in to a target matrix/rail
    char_index = 0
    for row_i, row in enumerate(rails):
        for col_i, column in enumerate(row):
            if column == '_':
                rails[row_i][col_i] = string[char_index]
                char_index += 1

    # decode string based on rail
    result: list = list()
    char_index = 0
    while len(result) != len(string):
        for row in rails:
            if char_index < len(row) and row[char_index] != '':
                result.append(row[char_index])
                char_index += 1

    return ''.join(result)
