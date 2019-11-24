#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def growing_plant(upSpeed, downSpeed, desiredHeight) -> int:
    """
    Each day a plant is growing by upSpeed meters. Each night
    that plant's height decreases by downSpeed meters due to the
    lack of sun heat. Initially, plant is 0 meters tall. We plant
    the seed at the beginning of a day. We want to know when the
    height of the plant will reach a certain level.
    :param upSpeed:
    :param downSpeed:
    :param desiredHeight:
    :return:
    """

    height = 0
    days = 0

    while height <= desiredHeight:
        height += upSpeed
        days += 1

        if height >= desiredHeight:
            return days

        height -= downSpeed

    return days
