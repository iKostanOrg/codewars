#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def get_min_digit(digits: list) -> int:

    min_digit = min(digits)
    if digits.index(min_digit) != 0:
        return min_digit
    else:
        min_digit = digits[1]
        for digit in digits[2:]:
            if digit < min_digit:
                min_digit = digit
        return min_digit


def concat_new_n(digits: list, min_digit: int, min_index: int) -> list:

    print()
    if min_digit < digits[0] and min_digit != 0:
        print('Rule #1')

        i, j = min_index, 0
        del digits[min_index]
        digits = [min_digit] + digits
    elif min_digit == 0:
        print('Rule #2')

        if min_index == 1:
            i, j = 0, min_index
            del digits[min_index]
        else:
            while digits[min_index] == 0:
                if min_index - 1 >= 0:
                    min_index -= 1
                else:
                    break

            i, j = min_index + 1, 0
            del digits[min_index + 1]
    else:
        print('Rule #3')

        max_digit = max(digits)
        i = min_index
        j = digits.index(max_digit)

        pre = digits[:j]
        digits.remove(digits[j])
        digits.remove(min_digit)
        for d in pre:
            digits.remove(d)

        digits = pre + [min_digit] + [max_digit] + digits

    return [int(''.join([str(digit) for digit in digits])), i, j]


def smallest(n: int) -> list:
    """
    Return an array or a tuple or a string depending on the language (see "Sample Tests") with

        1) the smallest number you got
        2) the index i of the digit d you took, i as small as possible
        3) the index j (as small as possible) where you insert this digit d to have the smallest number.

    :param n: a positive number n consisting of digits
    :return: an array with: smallest number, index, digit
    """
    digits: list = [int(char) for char in str(n)]

    min_digit = get_min_digit(digits)
    min_index = ''.join([str(d) for d in digits]).rindex(str(min_digit))

    return concat_new_n(digits, min_digit, min_index)
