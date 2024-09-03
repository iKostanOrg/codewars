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
    current = [args[0], args[0], False]
    result = ''

    for i, a in enumerate(args):

        if current[1] == a:
            continue

        if a == current[1] + 1:
            current[1] = a
            current[2] = False
        else:
            if abs(current[1] - current[0]) >= 2 and i != 1:
                result += str(current[0]) + '-' + str(current[1]) + ','
                current[2] = True
            else:
                result += str(current[0]) + ','
                current[2] = True

                if current[0] != current[1]:
                    result += str(current[1]) + ','

            current[0] = a
            current[1] = a

        if i == len(args) - 1 and current[2] is False:

            if current[1] + 1 == a:
                current[1] = a

            result += str(current[0])
            if abs(current[1] - current[0]) >= 2:
                result += '-' + str(current[1])
            elif current[0] != current[1]:
                result += ',' + str(current[1])

        if i == len(args) - 1 and current[-1] != a and current[2] is True:
            result += str(a)

    return result
