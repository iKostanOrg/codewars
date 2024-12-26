"""
Solution for -> Compare within margin.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def close_compare(a: float, b: float, margin: int = 0) -> int:
    """
    Return whether 'a' is lower than, close to, or higher than 'b'.

    If margin is not given, treat it as if it were zero.
    Assume: margin >= 0
    :param a: float
    :param b: float
    :param margin: int
    :return: int
    """
    # When a is close to b, return 0.
    if margin >= abs(b - a):
        return 0
    # When 'a' is less than 'b', return -1.
    if a < b:
        return -1
    # When a is greater than b, return 1.
    return  1
