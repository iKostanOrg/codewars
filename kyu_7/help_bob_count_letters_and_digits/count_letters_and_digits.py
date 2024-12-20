"""
Solution for -> Help Bob count letters and digits.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def count_letters_and_digits(s: str) -> int:
    """
    Determine how many letters and digits are in a given string.

    :param s:
    :return:
    """
    result: int = 0

    for char in s:
        if char.isalpha() or char.isdigit():
            result += 1

    return result
