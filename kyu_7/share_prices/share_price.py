"""
Solution for -> Share prices
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def share_price(invested: int, changes: list) -> str:
    """
    Calculates, and returns the current price of your share,
    given the following two arguments:

    1. invested(number), the amount of money you initially
    invested in the given share

    2. changes(array of numbers), contains your shares daily
    movement percentages

    The returned number, should be in string format, and it's
    precision should be fixed at 2 decimal numbers.
    :param invested: int
    :param changes: list
    :return: str
    """
    for c in changes:
        invested = invested + ((invested * c) / 100.00)

    return '{:.2f}'.format(invested)
