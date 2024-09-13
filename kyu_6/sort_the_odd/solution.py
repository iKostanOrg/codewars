"""
Solution for -> Sort the odd
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def sort_array(source_array: list) -> list:
    """
    Sorting ascending odd numbers but even
    numbers must be on their places.

    Zero isn't an odd number and you don't
    need to move it. If you have an empty array,
    ou need to return it.

    :param source_array:
    :return:
    """
    output: list = source_array[:]
    is_sorted: bool = False

    while not is_sorted:
        is_sorted = True
        for i_o, o in enumerate(output):
            conditions_o: tuple = (output[i_o] != 0,
                                   output[i_o] % 2 != 0)
            if all(conditions_o):
                for i_b, b in enumerate(output):
                    conditions_b: tuple = (output[i_b] != 0,
                                           output[i_b] % 2 != 0,
                                           output[i_o] > output[i_b],
                                           i_o < i_b)
                    if all(conditions_b):
                        is_sorted = False
                        output[i_o], output[i_b] = b, o
                        break

    return output
