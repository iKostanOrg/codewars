"""
Solution for -> Master your primes: sieve with memoization
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def is_prime(digit: int) -> bool:
    """
    A function that checks if a given number 'digit' is a prime looping
    through it and, possibly, expanding the array/list of known
    primes only if/when necessary (ie: as soon as you check for a
    potential prime which is greater than a given threshold for
    each 'digit', stop}.
    :param digit: int
    :return: bool
    """
    primes: list = [2, 3, 5, 7]

    if digit < 2:
        return False

    for i in range(3, int(digit ** 0.5) + 1, 2):
        if is_prime(i) and i not in primes:
            primes.append(i)

        if digit % i == 0:
            return False

    return True
