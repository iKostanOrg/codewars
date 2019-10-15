import math

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def is_square(n) -> bool:
    """
    Given an integral number, determine if it's a square number:
    :param n:
    :return:
    """
    if n > -1:
        number = math.sqrt(n)
        if (number - int(number)) == 0:
            return True
    return False
