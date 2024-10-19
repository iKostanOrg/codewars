"""
Solution for -> Messi goals function
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def goals(la_liga: int, copa_delrey: int, champions_league: int) -> int:
    """
    The function returns Messi's total number
    of goals in all three leagues:
    - LaLiga
    - Copa del Rey
    - Champions

    :param la_liga: int
    :param copa_delrey: int
    :param champions_league: int
    :return: int
    """
    return la_liga + copa_delrey + champions_league
