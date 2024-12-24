"""
Solution for -> Remove First and Last Character.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def remove_char(s: str) -> str:
    """
    Remove the first and last characters of a string.

    You're given one parameter, the original string.
    You don't have to worry with strings with less than two characters.
    :param s: str
    :return: str
    """
    return s[1:-1]
