"""
Solution for -> Fibonacci Streaming.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def all_fibonacci_numbers():
    """
    All Fibonacci numbers.

    A utility method that generates an infinite sized,
    sequential IntStream (in Python generator) which
    contains all the numbers in a fibonacci sequence.
    :return: int
    """
    a: int = 0
    b: int = 1
    yield 1

    while True:
        c = a + b
        a, b = b, c
        yield c
