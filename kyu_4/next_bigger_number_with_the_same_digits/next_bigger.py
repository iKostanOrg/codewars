#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


import itertools


def next_bigger(n: int) -> int:
    """
    A function that takes a positive integer number
    and returns the next bigger number formed by the same digits.

    If no bigger number can be composed using those digits, return -1
    """

    numbers = sorted(set(sorted(int(''.join(i)) for i in itertools.permutations(str(n)))))

    if n == numbers[-1]:
        return -1
    else:
        return numbers[numbers.index(n) + 1]
