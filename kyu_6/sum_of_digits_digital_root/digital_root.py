"""
Solution for -> Sum of Digits / Digital Root
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def digital_root(n: int) -> int:
    """
    In this kata, you must create a digital root function.

    A digital root is the recursive sum of all the digits
    in a number. Given n, take the sum of the digits of n.
    If that value has more than one digit, continue reducing
    in this way until a single-digit number is produced. This
    is only applicable to the natural numbers.

    :param n:
    :return:
    """
    if len(str(n)) == 1:
        return n
    else:
        temp: int = 0
        n_str: str = str(n)
        for char in n_str:
            temp += int(char)
        return digital_root(temp)
