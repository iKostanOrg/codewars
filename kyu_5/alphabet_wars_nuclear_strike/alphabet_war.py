"""
Solution for -> Alphabet wars - nuclear strike
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def alphabet_war(battlefield: str) -> str:
    """
    A function that accepts battlefield string and
    returns letters that survived the nuclear strike.
    :param battlefield:
    :return: str
    """

    if '#' not in battlefield:
        return ''.join(char for char in battlefield if char.isalpha())

    result: str = clean_unsheltered(battlefield)
    result: str = clean_battlefield(result)
    return result


def clean_unsheltered(battlefield: str) -> str:
    """
    Clean letters outside the shelter
    :param battlefield: str
    :return: str
    """

    result: str = ''
    temp = battlefield.split('[')

    for char in temp:
        if char.count(']') == 0:
            c = ''.join(k for k in char if not k.isalpha())
            result += c
        elif len(char) == char.count('#'):
            result += char
        else:
            sharp = char.count('#')
            char = char[0:char.index(']') + 1]
            result += '[' + char + ('#' * sharp)

    return result


def clean_battlefield(battlefield: str) -> str:
    """
    Clean the battlefield and return only survived letters
    :param battlefield: str
    :return: str
    """
    result: list = battlefield.split('[')
    result: list = [string for string in result if string != '']
    result: list = list(reversed(result))
    temp: list = list()

    while result:
        for i, r in enumerate(result):
            if r.count('#') <= 1:
                if i + 1 < len(result) and (r.count('#') == 0 and result[i + 1].count('#') < 2):
                    temp.append(''.join(char for char in r if char .isalpha()))
                    del result[i]
                    break

                if i + 1 < len(result) and (r.count('#') == 1 and result[i + 1].count('#') == 0):
                    temp.append(''.join(char for char in r if char .isalpha()))
                    del result[i]
                    break

                if i + 1 < len(result):
                    del result[i]
                    break

                temp.append(''.join(char for char in r if char .isalpha()))
                del result[i]
                break

            del result[i]
            break

    answer: str = ''.join(char for char in reversed(temp))
    return answer
