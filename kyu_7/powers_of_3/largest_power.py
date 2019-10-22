#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def largestPower(N: int) -> int:
    """
    Given a positive integer N,
    return the largest integer k
    such that 3^k < N.
    :param N:
    :return:
    """

    result = 0
    n = 0
    while result < N:
        result = 3 ** n
        if result >= N:
            return n - 1
        n += 1
