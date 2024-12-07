"""
Solution for -> Strings Mix.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

import string

LOWERCASE = string.ascii_lowercase


def mix(s1: str, s2: str) -> str:
    """
    Mix function.
    
    Given two strings s1 and s2, we want to visualize
    how different the two strings are. We will only
    take into account the lowercase letters (a to z).
    First let us count the frequency of each lowercase
    letters in s1 and s2.
    :param s1: string a
    :param s2: string b
    :return: the difference between two strings
    """
    s1_results: dict = get_counters(s1)
    s2_results: dict = get_counters(s2)
    keys: list = sorted(
        list(
            set(
                list(s1_results.keys()) + list(s2_results.keys())
            )))

    results: list = []
    for key in keys:
        if (
            key in s2_results
            and key in s1_results
            and s1_results[key] == s2_results[key]
        ):
            results.append(f'=:{key * s1_results[key]}')
        elif (
            key in s2_results
            and key in s1_results
            and s1_results[key] > s2_results[key]
            or (key not in s2_results or key not in s1_results)
            and key in s1_results
        ):
            results.append(f'1:{key * s1_results[key]}')
        else:
            results.append(f'2:{key * s2_results[key]}')
    return '/'.join(sort_results(results))


def sort_results(results: list) -> list:
    """
    Sorting results.

    The results will be in decreasing order of their length
    and when they have the same length sorted in ascending
    lexicographic order (letters and digits - more precisely
    sorted by code-point).
    :param results:
    :return:
    """
    results = sorted(results)
    is_sorted: bool = False

    while not is_sorted:
        is_sorted = True
        for i, result in enumerate(results):
            if i + 1 < len(results):

                if (len(results[i]) == len(results[i + 1])) and \
                        (results[i][0] > results[i + 1][0]):
                    is_sorted = False
                    results[i], results[i + 1] = results[i + 1], result

                if len(results[i]) < len(results[i + 1]):
                    is_sorted = False
                    results[i], results[i + 1] = results[i + 1], result
    return results


def get_counters(s: str) -> dict:
    """
    Get counters.
    
    :param s: str
    :return: dict
    """
    s_results: dict = {}
    for char in s:
        counter = s.count(char)
        if char in LOWERCASE and counter > 1 and char not in s_results:
            s_results[char] = counter
    return s_results
