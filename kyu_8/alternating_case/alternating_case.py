"""
altERnaTIng cAsE <=> ALTerNAtiNG CaSe

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def to_alternating_case(string: str) -> str:
    """
    each lowercase letter becomes uppercase and
    each uppercase letter becomes lowercase
    :param string:
    :return:
    """
    return ''.join((char.upper() if char.islower() else char.lower()) for char in string)
