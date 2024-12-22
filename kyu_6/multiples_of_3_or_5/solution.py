"""
Solution for -> Multiples of 3 or 5.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def solution(number: int) -> int:
    """
    Solution for 'ultiples of 3 or 5' problem.

    If we list all the natural numbers below 10 that are
    multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of
    these multiples is 23.

    Finish the solution so that it returns the sum of all
    the multiples of 3 or 5 below the number passed in.
    :param number:
    :return:
    """
    result: int = 0
    for n in range(1, number):
        if n % 3 == 0 or n % 5 == 0:
            result += n

    return result
