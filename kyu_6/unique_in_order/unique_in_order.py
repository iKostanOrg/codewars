"""
Test for -> Unique In Order.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

from typing import Iterable, List


def unique_in_order(iterable: Iterable) -> list:
    """
    Unique In Order.

    Takes as argument a sequence and returns a list
    of items without any elements with the same value
    next to each other and preserving the original
    order of elements.
    :param iterable:
    :return:
    """
    result: list = []
    for i in iterable:
        if len(result) == 0 or i != result[-1]:
            result.append(i)
    return result
