"""
Solution for -> The First Non Repeated Character In A String
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def first_non_repeated(s: str) -> (str, None):
    """
    You need to write a function, that returns the
    first non-repeated character in the given string.

    For example for string "test" function should return 'e'.
    For string "teeter" function should return 'r'.

    If a string contains all unique characters, then return
    just the first character of the string.
    Example: for input "trend" function should return 't'

    You can assume, that the input string has always
    non-zero length.
    :param s:
    :return:
    """
    for char in s:
        if s.count(char) == 1:
            return char
    return None
