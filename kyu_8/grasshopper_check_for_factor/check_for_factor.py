"""
Solution for -> Grasshopper - Check for factor.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def check_for_factor(base: int, factor: int) -> bool:
    """
    Check if the factor is a factor of base.

    Factors are numbers you can multiply
    together to get another number.

    Return true if it is a factor or
    false if it is not.
    :param base: int
    :param factor: int
    :return: bool
    """
    return base % factor == 0
