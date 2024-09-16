"""
Solution for -> String subpattern recognition I
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def has_subpattern(string: str) -> bool:
    """
    String subpattern recognition I

    In this kata you need to build a function to return
    either true/True or false/False if a string can be
    seen as the repetition of a simpler/shorter subpattern or not.

    Strings will never be empty and can be composed of any character
    (just consider upper- and lowercase letters as different entities)
    and can be pretty long (keep an eye on performances!).

    :param string:
    :return:
    """
    length: int = len(string)

    n: int = 2
    while n < (length // 2) + 1:
        if length % n != 0:
            n += 1
            continue
        if string[0:length // n] * n == string:
            return True
        n += 1

    return False
