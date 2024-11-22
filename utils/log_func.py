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
    print_output = kwargs.get('print_output', False)
    log: str = ''
    for key, item in kwargs.items():
        log += f'{key}: {item},\n'

    if print_output:
        print(f'\nLOG =>\n{log[:-2]}\n')
