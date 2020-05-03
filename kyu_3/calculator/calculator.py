#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


class Calculator:
    """
    calculator that given a string of operators
    (), +, -, *, / and numbers separated by spaces
    returns the value of that expression
    """

    def __calculate_multiplications_and_divisions(self, string: str) -> str:
        """
        Perform all operation with multiplications and divisions

        :param string: input string
        :return: output string with no '*' or '/'
        """
        strings = string.split(' ')

        while '*' in strings or '/' in strings:
            for i, char in enumerate(strings):

                if char == '*':
                    a = float(strings[i - 1])
                    b = float(strings[i + 1])
                    strings[i] = str(self.__multiplication(a, b))
                    del strings[i + 1]
                    del strings[i - 1]
                    break

                if char == '/':
                    a = float(strings[i - 1])
                    b = float(strings[i + 1])
                    strings[i] = str(self.__division(a, b))
                    del strings[i + 1]
                    del strings[i - 1]
                    break

        return ' '.join(strings)

    def __calculate_additions_and_subtractions(self, string: str) -> str:
        """
        Perform all operation with addition and subtraction

        :param string: input string
        :return: output string with no '+' or '-'
        """
        strings = string.split(' ')

        while '+' in strings or '-' in strings:
            for i, char in enumerate(strings):

                if char == '+':
                    a = float(strings[i - 1])
                    b = float(strings[i + 1])
                    strings[i] = str(self.__addition(a, b))
                    del strings[i + 1]
                    del strings[i - 1]
                    break

                if char == '-':
                    a = float(strings[i - 1])
                    b = float(strings[i + 1])
                    strings[i] = str(self.__subtraction(a, b))
                    del strings[i + 1]
                    del strings[i - 1]
                    break

        return ''.join(strings)

    @staticmethod
    def __process_string(string: str) -> str:
        """
        Remove all white spaces

        :param string: input string
        :return: string with no white spaces
        """
        return ''.join(s for s in string if s != ' ')

    def evaluate(self, string: str) -> float:
        """
        Returns value of the given expression

        :param string: a string of operators (), +, -, *, /
                       and numbers separated by spaces
        :return: calculated value of the given expression
        """
        string: str = self.__calculate_multiplications_and_divisions(string)
        result: str = self.__calculate_additions_and_subtractions(string)
        return float(result)

    @staticmethod
    def __addition(a: float, b: float) -> float:
        """
        Additions have a lower priority and
        should be performed left-to-right

        :param a: number in float format
        :param b: number in float format
        :return: a + b
        """
        return a + b

    @staticmethod
    def __subtraction(a: float, b: float) -> float:
        """
        Subtractions have a lower priority and
        should be performed left-to-right

        :param a: number in float format
        :param b: number in float format
        :return: a - b
        """
        return a - b

    @staticmethod
    def __multiplication(a: float, b: float) -> float:
        """
        Multiplications have a higher priority and
        should be performed left-to-right

        :param a: number in float format
        :param b: number in float format
        :return: a * b
        """
        return a * b

    @staticmethod
    def __division(a: float, b: float) -> float:
        """
        Divisions have a higher priority and
        should be performed left-to-right

        :param a: number in float format
        :param b: number in float format
        :return: a / b
        """
        return a / b
