"""
Solution for -> Format a string of names like \'Bart, Lisa & Maggie\'.
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def namelist(names: list) -> str:
    """
    Format a string of names like 'Bart, Lisa & Maggie'

    :param names: an array containing hashes of names
    :return: a string formatted as a list of names separated
             by commas except for the last two names, which
             should be separated by an ampersand.
    """
    if not names:
        return ""

    names_list: list = [name['name'] for name in names]

    if len(names_list) == 1:
        return names_list[0]

    if len(names_list) == 2:
        return f'{names_list[0]} & {names_list[1]}'

    return ', '.join(names_list[:-1]) + ' & ' + names_list[-1]
