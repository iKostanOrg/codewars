#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def is_isogram(string: str) -> bool:
    """
    Determines whether a string that
    contains only letters is an isogram

    :param string: str
    :return: bool
    """
    return len(set(string.lower())) == len(string)
