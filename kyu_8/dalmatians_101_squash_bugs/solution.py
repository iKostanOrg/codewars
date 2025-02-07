"""
Solution for -> # 101 Dalmatians - squash the bugs, not the dogs!.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

dogs: list = ["Hardly any",
              "More than a handful!",
              "Woah that's a lot of dogs!",
              "101 DALMATIONS!!!"]


def how_many_dalmatians(number: int) -> str:
    """
    Squash the bugs, not the dogs!.

    :param number: int
    :return: str
    """
    if number <= 10:
        return dogs[0]

    if number <= 50:
        return dogs[1]

    if number == 101:
        return dogs[3]

    return dogs[2]
