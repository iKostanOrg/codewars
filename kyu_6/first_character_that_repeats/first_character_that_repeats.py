"""
Solution for -> First character that repeats
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def first_dup(word: str) -> str | None:
    """
    Find the first character that repeats
    in a String and return that character.
    :param word: str
    :return: str, None
    """
    for char in word:
        if word.count(char) > 1:
            return char
    return None
