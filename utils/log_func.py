"""
Print logs function.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def print_log(**kwargs) -> None:
    """
    Print log
    :param args:
    :return:
    """

    log = ''
    for key in kwargs:
        log += '{}: {},\n'.format(key, kwargs[key])

    print('\nLOG =>\n{}\n'.format(log[:-2]))
    return None
