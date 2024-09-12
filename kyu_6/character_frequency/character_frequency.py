"""
Solution for -> Character frequency
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def letter_frequency(text: str) -> list:
    """
    return a list of tuples sorted by frequency with
    the most frequent letter first. Any letters with the
    same frequency are ordered alphabetically
    :param text:
    :return:
    """
    results: list = []
    chars: dict = dict()
    text: str = text.lower()

    for c in text:
        if c.isalpha() and c not in chars:
            chars[c] = text.count(c)
            results.append((c, chars[c]))

    results = sort_list(results)
    return results


def sort_list(results: list) -> list:
    """
    Sort results list
    :param results: list
    :return: list
    """

    is_sorted: bool = False
    results_length: int = len(results)

    while not is_sorted:
        is_sorted = True
        for i, result in enumerate(results):
            if i < (results_length - 1) and (results[i][1] < results[i + 1][1]):
                results[i], results[i + 1] = results[i + 1], result
                is_sorted = False
            elif i < (results_length - 1) and \
                    (results[i][1] == results[i + 1][1]) and \
                    (results[i][0] > results[i + 1][0]):
                results[i], results[i + 1] = results[i + 1], result
                is_sorted = False

    return results
