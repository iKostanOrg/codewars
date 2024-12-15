"""
Solution for -> Moving Zeros To The End.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def move_zeros(array: list) -> list:
    """
    move_zeros function.

    An algorithm that takes an array and moves all of the
    zeros to the end, preserving the order of the other elements.
    :param array: list
    :return: list
    """
    moving_zero: bool = True

    while moving_zero:
        moving_zero = False

        for i, a in enumerate(array):
            if a == 0 and array[i:].count(0) != len(array[i:]) and a is not False:
                del array[i]
                array.append(0)
                moving_zero = True
                break

    return array
