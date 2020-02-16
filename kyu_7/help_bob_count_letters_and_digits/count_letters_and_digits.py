#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def count_letters_and_digits(s: str) -> int:
    """
    A method that can determine how many
    letters and digits are in a given string.
    :param s:
    :return:
    """

    result = 0

    for char in s:
        if char.isalpha() or char.isdigit():
            result += 1

    return result
