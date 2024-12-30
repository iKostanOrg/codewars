"""
Solution for -> Pointless Farmer.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

from typing import Any


def buy_or_sell(pairs: list, harvested_fruit: str) -> list[Any] | str:
    """
    Decide which direction to trade.

    :param pairs: list
    :param harvested_fruit: str
    :return: list
    """
    currently_holding: str = harvested_fruit
    results: list = []

    for pair in pairs:
        # First item in pairs is for selling, second is for buying.
        if pair[0] == currently_holding == pair[-1] or pair[-1] == currently_holding:
            results.append('sell')
            currently_holding = pair[0]
        elif pair[0] == currently_holding:
            results.append('buy')
            currently_holding = pair[-1]
        else:
            return "ERROR"

    return results if currently_holding == harvested_fruit else "ERROR"
