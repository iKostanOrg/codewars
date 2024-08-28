"""
Evaluate mathematical expression.

Given a mathematical expression as a
string you must return the result as a number.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

OPERATORS = ['*', '/', '+', '-']


def calculate(i: int, char: str, strings: list) -> None:
    """
    Calculate math expression

    :param i: int
    :param char: str
    :param strings: list
    :return: None
    """
    a = float(strings[i - 1])
    b = float(strings[i + 1])

    if char == '*':
        strings[i] = str(a * b)

    if char == '/':
        strings[i] = str(a / b)

    del strings[i + 1]
    del strings[i - 1]


def process_math_expression(string: str, operators: list) -> str:
    """
    Process math expression

    :param string: str
    :param operators: list
    :return: str
    """
    strings = [s for s in string.split(' ') if bool(s != '+')]

    while any(s in operators for s in strings):
        for i, char in enumerate(strings):
            if char in operators:
                calculate(i, char, strings)
                break

    return ' '.join(strings)


def normalize_string(string: str) -> str:
    """
    Normalizing string input

    :param string: str
    :return: str
    """
    strings = []
    string_temp = ''.join([s for s in string if s != ' '])

    while string_temp != '':
        temp = ''

        for i, s in enumerate(string_temp):
            if s.isdigit():
                temp += s

            if s in '()':
                if temp != '':
                    strings.append(temp)
                strings.append(s)

                if i + 1 < len(string_temp):
                    string_temp = string_temp[i + 1:]
                else:
                    string_temp = ''
                break

            if s in OPERATORS:
                if temp != '':
                    strings.append(temp)
                strings.append(s)

                if i + 1 < len(string_temp):
                    string_temp = string_temp[i + 1:]
                break

            if i == len(string_temp) - 1:
                if temp != '':
                    strings.append(temp)
                string_temp = ''

    return ' '.join([s for s in strings if s != ''])


def bracket_start(strings: list) -> int:
    """
    Return index of first (open) bracket

    :param strings: list
    :return: int
    """
    return ([i for i, strg in enumerate(strings) if strg == '('])[-1]


def bracket_end(strings: list, start: int) -> int:
    """
    Return index of last (close) bracket

    :param strings:
    :param start:
    :return:
    """
    return strings[start:].index(')') + start


def process_brackets(string: str) -> str:
    """
    Process brackets in order to convert
    input string into math expression

    :param string: str
    :return: str
    """
    strings = string.split(' ')

    while '(' in strings:
        start = bracket_start(strings=strings)
        end = bracket_end(strings=strings, start=start)

        if len(strings[start + 1: end]) < 3:
            del strings[end]
            del strings[start]

        if len(strings[start + 1: end]) > 2:
            temp = ' '.join(strings[start + 1: end])
            temp = process_duplicate_minus(temp)
            temp = process_math_expression(temp, ['*', '/'])
            temp = str(sum([float(t) for t in temp.split() if t != '+']))
            tmp_strings = strings[:start]
            tmp_strings.append(temp)
            if end < len(strings) - 1:
                tmp_strings += strings[end + 1:]
            strings = tmp_strings

    return ' '.join(strings)


def process_duplicate_minus(string: str) -> str:
    """
    Eliminate duplicate minus

    :param string: str
    :return: str
    """
    done = False
    strings = string.split(' ')

    while not done:
        done = True
        for i, s in enumerate(strings):

            if s == '-':
                if strings[i + 1] == '-':
                    done = False
                    strings[i] = '+'
                    del strings[i + 1]
                    break

                if any([t.isdigit() for t in strings[i + 1]]):
                    done = False
                    strings[i] = str(float(strings[i + 1]) * (-1))
                    del strings[i + 1]
                    break

            if s == '+':
                if strings[i + 1] == '-':
                    done = False
                    del strings[i]
                    break

    return ' '.join([s for s in strings if s != ''])


def calc(string: str) -> float:
    """
    Calculate math expression from input string

    :param string: str
    :return: float
    """
    string = normalize_string(string)
    string = ' '.join(string.split('+'))
    string = process_brackets(string)
    string = process_duplicate_minus(string)
    string = process_math_expression(string, ['*', '/'])
    string = str(sum([float(s) for s in string.split(' ')]))
    return float(string)
