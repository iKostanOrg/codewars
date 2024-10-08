"""
Solution for -> Century From Year
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def century(year: int) -> int:
    """
    Given a year, return the century it is in
    :param year: int
    :return: int
    """
    if year % 100 == 0:
        return year // 100

    return (year // 100) + 1
