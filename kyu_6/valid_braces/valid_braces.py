"""
Test for -> Valid Braces
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

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
        # in the first half of the string a new pair
        # should not be starting from closing brackets
        if index < (len(string) // 2) and string[index] in CLOSING:
            return False
        # neighbor two brackets are matching pair
        if BRACES[string[index]] == string[index + 1]:
            index += 2
            continue
        # matching pair consist of brackets
        # in each half of the string
        if BRACES[string[index]] == string[(index + 1) * -1]:
            index += 1
            continue
        # no matching pair
        return False

    return True
