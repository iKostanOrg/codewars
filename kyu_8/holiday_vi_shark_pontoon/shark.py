#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def shark(pontoonDistance,
          sharkDistance,
          youSpeed,
          sharkSpeed,
          dolphin) -> str:
    """
    You are given 5 variables: sharkDistance = distance the shark
    needs to cover to eat you in metres, sharkSpeed = how fast it
    can move in metres/second, pontoonDistance = how far you need
    to swim to safety in metres, youSpeed = how fast you can swim
    in metres/second, dolphin = a boolean, if true, you can half
    the swimming speed of the shark as the dolphin will attack it.

    If you make it, return "Alive!", if not, return "Shark Bait!".

    :param pontoonDistance:
    :param sharkDistance:
    :param youSpeed:
    :param sharkSpeed:
    :param dolphin:
    :return:
    """

    if dolphin:
        sharkSpeed = sharkSpeed / 2

    if pontoonDistance / youSpeed < sharkDistance / sharkSpeed:
        return "Alive!"

    return "Shark Bait!"
