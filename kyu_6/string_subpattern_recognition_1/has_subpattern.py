#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import math


def has_subpattern(string: str) -> bool:
    """
    String subpattern recognition I

    In this kata you need to build a function to return
    either true/True or false/False if a string can be
    seen as the repetition of a simpler/shorter subpattern or not.

    Strings will never be empty and can be composed of any character
    (just consider upper- and lowercase letters as different entities)
    and can be pretty long (keep an eye on performances!).

    :param string:
    :return:
    """

    pass


def is_prime(n: int) -> list:
    """
    Test if a number is a prime number
    :param n:
    :return:
    """

    if n < 2:
        return [False, n]

    if n == 2:
        return [True]

    if n != 2 and n % 2 == 0:
        return [False, 2]

    for i in range(3, int(math.sqrt(n)) + 1,  2):
        if n % i == 0:
            return [False, i]

    return [True]
