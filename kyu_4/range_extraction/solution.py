"""
Solution for -> Range Extraction.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def solution(args: list) -> str:
    """
    Solution for Range Extraction problem.

    Tt takes a list of integers in increasing order and returns
    a correctly formatted string in the range format.
    :param args: list
    :return: str
    """
    current: list = [args[0], args[0], False]
    result: str = ''

    for i, a in enumerate(args):

        # case 1
        if current[1] == a:
            continue

        # case 2
        result = case_2(a=a, i=i, current=current, result=result)

        # case 3
        if i == len(args) - 1 and not current[2]:
            result = case_3(a=a, current=current, result=result)

        # case 4
        if i == len(args) - 1 and current[-1] != a and current[2]:
            result += str(a)

    return result


def case_3(a: int,
           current: list,
           result: str) -> str:
    """
    Case #3.

    :param a: int
    :param current: list
    :param result: str
    :return: str
    """
    if current[1] + 1 == a:
        current[1] = a

    result += str(current[0])
    if abs(current[1] - current[0]) >= 2:
        result += f'-{str(current[1])}'
    elif current[0] != current[1]:
        result += f',{str(current[1])}'

    return result


def case_2(**kwargs) -> str:
    """
    Case #2.

    :return: str
    """
    a: int = kwargs['a']
    i: int = kwargs['i']
    current: list = kwargs['current']
    result: str = kwargs['result']

    if a == current[1] + 1:
        current[1] = a
        current[2] = False
    else:
        current[2] = True

        if abs(current[1] - current[0]) >= 2 and i != 1:
            result += f'{str(current[0])}-{str(current[1])},'
        else:
            result += f'{str(current[0])},'
            if current[0] != current[1]:
                result += f'{str(current[1])},'

        current[0] = a
        current[1] = a

    return result
