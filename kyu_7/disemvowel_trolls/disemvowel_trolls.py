"""
Solution for -> 'Disemvowel' Trolls.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

VOWELS: tuple = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')


def disemvowel(string: str) -> str:
    """
    'disemvowel' function.

    A function that takes a string and return
    a new string with all vowels removed.

    For example, the string "This website is
    for losers LOL!" would become "Ths wbst s fr lsrs LL!".

    Note: for this kata y isn't considered a vowel.
    :param string:
    :return:
    """
    return ''.join(char for char in string if char not in VOWELS)
