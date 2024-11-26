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
    :param string:
    :return:
    """
    # Calc length of the input string
    len_str: int = len(string)
    # If the length is not even number -> return False
    if len_str % 2 > 0:
        return False

    index: int = 0
    while index < len(string) - 1:
        char = string[index]

        # in the first half of the string should
        # not be any closing brackets
        if index < (len_str // 2) and char in CLOSING:
            return False

        # next two brackets are matching pair
        if BRACES[char] == string[index + 1]:
            index += 2
        # matching pair consist of brackets in each
        # half of the string
        elif BRACES[char] == string[(index + 1) * -1]:
            index += 1
        # no matching pair
        else:
            return False

    return True
