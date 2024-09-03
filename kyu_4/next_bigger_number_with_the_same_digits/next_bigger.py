"""
Solution for -> Next bigger number with the same digits

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def next_bigger(n: int) -> int:
    """
    A function that takes a positive integer number
    and returns the next bigger number formed by the same digits.

    If no bigger number can be composed using those digits, return -1
    """
    # 1. Starting from last digit of given number, find the first digit
    # which breaks the sorted ordering. Let the index of this found
    # digit be 'i' and the digit be number[i].
    digits: list = list(str(n))
    i: int = digit_that_breaks_ordering_index(digits)
    # 2. Find the next greater digit in the right portion of number[i] - that
    # is from digit at index i+1 to last digit. Let that digit be number[j]
    # at index 'j'.
    j: int = next_greater_digit_index(digits, i + 1)
    # If the digits can't be rearranged to form a bigger number, return -1
    if j == -1:
        return j
    # 3. Swap digits at index 'i' and 'j'.
    digits[i], digits[j] = digits[j], digits[i]
    # 4. Sort the number from index i+1 to end index.
    return int(''.join(digits[:i + 1] + sorted(digits[i + 1:])))


def digit_that_breaks_ordering_index(digits: list) -> int:
    """
    Starting from last digit of given number, find the first
    digit which breaks the sorted ordering. Let the index of
    this found digit be 'i' and the digit be number[i].

    :param digits: list of digits
    :return: the index of the first digit which breaks the sorted ordering
    """
    i: int = -1
    for index in range(len(digits) - 1, -1, -1):
        if index - 1 >= 0 and digits[index] > digits[index - 1]:
            return index - 1
    return i if i >= 0 else 0


def next_greater_digit_index(digits: list, i: int) -> int:
    """
    Find the next greater digit in the right portion of
    number[i] - that is from digit at index i+1 to last
    digit. Let that digit be number[j] at index 'j'.

    :param digits: list of digits
    :param i: index of number[i]
    :return: next greater digit in the right portion of number[i]
    """
    j: int = -1
    current = ''
    if len(digits[i:]) == 1 and digits[1] > digits[0]:
        return i

    for index, digit in enumerate(digits[i:]):
        if digits[i - 1] < digit:
            if current == '':
                current = digit
                j = i + index
            elif current > digit:
                current = digit
                j = i + index
    return j
