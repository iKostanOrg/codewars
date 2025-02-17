"""
Solution for -> Pyramid Array.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def pyramid(n: int) -> list:
    """
    Pyramid function.

    Write a function that when given a number >= 0,
    returns an Array of ascending length subarrays.

    Note: the subarrays should be filled with 1s
    :param n: int
    :return: list
    """
    result: list = []
    if n is None or n == 0:
        return result

    for i in range(1, n + 1):
        result.append([1] * i)

    return result
