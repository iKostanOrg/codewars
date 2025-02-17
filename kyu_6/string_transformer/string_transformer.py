"""
Test for -> String transformer.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def string_transformer(s: str) -> str:
    """
    Transform string.

    Given a string, return a new string that has
    transformed based on the input:

    1. Change case of every character, ie. lower
    case to upper case, upper case to lower case.

    2. Reverse the order of words from the input.

    Note: You will have to handle multiple spaces, and
    leading/trailing spaces.

    You may assume the input only contain English
    alphabet and spaces.
    :param s: str
    :return: str
    """
    s_arr: list = s.split(' ')[::-1]
    for i, word in enumerate(s_arr):
        s_arr[i] = ''.join((char.upper() if char.islower()
                            else char.lower()) for char in word)

    return ' '.join(s_arr)
