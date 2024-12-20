"""
Solution for -> Computer problem series #1: Fill the Hard Disk Drive.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def save(sizes: list, hd: int) -> int:
    """
    'Save' function.

    Your task is to determine how many files of the
    copy queue you will be able to save into your
    Hard Disk Drive.

    Input:
    Array of file sizes (0 <= s <= 100)
    Capacity of the HD (0 <= c <= 500)

    Output:
    Number of files that can be fully saved in the HD

    :param sizes: list
    :param hd: int
    :return: int
    """
    counter: int = 0
    total: int = 0

    for size in sizes:
        total += size
        counter += 1

        if total > hd:
            counter -= 1
            break

    return counter
