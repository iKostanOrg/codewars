"""
Century From Year

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def century(year):
    """
    Given a year, return the century it is in
    :param year:
    :return:
    """

    if year % 100 == 0:
        return year // 100

    return (year // 100) + 1
