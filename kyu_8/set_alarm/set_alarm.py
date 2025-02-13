"""
Test for -> L1: Set Alarm.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def set_alarm(employed: bool, vacation: bool) -> bool:
    """
    'set_alarm' function.

    A function named setAlarm which receives two parameters.
    The first parameter, employed, is true whenever you are
    employed and the second parameter, vacation is true whenever
    you are on vacation.



    :param employed: bool
    :param vacation: bool
    :return: bool
    """
    if employed and not vacation:
        return True
    return False
