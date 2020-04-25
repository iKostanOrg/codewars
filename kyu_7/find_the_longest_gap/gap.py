#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def gap(num: int) -> int:
    """
    Returns the length of its longest
    binary gap.

    The function should return 0 if
    num doesn't contain a binary gap.
    :param num:
    :return:
    """
    binary = "{0:b}".format(num)
    g_max = g_cur = 0

    for i, char in enumerate(binary):
        if binary[i:].count('1') == 0:
            break

        g_cur = calc_g_cur(g_cur, char)
        g_max = calc_g_max(g_cur, g_max)

    return g_max


def calc_g_cur(g_cur, char):
    """
    Calculates g_cur
    :param g_cur:
    :param char:
    :return:
    """
    if char == '0':
        g_cur += 1
    else:
        g_cur = 0
    return g_cur


def calc_g_max(g_cur, g_max):
    """
    Calculates g_max
    """
    if g_cur > g_max:
        g_max = g_cur
    return g_max
