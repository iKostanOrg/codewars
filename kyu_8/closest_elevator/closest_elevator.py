"""
Solution for -> Closest elevator.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

def elevator(left: int, right: int, call: int) -> str:
    """
    Return closest elevator number.

    :param left: int
    :param right: int
    :param call: int
    :return: str
    """
    if right == left == call:
        return 'right'

    if left == call or abs(call - left) < abs(call - right):
        return 'left'

    return 'right'

