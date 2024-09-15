"""
Solution for -> Color Choice
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

from math import factorial


def checkchoose(m: int, n: int) -> int:
    """
    Knowing m (number of posters to design), knowing n
    (total number of available colors), search x
    (number of colors for each poster so that each poster
    has a unique combination of colors and the number of
    combinations is exactly the same as the number of posters).
    :param m:
    :param n:
    :return:
    """

    for x in range(1, n + 1):

        temp: int = factorial(n) // (factorial(x) * factorial(n - x))

        if m == temp and n != x:
            return x

        if m == temp and n == x:
            return 0

    return -1
