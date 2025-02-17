"""
Solution for -> Duplicate Encoder.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def duplicate_encode(word: str) -> str:
    """
    Duplicate Encoder.

    Converts a string to a new string where each
    character in the new string is "(" if that
    character appears only once in the original
    string, or ")" if that character appears more
    than once in the original string.

    Ignore capitalization when determining if
    a character is a duplicate.
    :param word:
    :return:
    """
    result: str = ''
    word = ''.join(char.lower() for char in word)

    for char in word:
        if word.count(char) > 1:
            result += ')'
        else:
            result += '('

    return result
