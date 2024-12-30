"""
Solution for -> Pointless Farmer.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def buy_or_sell(pairs: list, harvested_fruit: str) -> str | list:
    """
    Decide which direction to trade.

    :param pairs: list
    :param harvested_fruit: str
    :return: list
    """
    currently_holding: str = harvested_fruit
    results: list = []

    for pair in pairs:
        # First item in pairs is for selling.
        if pair[-1] == currently_holding:
            results.append('sell')
            currently_holding = pair[0]
            continue
        # Second is for buying.
        if pair[0] == currently_holding:
            results.append('buy')
            currently_holding = pair[-1]
            continue

        return "ERROR"

    return "ERROR" if currently_holding != harvested_fruit else results
