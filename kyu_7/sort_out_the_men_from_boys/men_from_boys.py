#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def men_from_boys(arr: list) -> list:
    """
    Sort out the men from the boys.

    Men are the Even numbers and Boys are the odd.

    Return an array/list where Even numbers
    come first then odds.

    Since, Men are stronger than Boys,
    then Even numbers in ascending order
    while odds in descending.
    :param arr:
    :return:
    """

    boys = list()
    men = list()

    for a in arr:
        if a % 2 == 0:
            if a not in men:
                men.append(a)
        else:
            if a not in boys:
                boys.append(a)

    return sorted(men) + sorted(boys, reverse=True)
