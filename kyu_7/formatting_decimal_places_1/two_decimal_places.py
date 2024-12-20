"""
Test for -> Formatting decimal places #1.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def two_decimal_places(number) -> float:
    """
    Formatting decimal places #1.

    Each floating-point number should be formatted that
    only the first two decimal places are returned.

    You don't need to check whether the input is a valid
    number because only valid numbers are used in the tests.

    Don't round the numbers! Just cut them after two decimal
    places!
    :param number:
    :return: float
    """
    number_str: str = str(number)
    return float(number_str[0:number_str.index('.') + 3])
