#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def odd_row(n: int) -> list:
    """
    Given a triangle of consecutive odd numbers
    finds the triangle's row knowing its index
    (the rows are 1-indexed).
    :param n:
    :return:
    """
    row = list()

    number = calc_first_number(n)
    last = calc_last_number(n)

    while number <= last:
        row.append(number)
        number += 2

    return row


def calc_first_number(n: int) -> int:
    """
    Calculate first number in the row
    :param n:
    :return:
    """
    return (n * (n - 1)) + 1


def calc_last_number(n: int) -> int:
    """
    Calculate last number in the row
    :param n:
    :return:
    """
    return (n * n) + (n - 1)
