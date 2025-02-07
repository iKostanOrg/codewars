"""
Solution for -> # 101 Dalmatians - squash the bugs, not the dogs!.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def how_many_dalmatians(number: int) -> str:
    """
    Squash the bugs, not the dogs!.

    :param number: int
    :return: str
    """
    dogs: list = ["Hardly any",
                  "More than a handful!",
                  "Woah that's a lot of dogs!",
                  "101 DALMATIONS!!!"]

    if number <= 10:
        return dogs[0]
    elif number <= 50:
        return dogs[1]
    elif number == 101:
        return dogs[3]
    else:
        return dogs[2]
