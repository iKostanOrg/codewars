"""
Solution for -> Powers of 3.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def largest_power(num: int) -> int:
    """
    Largest power function.

    Given a positive integer N,
    return the largest integer k
    such that 3^k < N.
    :param num:
    :return:
    """
    result: float = 0.0
    n: int = 0
    while result < num:
        result = 3 ** n
        if result >= num:
            n -= 1
            break
        n += 1

    return n
