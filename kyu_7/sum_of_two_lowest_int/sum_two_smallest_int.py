"""
Solution for -> Sum of two lowest positive integers
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def sum_two_smallest_numbers(numbers: list) -> int:
    """
    Returns the sum of the two lowest
    positive numbers given an array of
    minimum 4 positive integers.
    :param numbers:
    :return:
    """
    numbers.sort()
    return numbers[0] + numbers[1]
