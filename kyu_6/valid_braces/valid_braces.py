"""
Test for -> Valid Braces
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""
import typing

BRACES: dict = {
    '(': ')',
    ')': '(',
    '[': ']',
    ']': '[',
    '{': '}',
    '}': '{',
}

CLOSING: str = ')}]'


def valid_braces(string: str) -> bool:
    """
    A function that takes a string of braces, and determines if the order
    of the braces is valid. It should return true if the string is valid,
    and false if it's invalid.
    :param string: a string consist of brackets
    :return: boolean, indicates if input string is valid
    """
    index: int = 0
    while index < len(string) - 1:
        # get next index to validate
        index = validate_next_pair(string, index)
        if not index:
            return False

    return True


@typing.no_type_check
def validate_next_pair(string: str, index: int) -> None | int:
    """
    Check if next pair of brackets is valid
    :param string: string of brackets
    :param index: current index to validate
    :return: next index or None if no matching brackets
    """
    char: str = string[index]

    # in the first half of the string a new pair
    # should not be starting from closing brackets
    if index < (len(string) // 2) and char in CLOSING:
        return None

    # neighbor two brackets are matching pair
    if BRACES[char] == string[index + 1]:
        index += 2
        return index

    # matching pair consist of brackets
    # in each half of the string
    if BRACES[char] == string[(index + 1) * -1]:
        index += 1
        return index

    # no matching pair found
    return None
