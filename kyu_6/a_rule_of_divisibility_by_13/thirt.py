"""
Solution for -> A Rule of Divisibility by 13
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

REMAINDERS = (1, 10, 9, 12, 3, 4)


def thirt(n: int) -> int:
    """
    The function which processes this sequence of operations
    on an integer n (>=0). `thirt` will return the stationary number.
    :param n: int
    :return: int
    """
    while True:
        i: int = 0
        temp: int = 0
        t = str(n)[::-1]
        for s in t:
            temp += int(s) * REMAINDERS[i]
            if i + 1 < len(REMAINDERS):
                i += 1
            else:
                i = 0

        if int(n) == temp:
            return temp

        n = temp
