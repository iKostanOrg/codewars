"""
Solution for -> My head is at the wrong end!
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def fix_the_meerkat(arr: list) -> list:
    """
    You will be given an array which will have
    three values (tail, body, head).
    It is your job to re-arrange the array so
    that the animal is the right way round
    (head, body, tail).
    :param arr:
    :return:
    """
    return arr[::-1]
