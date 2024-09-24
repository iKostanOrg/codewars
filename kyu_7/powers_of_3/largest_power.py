"""
Solution for -> Powers of 3
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def largestPower(N: int) -> int:
    """
    Given a positive integer N,
    return the largest integer k
    such that 3^k < N.
    :param N:
    :return:
    """
    result: int = 0
    n: int = 0
    while result < N:
        result = 3 ** n
        if result >= N:
            n -= 1
            break
        n += 1

    return n
