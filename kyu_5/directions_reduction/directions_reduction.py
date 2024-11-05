"""
Solution for -> Directions Reduction
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

PAIRS: dict = {
    "NORTH": "SOUTH",
    "SOUTH": "NORTH",
    "EAST": "WEST",
    "WEST": "EAST"}


def dir_reduc(arr: list) -> list:
    """
    A function dir_reduc which will take an array of strings
    and returns an array of strings with the needless
    directions removed (W<->E or S<->N side by side).

    The Haskell version takes a list of directions with data
    Direction = North | East | West | South.

    :param arr: list
    :return: list
    """
    is_sorted: bool = False

    while not is_sorted:
        is_sorted = check_pairs(arr)

    return arr


def check_pairs(arr: list) -> bool:
    """
    Check conditions for pairs.
    Return False if any pairs were removed.
    Return True if there was nothing to remove.
    :param arr: list
    :return: bool
    """
    for i, arr_item in enumerate(arr):
        if i + 1 < len(arr) and PAIRS[arr_item] == arr[i + 1]:
            del_directions(i, arr)
            return False
    return True


def del_directions(i: int, arr: list) -> None:
    """
    Remove directions from the list
    :param i: int
    :param arr:list
    :return: None
    """
    del arr[i + 1]
    del arr[i]
