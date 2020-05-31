"""Strings Mix"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import string

LOWERCASE = string.ascii_lowercase


def mix(s1: str, s2: str) -> str:
    """
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
        list(set([key for key in s1_results] + [key for key in s2_results])))

    results: list = list()
    for key in keys:
        if key in s2_results and key in s1_results:
            if s1_results[key] == s2_results[key]:
                results.append('=:{}'.format(key * s1_results[key]))
            elif s1_results[key] > s2_results[key]:
                results.append('1:{}'.format(key * s1_results[key]))
            else:
                results.append('2:{}'.format(key * s2_results[key]))
        else:
            if key in s1_results:
                results.append('1:{}'.format(key * s1_results[key]))
            else:
                results.append('2:{}'.format(key * s2_results[key]))

    return '/'.join(sort_results(results))


def sort_results(results: list) -> list:
    """
    The results will be in decreasing order of their length
    and when they have the same length sorted in ascending
    lexicographic order (letters and digits - more precisely
    sorted by code-point)
    :param results:
    :return:
    """
    results = sorted(results)

    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(0, len(results)):
            if i + 1 < len(results):

                if (len(results[i]) == len(results[i + 1])) and \
                        (results[i][0] > results[i + 1][0]):
                    is_sorted = False
                    results[i], results[i + 1] = results[i + 1], results[i]

                if len(results[i]) < len(results[i + 1]):
                    is_sorted = False
                    results[i], results[i + 1] = results[i + 1], results[i]
    return results


def get_counters(s: str) -> dict:
    s_results: dict = dict()
    for char in s:
        counter = s.count(char)
        if char in LOWERCASE and counter > 1 and char not in s_results:
            s_results[char] = counter
    return s_results
