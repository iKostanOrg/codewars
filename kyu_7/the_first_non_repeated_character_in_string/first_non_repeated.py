"""
Solution for -> The First Non Repeated Character In A String.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def first_non_repeated(s: str) -> str | None:
    """
    Return the first non-repeated character in the given string.

    :param s:
    :return:
    """
    for char in s:
        if s.count(char) == 1:
            return char
    return None
