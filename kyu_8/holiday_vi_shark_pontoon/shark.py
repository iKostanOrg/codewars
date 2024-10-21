"""
Solution for -> Holiday VI - Shark Pontoon
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def shark(pontoon_distance,
          shark_distance,
          you_speed,
          shark_speed,
          dolphin) -> str:
    """
    You are given 5 variables: sharkDistance = distance the shark
    needs to cover to eat you in metres, sharkSpeed = how fast it
    can move in metres/second, pontoonDistance = how far you need
    to swim to safety in metres, youSpeed = how fast you can swim
    in metres/second, dolphin = a boolean, if true, you can half
    the swimming speed of the shark as the dolphin will attack it.

    If you make it, return "Alive!", if not, return "Shark Bait!".

    :param pontoon_distance:
    :param shark_distance:
    :param you_speed:
    :param shark_speed:
    :param dolphin:
    :return:
    """
    if dolphin:
        shark_speed = shark_speed / 2

    if pontoon_distance / you_speed < shark_distance / shark_speed:
        return "Alive!"

    return "Shark Bait!"
