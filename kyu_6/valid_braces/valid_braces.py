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

    # calculate indexes in order to process matching pairs
    a, b = (len_str // 2) - 1, len_str // 2
    while a > -1 and b < len_str:
        # Pair does not match, fails the test
        if BRACES[string[a]] != string[b]:
            return False
        a -= 1
        b += 1

    return True
