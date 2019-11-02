#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def factorial(n: int) -> int:
    """
    A function to calculate factorial for a given input.
    If input is below 0 or above 12 throw an exception
    of type ValueError (Python).
    :param n:
    :return:
    """

    if n < 0 or n > 12:
        raise ValueError('Invalid input: {}'.format(n))

    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result
