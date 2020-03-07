#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from typing import Iterable, List


def unique_in_order(iterable: Iterable) -> list:
    """
    Takes as argument a sequence and returns a list
    of items without any elements with the same value
    next to each other and preserving the original
    order of elements.
    :param iterable:
    :return:
    """

    result: List = []

    for i in iterable:

        if len(result) == 0 or i != result[-1]:
            result.append(i)

    return result
