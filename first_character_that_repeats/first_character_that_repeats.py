#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def first_dup(s):
    """
    Find the first character that repeats
    in a String and return that character.
    :param s:
    :return:
    """
    for char in s:
        if s.count(char) > 1:
            return char

    return None
