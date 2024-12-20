"""
Solution for -> You\'re a square.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

import math


def is_square(n: int) -> bool:
    """
    Given an integral number, determine if it's a square number.

    :param n:
    :return: bool
    """
    if n > -1:
        number = math.sqrt(n)
        if (number - int(number)) == 0:
            return True
    return False
