"""
Solution for -> Basic Math (Add or Subtract)
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


CONVERSION: dict = {
    'plus': '+',
    'minus': '-'}


def calculate(s: str) -> str:
    """
    Perform addition and subtraction on a given string
    :param s: str
    :return: str
    """
    s: str = s.lower()
    for key in CONVERSION:
        if key in s:
            s = s.replace(key, CONVERSION[key])

    return str(eval(s))
