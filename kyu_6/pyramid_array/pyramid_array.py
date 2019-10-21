#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def pyramid(n):
    """
    Write a function that when given a number >= 0,
    returns an Array of ascending length subarrays.

    Note: the subarrays should be filled with 1s
    :param n:
    :return:
    """
    result = []
    if n is None or n == 0:
        return result

    for n in range(1, n + 1):
        result.append([1] * n)

    return result
