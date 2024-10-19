"""
Check if number is prime
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

import math


def is_prime(n: int) -> bool:
    """
    Function to check for a prime number
    Return TRUE if 'n' is prime number. False otherwise
    :param n:
    :return:
    """
    result: bool = True

    if n <= 1 or (n % 2 == 0 and n > 2) or (n % 3 == 0 and n > 3):
        result = False

    if n == 2:
        result = True

    for x in range(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            result = False

    return result
