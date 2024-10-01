"""
Solution for -> Find the first non-consecutive number
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def first_non_consecutive(arr: list) -> int:
    """
    Find the first element of an array that is not consecutive.

    E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3
    then 4 are all consecutive but 6 is not,
    so that's the first non-consecutive number.

    If the whole array is consecutive then return null or Nothing.
    :param arr: list
    :return: int
    """
    for index, n in enumerate(arr):
        if index + 1 < len(arr) and n + 1 != arr[index + 1]:
            return arr[index + 1]
