"""
Test for -> Sums of Parts.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def parts_sums(input_ls: list) -> list:
    """
    Sum of Parts.

    The function parts_sums will take as parameter a list input_ls
    and return a list of the sums of its parts.
    :param input_ls:
    :return:
    """
    # empty list should return 0
    if not input_ls:
        return [0]

    result: list = []
    ls_sum: int = sum(input_ls)
    result.append(ls_sum)

    for num in input_ls:
        current_sum: int = ls_sum - num
        result.append(current_sum)
        ls_sum = current_sum

    return result
