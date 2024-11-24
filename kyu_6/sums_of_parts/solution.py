"""
Test for -> Sums of Parts
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def parts_sums(ls: list) -> list:
    """
    The function parts_sums will take as parameter a list ls
    and return a list of the sums of its parts.
    :param ls:
    :return:
    """
    # empty list should return 0
    if not ls:
        return [0]

    result: list = []
    ls_sum: int = sum(ls)
    result.append(ls_sum)

    for num in ls:
        n = ls_sum - num
        result.append(n)
        ls_sum = n

    return result
