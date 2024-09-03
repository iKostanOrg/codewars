"""
Test for -> Josephus Survivor
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def josephus_survivor(n) -> int:
    """
    Return who is the "survivor"
    :param n:
    :return:
    """
    n_list = [i for i in range(1, n + 1)]
    return n_list[0]
