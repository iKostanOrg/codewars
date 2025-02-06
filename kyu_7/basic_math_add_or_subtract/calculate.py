"""
Solution for -> Basic Math (Add or Subtract).

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

from asteval import Interpreter

aeval = Interpreter()

CONVERSION: dict = {
    'plus': '+',
    'minus': '-'}


def calculate(s: str) -> str:
    """
    Perform addition and subtraction on a given string.

    :param s: str
    :return: str
    """
    s = string_to_math(s)
    # pylint: disable=W0123
    # Evaluate a simple mathematical expression using
    # Python's built-in eval (safe subset).
    # allowed_names = {"__builtins__": None}
    # return f'{eval(s, {"__builtins__": None}, allowed_names)}'  # nosec B311
    return f'{aeval.eval(s)}'  # nosec B311
    # pylint: enable=W0123


def string_to_math(s: str) -> str:
    """
    Convert into simple arithmetic expression.

    :param s: str
    :return: str
    """
    s = s.lower().replace(' ', '')
    for key, item in CONVERSION.items():
        if key in s:
            s = s.replace(key, item)
    return s
