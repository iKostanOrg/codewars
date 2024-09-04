"""
Test for -> Integers: Recreation One
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

import math


def divisor_generator(n: int):
    """
    The best way to get all the divisors of a number.
    :param n: integers
    :return: all dividers of n
    """
    # You should only be running your loop from 1 to the
    # square root of n. Then to find the pair, do n / i,
    # and this will cover the whole problem space.
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor


def is_perfect_square(n: str) -> bool:
    """
    Check if a number is a perfect square.
    (number made by squaring a whole number:
    4 * $ = 16).
    :param n: integer
    :return: bool
    """
    # Step 1: 1.A Perfect Square always ends
    # with one of these numbers ( 0, 1, 4, 5, 6, 9).
    if n[-1] not in "014569":
        return False
    # Step #2: No number can be a perfect square unless its
    # digital root is 1, 4, 7, or 9.
    if digital_root(n) in [1, 4, 7, 9] and math.sqrt(int(n)) % 1 == 0:
        return True
    return False


# Returns digital root of num
def digital_root(num: str) -> int:
    """
    The digital root or digital sum of a non-negative integer
    is the single-digit value obtained by an iterative process
    of summing digits, on each iteration using the result from
    the previous iteration to compute the digit sum. The process
    continues until a single-digit number is reached.

    :param num: a digit/number/integer
    :return: digital root
    """
    if len(num) == 1:
        return int(num)
    else:
        n_sum = 0
        for i in num:
            n_sum += int(i)
        return digital_root(str(n_sum))


def list_squared(m: int, n: int) -> list:
    """
    Given two integers m, n (1 <= m <= n) we want to
    find all integers between m and n whose sum of
    squared divisors is itself a square.

    :param m: start
    :param n: end
    :return: list of integers between m and n whose sum of
             squared divisors is itself a square
    """
    results: list = []
    for z in range(m, n + 1):
        sum_squared_dividers = sum([i * i for i in divisor_generator(z)])
        if is_perfect_square(str(sum_squared_dividers)):
            results.append([z, sum_squared_dividers])
    return results
