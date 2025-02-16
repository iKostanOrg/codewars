"""
Solution for -> Basic Math (Add or Subtract).

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ASTEVAL is a safe(ish) evaluator of Python expressions
# and statements, using Python’s ast module. The idea is
# to provide a simple, safe, and robust miniature mathematical
# language that can handle user input. The emphasis here is on
# mathematical expressions so that many functions from numpy
# are imported and used if available.
from asteval import Interpreter
from asteval.astutils import ExceptionHolder

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
    result = aeval.eval(s)
    return f'{result}'  # nosec B311
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
