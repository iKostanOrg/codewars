"""
Solution for -> Third Angle of a Triangle.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def other_angle(a: int, b: int) -> int:
    """
    Calculate 3rd angle.

    You are given two angles (in degrees) of a triangle.
    Write a function to return the 3rd.
    Note: only positive integers will be tested.
    :param a:
    :param b:
    :return:
    """
    return 180 - (a + b)
