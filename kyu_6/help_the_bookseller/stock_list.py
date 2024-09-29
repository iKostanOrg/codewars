"""
Solution for -> Help the bookseller !
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def stock_list(list_of_art: list, list_of_cat: list) -> str:
    """
    You will be given a stockist (e.g. : L) and a
    list of categories in capital letters e.g :
    M = {"A", "B", "C", "W"}
    M = ["A", "B", "C", "W"]

    and your task is to find all the books of L with
    codes belonging to each category of M and to sum
    their quantity according to each category.

    :param list_of_art: list
    :param list_of_cat: list
    :return: string
    """
    result: str = ''

    if not list_of_art:
        return result

    for cat in list_of_cat:
        total = 0

        for art in list_of_art:
            if cat in art[0]:
                total += int(art.split(' ')[1])

        if result != '':
            result += f' - ({cat} : {total})'
        else:
            result += f'({cat} : {total})'

    return result
