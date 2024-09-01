#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan


def make_readable(seconds: int) -> str:
    """
    Write a function, which takes a non-negative integer
    (seconds) as input and returns the time in a
    human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

    The maximum time never exceeds 359999 (99:59:59)
    :param seconds:
    :return:
    """

    hours = seconds // (60 * 60)
    minutes = (seconds - (hours * 60 * 60)) // 60
    seconds = seconds - (hours * 60 * 60) - (minutes * 60)

    if hours == 0:
        hours_str: str = '00'
    else:
        if len(str(hours)) > 1:
            hours_str = str(hours)
        else:
            hours_str = '0' + str(hours)

    if minutes == 0:
        minutes_str: str = '00'
    else:
        if len(str(minutes)) > 1:
            minutes_str = str(minutes)
        else:
            minutes_str = '0' + str(minutes)

    if seconds == 0:
        seconds_str: str = '00'
    else:
        if len(str(seconds)) > 1:
            seconds_str = str(seconds)
        else:
            seconds_str = '0' + str(seconds)

    result: str = '{}:{}:{}'.format(
        hours_str,
        minutes_str,
        seconds_str
    )

    return result
