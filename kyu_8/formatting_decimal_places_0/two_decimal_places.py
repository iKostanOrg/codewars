#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def two_decimal_places(n):
    """
    Each number should be formatted that it is
    rounded to two decimal places. You don't
    need to check whether the input is a valid
    number because only valid numbers are used
    in the tests.
    :param n:
    :return:
    """
    return float('{:.2f}'.format(n))
