"""
Beginner Series #3 Sum of Numbers
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def get_sum(a: int, b: int) -> int:
    """
    Given two integers a and b,
    which can be positive or negative,
    find the sum of all the numbers
    between including them too and return it.
    If the two numbers are equal return a or b.
    :param a:
    :param b:
    :return:
    """
    if a > b:
        a, b = b, a
    return sum(i for i in range(a, (b + 1)))
