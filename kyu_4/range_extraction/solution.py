"""
Solution for -> Range Extraction
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def solution(args: list) -> str:
    """
    Tt takes a list of integers in increasing order and returns
    a correctly formatted string in the range format.
    :param args:
    :return:
    """
    current: list = [args[0], args[0], False]
    result: str = ''

    for i, a in enumerate(args):

        # case 1
        if current[1] == a:
            continue

        # case 2
        result = case_2(a, i, current, result)

        # case 3
        if i == len(args) - 1 and not current[2]:
            if current[1] + 1 == a:
                current[1] = a

            result += str(current[0])
            if abs(current[1] - current[0]) >= 2:
                result += '-' + str(current[1])
            elif current[0] != current[1]:
                result += ',' + str(current[1])

        # case 4
        if i == len(args) - 1 and current[-1] != a and current[2]:
            result += str(a)

    return result


def case_2(a: int, i: int,  current: list, result: str) -> str:
    """
    Case #2
    :param i:
    :param a:
    :param current:
    :param result:
    :return:
    """
    if a == current[1] + 1:
        current[1] = a
        current[2] = False
    else:
        current[2] = True

        if abs(current[1] - current[0]) >= 2 and i != 1:
            result += str(current[0]) + '-' + str(current[1]) + ','
        else:
            result += str(current[0]) + ','
            if current[0] != current[1]:
                result += str(current[1]) + ','

        current[0] = a
        current[1] = a

    return result
