"""
Solution for -> Permute a Palindrome
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def permute_a_palindrome(string: str) -> bool:
    """
    A function that check whether the permutation
    of an input string is a palindrome.
    :param string:
    :return:
    """

    if string == '' or \
            string is None or \
            len(string) == 1 or \
            string == string[::-1]:
        return True

    non_even = 0
    chars = set(string)
    for char in chars:
        if string.count(char) % 2 != 0:
            non_even += 1

        if non_even > 1:
            return False

    return True
