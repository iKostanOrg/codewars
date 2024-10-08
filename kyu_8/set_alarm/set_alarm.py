"""
Test for -> L1: Set Alarm
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def set_alarm(employed: bool, vacation: bool) -> bool:
    """
    A function named setAlarm which receives two parameters.
    The first parameter, employed, is true whenever you are
    employed and the second parameter, vacation is true whenever
    you are on vacation.

    The function should return true if you are employed and
    not on vacation (because these are the circumstances under
    which you need to set an alarm). It should return false
    otherwise.

    Examples:

    setAlarm(true, true) -> false
    setAlarm(false, true) -> false
    setAlarm(false, false) -> false
    setAlarm(true, false) -> true

    :param employed: bool
    :param vacation: bool
    :return: bool
    """

    if employed and not vacation:
        return True
    return False
