"""
Solution for -> Significant Figures.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def number_of_sigfigs(number: str) -> int:
    """
    Return the number of significant figures in the given number.

    :param number:
    :return:
    """
    number = normalize_string(number)
    if number == '0':
        return 0
    if number == '0.0':
        return 1

    result: int = 0
    for i, char in enumerate(number):
        if char.isdigit() and not (i == 0 and char == '0'):
            result += 1

    return result


def normalize_string(number: str) -> str:
    """
    Normalize string by converting it into a number and back to string again.

    :param number:
    :return:
    """
    if '.' not in number:
        number = str(int(number))
        number = remove_extra_zeroes(number)
    else:
        number = remove_extra_leading_zeroes(number)

    return number


def remove_extra_zeroes(number: str) -> str:
    """
    Remove all zeroes from the end of the string.

    :param number:
    :return:
    """
    index = None
    for i in range(-1, len(number) * -1, -1):
        if number[i] == '0':
            index = i
        else:
            break

    if index is not None:
        return number[0:index]

    return number


def remove_extra_leading_zeroes(number: str) -> str:
    """
    Remove all extra leading zeroes from the head of the string.

    :param number:
    :return:
    """
    new_number: str = str(float(number))
    after_dot: int = len(number[number.index('.'):])
    new_after_dot: int = len(new_number[new_number.index('.'):])

    if after_dot == new_after_dot:
        return new_number

    return new_number + ('0' * (after_dot - new_after_dot))
