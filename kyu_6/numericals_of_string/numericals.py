"""
Solution for -> Numericals of a String
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def numericals(s: str) -> str:
    """
    For each symbol in the string if it's the
    first character occurrence, replace it with
    a '1', else replace it with the amount of
    times you've already seen it.
    :param s:
    :return:
    """
    char_dict: dict = {}
    result: str = ''

    for char in s:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
        result += str(char_dict[char])

    return result
