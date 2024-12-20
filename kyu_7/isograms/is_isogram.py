"""
Solution for -> Isograms.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def is_isogram(string: str) -> bool:
    """
    Determine whether a string that contains only letters is an 'isogram'.

    :param string: str
    :return: bool
    """
    return len(set(string.lower())) == len(string)
