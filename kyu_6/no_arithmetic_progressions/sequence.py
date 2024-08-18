"""
Solution for -> No arithmetic progressions
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


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
    return 0


def sum_of_arithmetic_progression(a: int, dif: int, terms: int = 3) -> int:
    # Sum of an Arithmetic Progression
    return terms * (a + general_term_of_arithmetic_progression(a, dif)) // 2


def general_term_of_arithmetic_progression(a: int, dif: int, terms: int = 3) -> int:
    # General Term of an Arithmetic Progression
    return a + (terms - 1) * dif
