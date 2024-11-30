"""
Solution for -> Valid Parentheses
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

def valid_parentheses(paren_str: str) -> bool:
    """
    A function that takes a string of parentheses, and determines
    if the order of the parentheses is valid. The function should
    return true if the string is valid, and false if it's invalid.
    :param paren_str: str
    :return: bool
    """
    print(paren_str)

    # Should return True for empty strings
    if not paren_str:
        return True

    # Fail if starts from closing bracket
    if paren_str[0] == ')':
        return False

    # A number of closing and opening
    # brackets should be equal
    if paren_str.count('(') != paren_str.count(')'):
        return False

    while paren_str:
        # Fail if starts from closing bracket
        if paren_str[0] == ')':
            return False
        # Find matching pair and remove them from the string
        for i in range(1, len(paren_str)):
            if paren_str[i] == ')':
                paren_str = update_str(paren_str, i)
                break

    return True


def update_str(paren_str: str, i: int) -> str:
    """
    Update string:
    1. remove first char.
    2. remove matching char/bracket.
    :param paren_str: str
    :param i: int
    :return: str
    """
    return ''.join(paren_str[indx] for indx, char in enumerate(paren_str) if indx not in [0, i])
