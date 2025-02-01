"""
Solution for -> Easy Line.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

import math


def easy_line(n: int) -> int:
    """
    Easy line function.

    The function will take n (with: n>= 0) as parameter
    and will return the sum of the squares of the binomial
    coefficients with line 'n'.
    :param n: the line number (with: n>= 0)
    :return:
    """
    if n < 0:
        raise ValueError(f'ERROR: invalid n ({n}) value. n must be >= 0')

    if n == 0:
        return 1

    result: int = 0
    i: int = 0
    for row in range(n - 1, 2 * n):
        result += calc_combination_per_row_item(row, i)
        i += 1

    return result


def calc_combination_per_row_item(row: int, i: int) -> int:
    """
    Generate specific combination from Pascal's Triangle row by specified index.

    :param row: row
    :param i: index
    :return:
    """
    combination: int = (int(math.factorial(row)) //
                        (int(math.factorial(i)) *
                         int(math.factorial(row - i))))
    return combination
