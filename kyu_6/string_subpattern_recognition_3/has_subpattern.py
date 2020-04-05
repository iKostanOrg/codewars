#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from typing import Set, Dict
from utils.is_prime_util.is_prime import is_prime


def has_subpattern(string: str) -> str:
    """
    String subpattern recognition III

    Since there is no deterministic way to tell which pattern
    was really the original one among all the possible
    permutations of a fitting subpattern, return a subpattern
    with sorted characters, otherwise return the base string
    with sorted characters (you might consider this case as an
    edge case, with the subpattern being repeated only once
    and thus equalling the original input string).

    :param string:
    :return:
    """

    primes: Set[int] = set()
    length: int = len(string)
    char_dict: Dict[str, int] = dict()

    for char in string:

        if char not in char_dict:
            char_dict[char] = string.count(char)

            if char_dict[char] == 1:
                return ''.join(sorted(char for char in string))

            if char_dict[char] in primes or is_prime(char_dict[char]):
                primes.add(char_dict[char])
                if length % char_dict[char] != 0:
                    return ''.join(sorted(char for char in string))

    result: str = ''.join(sorted(list(set(string))))
    return result
