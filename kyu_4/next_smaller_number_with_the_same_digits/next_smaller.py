"""
Solution for -> Next smaller number with the same digits

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def next_smaller(n: int) -> int:
    """
    A function that takes a positive integer and returns the
    next smaller positive integer containing the same digits.

    If no smaller number can be composed using those digits, return -1
    """
    # 1
    # Starting from the right, find the index of the first digit that
    # has at least one smaller digit to its right. We'll call that digit X.
    x_i: int = find_x(n)
    if x_i < 0:
        return x_i

    # 2
    # Then find the index of the largest digit that is to the
    # right of X, and is smaller than X. We'll call that digit Y.
    y_i: int = find_y(n, x_i)

    # 3
    # Swap X and Y. This makes the number smaller.
    n_list: list = [int(i) for i in str(n)]
    n_list[x_i], n_list[y_i] = n_list[y_i], n_list[x_i]

    # 4
    # Then sort all of the digits to the right of Y in descending order.
    # This makes the number as big as possible, without making it bigger
    # than the original.
    result: int = int(
        ''.join([str(i) for i in (n_list[:x_i + 1] + sorted(n_list[x_i + 1:],
                                                            reverse=True))]))
    return result if len(str(result)) == len(str(n)) else -1


def find_x(n: int) -> int:
    """
    Find x
    :param n: int
    :return: int
    """
    n_list: list = [int(i) for i in str(n)[::-1]]
    for index, digit in enumerate(n_list):
        if index - 1 >= 0 and n_list[index] > n_list[index - 1]:
            return len(n_list) - index - 1
    return -1


def find_y(n: int, x_i: int) -> int:
    """
    Find y
    :param n: int
    :param x_i: int
    :return: int
    """
    n_list: list = [int(i) for i in str(n)]
    comparable_x = {
        'x': n_list[x_i],
        'index': None,
        'y': None
    }

    for index, y in enumerate(n_list[x_i + 1:]):
        if comparable_x['x'] > y:
            if not comparable_x['y']:
                comparable_x['y'] = y
                comparable_x['index'] = index + x_i + 1
            else:
                if comparable_x['y'] < y:
                    comparable_x['y'] = y
                    comparable_x['index'] = index + x_i + 1
    return comparable_x['index'] if comparable_x['index'] else -1
