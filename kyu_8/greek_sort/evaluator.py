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
    val: bool = False

    if expected == '< 0':
        val = result < 0

    if expected == '== 0':
        val = result == 0

    if expected == '> 0':
        val = result > 0

    return val
