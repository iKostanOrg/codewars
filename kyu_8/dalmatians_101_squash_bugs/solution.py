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
        respond = dogs[0]
    elif number <= 50:
        respond = dogs[1]
    elif number == 101:
        respond = dogs[3]
    else:
        respond = dogs[2]

    return respond