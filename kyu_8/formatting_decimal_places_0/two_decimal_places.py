"""
Solution for -> Formatting decimal places #0
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def two_decimal_places(n: float) -> float:
    """
    Each number should be formatted that it is
    rounded to two decimal places. You don't
    need to check whether the input is a valid
    number because only valid numbers are used
    in the tests.
    :param n: float
    :return: float
    """
    return float(f'{n:.2f}')
