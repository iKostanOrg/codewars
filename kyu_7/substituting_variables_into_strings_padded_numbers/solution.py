#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def solution(value: int) -> str:
    """
    Complete the solution so that it
    returns a formatted string.

    The return value should equal "Value
    is VALUE" where value is a 5 digit
    padded number.
    :param value:
    :return:
    """

    result = str(value)

    while len(result) != 5:
        result = '0' + result

    return 'Value is {}'.format(result)
