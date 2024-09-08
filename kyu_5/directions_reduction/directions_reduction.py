"""
Solution for -> Directions Reduction
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

PAIRS: dict = {
    "NORTH": "SOUTH",
    "SOUTH": "NORTH",
    "EAST": "WEST",
    "WEST": "EAST",
}


def dir_reduc(arr: list) -> list:
    """
    A function dir_reduc which will take an array of strings
    and returns an array of strings with the needless
    directions removed (W<->E or S<->N side by side).

    The Haskell version takes a list of directions with data
    Direction = North | East | West | South.

    The Clojure version returns nil when the path is reduced
    to nothing.

    The Rust version takes a slice of enum Direction
    {NORTH, SOUTH, EAST, WEST}.
    :param arr: lst
    :return: lst
    """

    is_sorted: bool = False

    while not is_sorted:
        is_sorted = True
        for i, a in enumerate(arr):
            if check_pairs(i, arr, a):
                del_directions(i, arr)
                is_sorted = False
                break

    return arr


def check_pairs(i: int, arr: list, a: str) -> bool:
    """
    Check conditions
    :param i: int
    :param arr: list
    :param a: str
    :return: bool
    """
    return i + 1 < len(arr) and PAIRS[a] == arr[i + 1]


def del_directions(i: int, arr: list) -> None:
    """
    Delete array members
    :param i: int
    :param arr:list
    :return: None
    """
    del arr[i + 1]
    del arr[i]
