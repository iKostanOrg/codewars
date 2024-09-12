"""
Solution for Casino chips
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def solve(arr: list) -> int:
    """
    You are given three piles of casino chips: white, green and black
    chips:

        the first pile contains only white chips
        the second pile contains only green chips
        the third pile contains only black chips

    Each day you take exactly two chips of different colors and head to
    the casino. You can chose any color, but you are not allowed to take
    two chips of the same color in a day.

    You will be given an array representing the number of chips of each
    color and your task is to return the maximum number of days you can
    pick the chips. Each day you need to take exactly two chips.

    :param arr:
    :return:
    """

    arr: list = sorted(arr)

    if arr[0] + arr[1] <= arr[2]:
        return arr[0] + arr[1]
    else:
        return sum(arr) // 2

