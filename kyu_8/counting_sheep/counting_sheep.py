"""
Solution for -> Counting sheep...

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def count_sheep(array_of_sheep: list) -> int:
    """
    Count sheep.

    Consider an array of sheep where some sheep
    may be missing from their place. We need a
    function that counts the number of sheep
    present in the array (true means present).

    Hint: Don't forget to check for bad values
    like null/undefined
    :param array_of_sheep: list
    :return: int
    """
    return 0 if array_of_sheep is None \
        else array_of_sheep.count(True)
