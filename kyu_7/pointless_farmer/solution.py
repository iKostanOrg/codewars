"""
Solution for -> Pointless Farmer.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

from typing import Any


def buy_or_sell(pairs: list, harvested_fruit: str) -> list[Any]:
    """
    Decide which direction to trade.

    :param pairs: list
    :param harvested_fruit: str
    :return:
    """
    currently_holding: str = harvested_fruit
    results: list = []

    for pair in pairs:
        currently_holding = make_deal(results, pair, currently_holding)
        if currently_holding:
            continue

        return "ERROR"

    return "ERROR" if currently_holding != harvested_fruit else results


def make_deal(results: list, pair: tuple, currently_holding: str) -> str:
    """
    Buy or sell.

    Return an empty string if no deal made.
    :param results: list
    :param pair: tuple
    :param currently_holding: str
    :return: str
    """
    # First item in pairs is for selling.
    if pair[-1] == currently_holding:
        results.append('sell')
        return pair[0]
    # Second is for buying.
    if pair[0] == currently_holding:
        results.append('buy')
        return pair[-1]

    return ''
