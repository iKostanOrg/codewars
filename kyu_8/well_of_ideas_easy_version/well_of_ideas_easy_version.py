"""
Solution for -> Well of Ideas - Easy Version.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

from typing import List


def well(x: List[str]) -> str:
    """
    'well' function

    :param x: List[str]
    :return: str
    """
    counter: int = sum(1 for i in x if i.lower() == 'good')
    result: str = ''

    if counter == 0:
        result = 'Fail!'

    if 0 < counter < 3:
        result = 'Publish!'

    if counter > 2:
        result = 'I smell a series!'

    return result
