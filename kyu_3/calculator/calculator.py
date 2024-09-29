"""
Solution for -> Calculator
Create a simple calculator that given a string
of operators '()', '+', '-', '*', '/'  and numbers separated
by spaces returns the value of that expression.
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


class Calculator:
    """
    Given string of operators '()', '+', '-', '*', '/'
    and numbers separated by spaces.
    Returns the value of that expression.
    """

    def __init__(self):
        self.__string = None
        self.__result = None

    @property
    def result(self) -> float:
        """
        1. Set result value by converting
        string value to a float
        2. Return result value
        
        :return: float
        """
        self.__result = float(self.__string)
        return self.__result

    @staticmethod
    def __calculate(i: int, char: str, strings: list):
        """
        1. Perform math operation
        2. Reorganize math expression

        :param i: (int) math operation index
        :param char: (str) math operation
        :param strings: (list) math expression
        :return: None
        """

        a: float = float(strings[i - 1])
        b: float = float(strings[i + 1])

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
        Perform all operation with multiplications, divisions, additions and subtractions
        :param string: str, input string
        :param operators: list, contains math operators
        :return: str, output string with no ‘*’, ‘/’, ‘+’, ‘-‘
        """
        strings: list = string.split(' ')

        while any((s in operators) for s in strings):
            for i, char in enumerate(strings):
                if char in operators:
                    self.__calculate(i, char, strings)
                    break

        return ' '.join(strings)

    def evaluate(self, string: str) -> float:
        """
        Returns value of the given expression
        :param string: str, input string to evaluate
        :return: (float) result
        """
        self.__string: str = string
        self.__string: str = self.__process_math_expression(self.__string,
                                                            ['*', '/'])
        self.__string: str = self.__process_math_expression(self.__string,
                                                            ['+', '-'])
        return self.result
