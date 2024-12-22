"""
altERnaTIng cAsE <=> ALTerNAtiNG CaSe.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def to_alternating_case(string: str) -> str:
    """
    Alternating case.

    Each lowercase letter becomes uppercase and
    each uppercase letter becomes lowercase.
    :param string: str
    :return: str
    """
    return ''.join((char.upper() if char.islower() else char.lower()) for char in string)
