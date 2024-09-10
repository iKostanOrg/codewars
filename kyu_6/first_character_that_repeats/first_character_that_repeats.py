"""
Solution for -> First character that repeats
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def first_dup(s: str) -> (str, None):
    """
    Find the first character that repeats
    in a String and return that character.
    :param s: str
    :return: str, None
    """
    for char in s:
        if s.count(char) > 1:
            return char
    return None
