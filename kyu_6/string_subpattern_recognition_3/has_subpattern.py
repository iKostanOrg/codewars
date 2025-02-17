"""
Solution for -> String subpattern recognition III.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

import math


def has_subpattern(string: str) -> str:
    """
    Recognition of string subpattern III.

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
    # get unique chars
    filtered_chars: set = set(list(string))
    # set counter for each char in string
    char_counter: dict = {}
    for char in filtered_chars:
        char_counter[char] = string.count(char)

    # get sorted counters
    sorted_char_counters: list = sorted(set(char_counter.values()))
    # find common greatest divider:
    divider = sorted_char_counters[0]
    if len(sorted_char_counters) > 1:
        for r in sorted_char_counters[1:]:
            divider = math.gcd(divider, r)

    # return result as a string
    return ''.join(char * (char_counter[char] // divider) for char in sorted(filtered_chars))
