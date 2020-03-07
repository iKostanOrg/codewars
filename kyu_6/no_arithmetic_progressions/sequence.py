#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def sequence(n: int) -> int:
    """
    A function f(n), which returns the n-th member of sequence.

    Consider a sequence, which is formed by the following rule:
    next term is taken as the smallest possible non-negative integer,
    which is not yet in the sequence, so that no 3 terms of sequence
    form an arithmetic progression.

    Example:
        f(0) = 0 -- smallest non-negative
        f(1) = 1 -- smallest non-negative, which is not yet in the sequence
        f(2) = 3 -- since 0, 1, 2 form an arithmetic progression
        f(3) = 4 -- neither of 0, 1, 4, 0, 3, 4, 1, 3, 4 form an arithmetic
                    progression, so we can take smallest non-negative, which is larger than 3
        f(4) = 9 -- 5, 6, 7, 8 are not good, since 1, 3, 5, 0, 3, 6, 1, 4, 7, 0, 4, 8
                    are all valid arithmetic progressions.
    :param n:
    :return:
    """
    pass


def Nth_of_AP(a, d, N):
    """
    Python 3 Program to find nth
    term of Arithmetic progression

    Using formula to find the
    Nth term t(n) = a(1) + (n-1)*d

    Driver code
        a = 2  # starting number
        d = 1  # Common difference
        N = 5  # N th term to be find

    :param a:
    :param d:
    :param N:
    :return:
    """
    return a + (N - 1) * d


def is_arithmetic(arr: list) -> bool:
    """
    Check a sequence of numbers is an
    arithmetic progression or not

    :param arr:
    :return:
    """
    delta = arr[1] - arr[0]
    for index in range(len(delta) - 1):
        if not (arr[index + 1] - arr[index] == delta):
            return False
    return True
