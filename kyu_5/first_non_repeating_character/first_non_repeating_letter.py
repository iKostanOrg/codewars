"""
Solution for -> First non-repeating character
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def first_non_repeating_letter(string: str) -> str:
    """
    A function named first_non_repeating_letter that
    takes a string input, and returns the first
    character that is not repeated anywhere in the string.
    :param string: str
    :return: str
    """
    result: str = ''
    string_lower: str = string.lower()

    for i, s in enumerate(string_lower):
        if string_lower.count(s) == 1:
            return string[i]

    return result
