#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def litres(time) -> int:
    """
    Because Nathan knows it is important to stay hydrated,
    he drinks 0.5 litres of water per hour of cycling.

    You get given the time in hours and you need to return
    the number of litres Nathan will drink, rounded
    to the smallest value.
    :param time:
    :return:
    """

    return int(time * 0.5)
