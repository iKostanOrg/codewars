#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import math


def is_prime(n: int) -> bool:
    """
    Function to check for a prime number
    Return TRUE if i is prime number. False otherwise
    :param n:
    :return:
    """

    if n == 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0 and n > 2:
        return False

    for x in range(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False

    return True
