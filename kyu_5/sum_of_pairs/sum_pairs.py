"""
Solution for -> Sum of Pairs
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def sum_pairs(ints: list, s: int):
    """
    Given a list of integers and a single sum value,
    returns the first two values (parse from the left please)
    in order of appearance that add up to form the sum.

    :param ints: a list of integers
    :param s: a single sum value
    :return: the first two values = s
    """
    results: dict = {}
    short_ints: list = simplify(ints)

    for indx_a, a in enumerate(short_ints):
        for indx_b, b in enumerate(short_ints):

            if indx_a != indx_b and a + b == s:
                dif = abs(indx_a - indx_b)

                if dif == 1:
                    return [a, b]

                if dif not in results:
                    results[dif] = [a, b]

    return results[min(results)] if len(results) > 0 else None


def simplify(ints: list) -> list:
    """
    In order to speed up the process we should simplify
    the input list by reducing duplicate values, see sample below:

    [1,4,5,1,1,1,1,1,4,7,8] >>> [1,4,5,1,4,7,8]

    :param ints: a list of integers
    :return: simplified list of integers
    """
    result: list = []
    temp: int = -1

    for i in ints:
        if temp != i:
            temp = i
            result.append(i)

    return result
