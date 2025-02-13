"""
Solution for -> Sum of two lowest positive integers.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def sum_two_smallest_numbers(numbers: list) -> int:
    """
    Return the sum of the two lowest positive numbers.

    :param numbers: list
    :return: int
    """
    numbers.sort()
    return numbers[0] + numbers[1]
