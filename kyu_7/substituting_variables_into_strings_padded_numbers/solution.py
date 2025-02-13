"""
Test for -> Substituting Variables Into Strings: Padded Numbers.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def solution(value: int) -> str:
    """
    Complete the solution so that it returns a formatted string.

    The return value should equal "Value
    is VALUE" where value is a 5 digit
    padded number.
    :param value: int
    :return: str
    """
    result: str = str(value)
    while len(result) != 5:
        result = '0' + result

    return f'Value is {result}'
