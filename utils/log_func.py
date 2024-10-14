"""
Print logs function.
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def print_log(**kwargs) -> None:
    """
    Print log
    :param kwargs:
    :return:
    """
    log: str = ''
    for key in kwargs:
        log += f'{key}: {kwargs[key]},\n'

    print(f'\nLOG =>\n{log[:-2]}\n')
    return None
