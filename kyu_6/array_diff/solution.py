"""
Solution for -> Array.diff.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def array_diff(a: list, b: list) -> list:
    """
    Difference function, which subtracts one
    list from another and returns the result.

    :param a: list a
    :param b: list b
    :return: diff between a and b
    """
    return [item for item in a if item not in b]
