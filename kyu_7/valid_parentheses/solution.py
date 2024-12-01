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
    # convert string into list
    paren_str_list: list = list(paren_str)

    while paren_str_list:
        # 1. Fail if starts from closing bracket
        # 2. A number of closing and opening
        # brackets should be equal
        if paren_str_list[0] == ')' or paren_str.count('(') != paren_str.count(')'):
            return False
        # Find matching pair and remove them from the string
        for i in range(1, len(paren_str_list)):
            if paren_str_list[i] == ')':
                # delete a matching pair
                del paren_str_list[i]
                del paren_str_list[0]
                # start all over again
                break

    return True
