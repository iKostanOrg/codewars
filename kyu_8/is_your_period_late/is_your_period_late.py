"""
Solution for -> Is your period late
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

from datetime import date, timedelta


def period_is_late(last: date, today: date, cycle_length: int) -> bool:
    """
    Test whether a period is late.

    :param last: The Date object with the date of the last period
    :param today: The Date object with the date of the check
    :param cycle_length: Integer representing the length of the cycle in days
    :return: bool
    """
    delta: timedelta = today - last
    if int(delta.days) > cycle_length:
        return True
    return False
