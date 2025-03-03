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
    Calculate math expression.

    :param i: int
    :param char: str
    :param strings: list
    :return: None
    """
    # pylint: disable=R0801
    a: float = float(strings[i - 1])
    b: float = float(strings[i + 1])

    if char == '*':
        strings[i] = str(a * b)

    if char == '/':
        strings[i] = str(a / b)
    # pylint: enable=R0801
    del strings[i + 1]
    del strings[i - 1]


def process_math_expression(string: str, operators: list) -> str:
    """
    Process math expression.

    :param string: str
    :param operators: list
    :return: str
    """
    strings: list = [s for s in string.split(' ') if bool(s != '+')]

    while any(s in operators for s in strings):
        for i, char in enumerate(strings):
            if char in operators:
                calculate(i, char, strings)
                break

    return ' '.join(strings)


def bracket_start(strings: list) -> int:
    """
    Return index of first (open) bracket.

    :param strings: list
    :return: int
    """
    a: int = ([i for i, strg in enumerate(strings) if strg == '('])[-1]
    return a


def bracket_end(strings: list, start: int) -> int:
    """
    Return index of last (close) bracket.

    :param strings:
    :param start:
    :return:
    """
    return strings[start:].index(')') + start


def process_brackets(strings: list) -> str:
    """
    Test bracket processing.

    Process brackets in order to convert input
    string into math expression.
    :param strings: list
    :return: str
    """
    while '(' in strings:
        start = bracket_start(strings=strings)
        end = bracket_end(strings=strings, start=start)

        if len(strings[start + 1: end]) < 3:
            del strings[end]
            del strings[start]

        if len(strings[start + 1: end]) > 2:
            temp: str = ' '.join(strings[start + 1: end])
            temp = process_duplicate_minus(temp)
            temp = process_math_expression(temp, ['*', '/'])
            temp_lst: list = [float(t) for t in temp.split() if t != '+']
            temp = str(sum(temp_lst))
            tmp_strings: list = strings[:start]
            tmp_strings.append(temp)
            if end < len(strings) - 1:
                tmp_strings += strings[end + 1:]
            strings = tmp_strings

    return ' '.join(strings)


def process_duplicate_minus(string: str) -> str:
    """
    Eliminate duplicate minus.

    :param string: str
    :return: str
    """
    done: bool = False
    strings: list = string.split(' ')

    while not done:
        done = True
        for i, s in enumerate(strings):

            if s == '-':
                if strings[i + 1] == '-':
                    done = False
                    strings[i] = '+'
                    del strings[i + 1]
                    break

                str_temp = [t.isdigit() for t in strings[i + 1]]
                if any(str_temp):
                    done = False
                    strings[i] = str(float(strings[i + 1]) * (-1))
                    del strings[i + 1]
                    break

            if s == '+':
                if strings[i + 1] == '-':
                    done = False
                    del strings[i]
                    break

    return ' '.join(strings)


def calc(string: str) -> float:
    """
    Calculate math expression from input string.

    :param string: str
    :return: float
    """
    string = ''.join([s for s in string if s != ' '])

    strings: list = []
    while string:
        temp: str = ''
        temp, string = check_conditions(strings, string, temp)
    string = ' '.join(strings)

    string = ''.join(string.split('+'))
    strings = string.split()
    string = process_brackets(strings)
    string = process_duplicate_minus(string)
    string = process_math_expression(string, ['*', '/'])
    string_lst: list = string.split(' ')
    string_lst = [float(s) for s in string_lst]
    string = str(sum(string_lst))
    return float(string)


def check_conditions(strings: list, string: str, temp: str) -> tuple[str, str]:
    """
    Test string normalization.

    Normalize string input by checking conditions.
    :param strings: list
    :param string: str
    :param temp: str
    :return: tuple(str, str)
    """
    for i, s in enumerate(string):
        if s.isdigit():
            temp += s

        if (s in ''.join(OPERATORS) + '()' or i == len(string) - 1) and temp:
            strings.append(temp)

        if s in '()':
            strings.append(s)

            if i + 1 < len(string):
                string = string[i + 1:]
            else:
                string = ''

            break

        if s in OPERATORS:
            strings.append(s)

            if i + 1 < len(string):
                string = string[i + 1:]

            break

        if i == len(string) - 1:
            string = ''

    return temp, string
