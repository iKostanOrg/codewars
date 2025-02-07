"""
Solution for -> Always perfect.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

import math
from typing import List


def check_root(string: str) -> str:
    """
    Check root.

    A function which takes numbers separated by commas
    in string format and returns the number which is a
    perfect square and the square root of that number.

    If string contains other characters than number or
    it has more or less than 4 numbers separated by comma
    function returns "incorrect input".

    If string contains 4 numbers but not consecutive it
    returns "not consecutive".
    :param string:
    :return:
    """
    string_arr: List = string.split(',')
    if len(string_arr) != 4:
        return 'incorrect input'

    try:
        string_arr = list(int(char) for char in string_arr)
    except ValueError:
        return 'incorrect input'

    result: int = 1
    for s in string_arr:
        result *= s

    result += 1
    root: float = math.sqrt(result)

    if root % 1 == 0:
        return f'{result}, {int(root)}'

    return 'not consecutive'
