"""
Solution for -> Sum of odd numbers.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def odd_row(n: int) -> list:
    """
    Find odd row.

    Given a triangle of consecutive odd numbers
    finds the triangle's row knowing its index
    (the rows are 1-indexed).
    :param n:
    :return:
    """
    # pylint: disable-msg=R0801
    row: list = []
    number: int = calc_first_number(n)
    last: int = calc_last_number(n)
    # pylint: enable-msg=R0801
    while number <= last:
        row.append(number)
        number += 2

    return row


def calc_first_number(n: int) -> int:
    """
    Calculate first number in the row.

    :param n:
    :return:
    """
    return (n * (n - 1)) + 1


def calc_last_number(n: int) -> int:
    """
    Calculate last number in the row.

    :param n:
    :return:
    """
    return (n * n) + (n - 1)


def row_sum_odd_numbers(n: int) -> int:
    """
    Sum of odd numbers function.

    :param n:
    :return:
    """
    return sum(odd_row(n))
