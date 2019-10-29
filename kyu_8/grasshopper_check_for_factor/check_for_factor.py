#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def check_for_factor(base, factor):
    """
    This function should test if the
    factor is a factor of base.

    Factors are numbers you can multiply
    together to get another number.

    Return true if it is a factor or
    false if it is not.
    :param base:
    :param factor:
    :return:
    """

    return True if base % factor == 0 else False
