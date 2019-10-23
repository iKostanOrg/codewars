#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def sum_triangular_numbers(n: int) -> int:
    """
    returns the sum of Triangular Numbers
    up-to-and-including the nth Triangular Number.
    :param n:
    :return:
    """

    if n <= 0:
        return 0

    sum_nums = [0]
    for i in range(1, n + 1):
        sum_nums.append(sum_nums[-1] + i)

    return sum(sum_nums)
