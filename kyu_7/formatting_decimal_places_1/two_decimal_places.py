"""
Test for -> Formatting decimal places #1.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def two_decimal_places(number) -> float:
    """
    Format decimal places #1.

    Each floating-point number should be formatted that
    only the first two decimal places are returned.
    :param number:
    :return: float
    """
    number_str: str = str(number)
    return float(number_str[0:number_str.index('.') + 3])
