"""
Solution for -> The museum of incredible dull things.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def remove_smallest(numbers: list) -> list:
    """
    Remove the smallest function.

    Given an array of integers, remove the smallest value.
    Do not mutate the original array/list. If there are multiple
    elements with the same value, remove the one with a lower index.
    If you get an empty array/list, return an empty array/list.

    Don't change the order of the elements that are left.
    :param numbers: list
    :return: list
    """
    new_array: list = []
    if len(numbers) < 1:
        return numbers

    min_num: int = min(numbers)
    min_i: int = numbers.index(min_num)
    for i, el in enumerate(numbers):
        if i != min_i:
            new_array.append(el)

    return new_array
