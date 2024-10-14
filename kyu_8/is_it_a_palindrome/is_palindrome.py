"""
Solution for -> Is it a palindrome?
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def is_palindrome(s: str) -> bool:
    """
    Write function isPalindrome that checks if
    a given string (case insensitive) is a palindrome.
    :param s: str
    :return: bool
    """
    s = s.lower()
    return s == s[::-1]
