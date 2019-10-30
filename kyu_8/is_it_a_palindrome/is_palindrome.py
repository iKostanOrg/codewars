#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def is_palindrome(s: str) -> bool:
    """
    Write function isPalindrome that checks if
    a given string (case insensitive) is a palindrome.
    :param s:
    :return:
    """
    s = s.lower()
    return s == s[::-1]
