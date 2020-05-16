#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def increment_string(string: str) -> str:
    """
    A function which increments a string, to create a new string:
    1. If the string already ends with a number, the number should be incremented by 1.
    2. If the string does not end with a number. the number 1 should be appended to the new string.

    :param string: input string
    :return: output string with incremented number
    """
    first_digit = get_first_digit_index(string)

    if first_digit:
        digit: int = int(string[first_digit:])
        incremented_digit: str = '{}{}'.format(('0' * (len(string[first_digit:]) - len(str(
            digit + 1))) if len(str(digit + 1)) != len(string[first_digit:]) else ''), digit + 1)
        return '{}{}'.format(string[:first_digit], incremented_digit)
    else:
        if string.isdigit():
            digit = int(string)
            incremented_digit = '{}{}'.format(
                ('0' * (len(string) - len(str(digit + 1))) if len(str(digit + 1)) != len(string)
                 else ''), digit + 1)
            return incremented_digit
        else:
            return '{}{}'.format(string, 1)


def get_first_digit_index(string: str):
    """
    Find index of first non digit char from right to left

    :param string: input string
    :return: index of first non digit char or None
    """
    for i in range(-1, -1 * len(string) - 1, -1):
        if not string[i].isdigit():
            return i + 1
    return None
