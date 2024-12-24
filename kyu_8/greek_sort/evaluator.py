"""
Evaluator function for -> Greek Sort.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def evaluator(result: int, expected: str) -> bool:
    """
    Comparator for a list of phonetic words.

    :param result: int
    :param expected: str
    :return: bool
    """
    val: bool = False

    if expected == '< 0':
        val = result < 0

    if expected == '== 0':
        val = result == 0

    if expected == '> 0':
        val = result > 0

    return val
