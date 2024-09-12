"""
Solution for -> Count letters in string
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def letter_count(s: str) -> dict:
    """
    Count lowercase letters in a given string
    and return the letter count in a hash with
    'letter' as key and count as 'value'.
    :param s:
    :return:
    """

    result: dict = dict()

    for char in s:
        if char.islower():
            if char not in result:
                result[char] = 1
            else:
                result[char] += 1

    return result
