"""
Solution -> Simple Fun #74: Growing Plant
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def growing_plant(up_speed: int, down_speed:int, desired_height: int) -> int:
    """
    Each day a plant is growing by upSpeed meters. Each night
    that plant's height decreases by downSpeed meters due to the
    lack of sun heat. Initially, plant is 0 meters tall. We plant
    the seed at the beginning of a day. We want to know when the
    height of the plant will reach a certain level.

    :param up_speed: int
    :param down_speed: int
    :param desired_height: int
    :return: int
    """

    height: int = 0
    days: int = 0

    while height <= desired_height:
        height += up_speed
        days += 1

        if height >= desired_height:
            return days

        height -= down_speed

    return days
