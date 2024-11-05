"""
Solution for -> Human Readable Time
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


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

    hours_str = time_converter(hours)
    minutes_str = time_converter(minutes)
    seconds_str = time_converter(seconds)

    result: str = f'{hours_str}:{minutes_str}:{seconds_str}'
    return result


def time_converter(time: int) -> str:
    """
    Format time (hours, minutes, seconds) into string
    :param time: int
    :return: str
    """
    if time == 0:
        time_str: str = '00'
    elif len(str(time)) > 1:
        time_str = str(time)
    else:
        time_str = '0' + str(time)

    return time_str
