"""
Solution for -> Find the in-between point.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

import math


def middle_point(*args) -> int:
    """
    Return 1, 2, or 3 to indicate which point is the in-between one.

    :param args: 3 sets of 3D coordinates.
    :return: int, middle point.
    """
    # Set 3D coordinates
    a: tuple = args[0][:3]
    b: tuple = args[0][3:6]
    c: tuple = args[0][6:]

    # Calculate distances
    a_b: float = distance_between_two_points(a, b)
    a_c: float = distance_between_two_points(a, c)
    b_c: float = distance_between_two_points(b, c)

    if a_c < b_c and a_b < b_c:
        return 1

    return 2 if a_b < a_c and b_c < a_c else 3


def distance_between_two_points(a: tuple, b: tuple) -> float:
    """
    Return distance between two points on a 3D coordinate.

    :param a: tuple
    :param b: tuple
    :return: float
    """
    return math.sqrt((b[2] - a[2]) ** 2 + (b[1] - a[1]) ** 2 + (b[0] - a[0]) ** 2)
