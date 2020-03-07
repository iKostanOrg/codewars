"""Find the odd int"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from typing import List, Dict


def find_it(seq: List[int]) -> int:
    """
    Given an array, find the int that
    appears an odd number of times.
    :param seq:
    :return:
    """
    pares: Dict[int, int] = dict()
    result: int = 0

    for n in seq:
        if n not in pares:
            pares[n] = 1
        else:
            pares[n] = pares[n] + 1

    for key in pares.keys():
        if pares[key] % 2 > 0:
            result = key
            break

    return result
