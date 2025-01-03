"""
Solution for -> Grasshopper - Terminal game move function.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def move(position: int, roll: int) -> int:
    """
    'move' function.

    A function for the terminal game that takes
    the current position of the hero and the roll
    (1-6) and return the new position.
    :param position: int
    :param roll: int
    :return: int
    """
    return position + (roll * 2)
