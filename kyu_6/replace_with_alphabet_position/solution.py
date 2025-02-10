"""
Solution for -> Replace With Alphabet Position

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

import string

alphabet: str = string.ascii_lowercase


def alphabet_position(text: str) -> str:
    """
	Replace every letter with its position in the alphabet.

	:param text: str
	:return: str
    """
    return ' '.join([str(alphabet.index(char.lower()) + 1) for char in text if char.isalpha()])
