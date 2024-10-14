"""
Evaluates the expression
"""


def evaluator(result: int, expected: str) -> bool:
    """
    Evaluator
    :param result: int
    :param expected: str
    :return: bool
    """
    if expected == '< 0':
        return result < 0
    elif expected == '== 0':
        return result == 0
    elif expected == '> 0':
        return result > 0
