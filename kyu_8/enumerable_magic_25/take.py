"""
Solution for -> Enumerable Magic #25 - Take the First N Elements
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def take(arr: list, n: int) -> list:
    """
    Accepts a list/array and a number n,
    and returns a list/array array of the
    first n elements from the list/array.

    :param arr: list
    :param n: int
    :return: list
    """
    return arr[:n]
