"""
Solution for -> Grasshopper - Summation
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def summation(num: int) -> int:
    """
    A program that finds the summation of every
    number from 1 to num.
    The number will always be a positive
    integer greater than 0.
    :param num:
    :return:
    """
    result: int = 0
    for i in range(1, num + 1):
        result += i

    return result
