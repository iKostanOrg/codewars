"""
Solution for -> V A P O R C O D E
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def vaporcode(s: str) -> str:
    """
    function that converts any sentence
    into a V A P O R W A V E sentence
    :param s:
    :return:
    """
    return '  '.join(char.upper() for char in s if char != ' ')
