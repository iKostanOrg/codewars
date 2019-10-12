"""Beginner Series #3 Sum of Numbers"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def get_sum(a, b):
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

    nums = range(a, (b + 1))
    return sum(nums)
