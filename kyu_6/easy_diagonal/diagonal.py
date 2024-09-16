"""
Solution for -> Easy Diagonal
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

import math


def diagonal(n: int, p: int) -> int:
    """
    We want to calculate the sum of the binomial coefficients on a given diagonal.
    The sum on diagonal 0 is 8 (we'll write it S(7, 0), 7 is the number of the line
    where we start, 0 is the number of the diagonal).
    In the same way S(7, 1) is 28, S(7, 2) is 56.

    :param n: n is the line where we start and
    :param p: p is the number of the diagonal
    :return: the sum of the binomial coefficients on a given diagonal
    """
    if n < 0:
        raise ValueError('ERROR: invalid n ({}) value. n must be >= 0')

    if p < 0:
        raise ValueError('ERROR: invalid p ({}) value. p must be >= 0')

    result: int = math.factorial(
        n + 1) // (math.factorial(p + 1) * math.factorial(n - p))

    return result
