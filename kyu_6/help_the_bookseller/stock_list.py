"""
Solution for -> Help the bookseller !
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def stock_list(listOfArt: list, listOfCat: list) -> str:
    """
    You will be given a stockist (e.g. : L) and a
    list of categories in capital letters e.g :
    M = {"A", "B", "C", "W"}
    M = ["A", "B", "C", "W"]

    and your task is to find all the books of L with
    codes belonging to each category of M and to sum
    their quantity according to each category.

    :param listOfArt: list
    :param listOfCat: list
    :return: string
    """
    result = ''

    if not listOfArt:
        return result

    for cat in listOfCat:
        total = 0

        for art in listOfArt:
            if cat in art[0]:
                total += int(art.split(' ')[1])

        if result != '':
            result += ' - ({} : {})'.format(cat, total)
        else:
            result += '({} : {})'.format(cat, total)

    return result
