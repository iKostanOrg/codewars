"""
Solution for -> Calculator

Create a simple calculator that given a string
of operators '(), +, -, *, /' and numbers separated
by spaces returns the value of that expression

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


class Calculator:
    """
    Given string of operators '(), +, -, *, /'
    and numbers separated by spaces.
    Returns the value of that expression.
    """

    @staticmethod
    def __calculate(i: int, char: str, strings: list):
        """
        1. Perform math operation
        2. Reorganize math expression

        :param i:'char (math operation) index'
        :param char:'math operation'
        :param strings:'math expression'
        :return:'result'
        """

        a = float(strings[i - 1])
        b = float(strings[i + 1])

        if char == '*':
            strings[i] = str(a * b)

        if char == '/':
            strings[i] = str(a / b)

        if char == '+':
            strings[i] = str(a + b)

        if char == '-':
            strings[i] = str(a - b)

        del strings[i + 1]
        del strings[i - 1]

    def __process_math_expression(self, string: str, operators: list) -> str:
        """
        Perform all operation with:
        multiplications, divisions, additions and subtractions

        :param string: input string
        :return: output string with no '*', '/', '+', '-'
        """
        strings = string.split(' ')

        while any((True if s in operators else False) for s in strings):
            for i, char in enumerate(strings):
                if char in operators:
                    self.__calculate(i, char, strings)
                    break

        print(strings)
        return ' '.join(strings)

    def evaluate(self, string: str) -> float:
        """
        Returns value of the given expression

        :param string: a string of operators (), +, -, *, /
                       and numbers separated by spaces
        :return: calculated value of the given expression
        """
        string = self.__process_math_expression(string, ['*', '/'])
        result: str = self.__process_math_expression(string, ['+', '-'])
        return float(result)
