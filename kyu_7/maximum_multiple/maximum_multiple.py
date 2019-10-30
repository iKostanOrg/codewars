#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def max_multiple(divisor: int, bound: int) -> int:
    """
    Given a Divisor and a Bound , Find the
    largest integer N , Such That ,

    Conditions:
        1. N is divisible by divisor
        2. N is less than or equal to bound
        3. N is greater than 0.

    Notes:
        1. The parameters (divisor, bound)
            passed to the function are only positve values .
        2. It's guaranteed that a divisor is Found .
    :param divisor:
    :param bound:
    :return:
    """

    while bound > 0:
        if bound % divisor == 0:
            return bound
        bound -= 1
    return 0
