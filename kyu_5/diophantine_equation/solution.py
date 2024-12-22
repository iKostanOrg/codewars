"""
Solution for -> Diophantine Equation.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def sol_equa(n: int) -> list:
    """
    Diophantine Equation solution.

    Finds all integers x, y (x >= 0, y >= 0)
    solutions of a diophantine equation of the form x2 - 4 * y2 = n
    :param n: int
    :return: list
    """
    result: list = []

    start = n//2
    if n % 2 != 0:
        start = n // 2 + 1

    for x in range(start, 0, -2):
        for y in range(x//2, -1, -1):
            if (x - 2 * y) * (x + 2 * y) == n:
                result.append([x, y])
                break

    return result
