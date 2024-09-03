"""
Solution for -. Permutations

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def permutations(string: str) -> list:
    """
    creates all permutations of an input string and
    remove duplicates, if present. This means, you
    have to shuffle all letters from the input in all
    possible orders.
    """
    for char in string:
        print(char)
