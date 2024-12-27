"""
Test for -> A Strange Trip to the Market.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

INDICATIONS: list = ['tree fiddy', 'three fifty', '3.50', ]

def is_loch_ness_monster(string: str) -> bool:
    """
    Return true if you're talking with 'The Loch Ness Monster', false otherwise.

    :param string: str
    :return: bool
    """
    # A) it is a 400-foot tall beast from the paleolithic era;
    # B) it will ask you for tree fiddy.
    return any([True for s in INDICATIONS if s in string.lower()])
