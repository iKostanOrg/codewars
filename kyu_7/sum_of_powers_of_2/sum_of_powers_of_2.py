"""
Solution for -> Sum of powers of 2
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

from typing import List


def powers(n: int) -> list:
    """
    Return an array of numbers
    (that are a power of 2)
    for which the input "n" is the sum
    :param n:
    :return:
    """
    lst: list = []
    power: int = 0

    while (2 ** power) <= n:
        lst.append(2 ** power)
        power += 1

    i: int = -1
    result: List[int] = []

    while sum(result) != n:
        if sum(result) + lst[i] <= n:
            result.append(lst[i])
        i -= 1

    return sorted(result)
