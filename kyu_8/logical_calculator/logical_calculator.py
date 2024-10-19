"""
Solution for -> Logical Calculator
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def logical_calc(array: list, op: str) -> bool:
    """
    Calculates logical value of boolean array.

    Logical operations: AND, OR and XOR.

    Begins at the first value, and repeatedly
    apply the logical operation across the
    remaining elements in the array sequentially.

    :param array: list
    :param op: str
    :return: bool
    """
    logical: str = op.strip().upper()
    operators: list = ['AND', 'OR', 'XOR']
    result: bool = False

    # op param validation
    if logical not in operators:
        raise ValueError(f'ERROR: {op} is not a valid operator. '
                         f'Please use one of the followings: {operators}')

    # AND
    if logical == operators[0]:
        result = all(array)

    # OR
    if logical == operators[1]:
        result = any(array)

    # XOR
    if logical == operators[2]:
        result = array[0]
        i = 1

        while i < len(array):
            tmp = array[i]

            if result == tmp:
                result = False
            else:
                result = True

            i = i + 1

    return result
