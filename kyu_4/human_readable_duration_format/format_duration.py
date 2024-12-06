"""
Format duration.

A function which formats a duration, given as a
number of seconds, in a human-friendly way.
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def format_duration(seconds: int) -> str:
    """
    format_duration function.

    A function which formats a duration, given as a
    number of seconds, in a human-friendly way.

    The resulting expression is made of components like 4 seconds,
    1 year, etc. In general, a positive integer and one of the
    valid units of time, separated by a space. The unit of time
    is used in plural if the integer is greater than 1.

    The components are separated by a comma and a space (", ").
    Except the last component, which is separated by " and ", just
    like it would be written in English.

    A more significant units of time will occur before than a least
    significant one. Therefore, 1 second and 1 year is not correct,
    but 1 year and 1 second is.

    Different components have different unit of times. So there is
    not repeated units like in 5 seconds and 1 second.

    A component will not appear at all if its value happens to be zero.
    Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

    A unit of time must be used "as much as possible". It means that the
    function should not return 61 seconds, but 1 minute and 1 second instead.
    Formally, the duration specified by of a component must not be greater than
    any valid more significant unit of time.

    :param seconds: int
    :return: str
    """

    if seconds == 0:
        return 'now'

    result: str = ''

    years: int = calc_years(seconds)
    days: int = calc_days(seconds)
    hours: int = calc_hours(seconds)
    minutes: int = calc_minutes(seconds)
    seconds = calc_seconds(seconds)

    year: str = get_string(years, 'year')
    day: str = get_string(days, 'day')
    hour: str = get_string(hours, 'hour')
    minute: str = get_string(minutes, 'minute')
    second: str = get_string(seconds, 'second')

    if years > 0:
        result += f'{year}'

    result = format_days(days, day, result)
    result = format_hours(hours, hour, result)
    result = format_minutes(minutes, seconds, minute, result)
    result = format_seconds(seconds, second, result)

    return result


def format_days(days: int,
                day: str,
                result: str) -> str:
    """
    Format days for the final string.

    :param days: int
    :param day: str
    :param result: str
    :return: str
    """
    if days > 0:
        result += f', {day}' if result else f'{day}'

    return result


def format_hours(hours: int,
                 hour: str,
                 result: str) -> str:
    """
    Format hours for the final string.

    :param hours: int
    :param hour: str
    :param result: str
    :return: str
    """
    if hours > 0:
        result += f', {hour}' if result else f'{hour}'

    return result


def format_minutes(minutes: int,
                   seconds: int,
                   minute: str,
                   result: str) -> str:
    """
    Format minutes for the final string.

    :param minutes: int
    :param seconds: int
    :param minute: str
    :param result: str
    :return: str
    """
    if minutes > 0 and result != '' and seconds == 0:
        result += f' and {minute}'
    elif minutes > 0 and result != '':
        result += f', {minute}'
    else:
        result += f'{minute}'

    return result


def format_seconds(seconds: int, second: str, result: str) -> str:
    """
    Format seconds for the final string.

    :param seconds: int
    :param second: str
    :param result: str
    :return: str
    """
    if seconds > 0:
        result += f' and {second}' if result else f'{second}'

    return result


def get_string(number: int,
               string: str) -> str:
    """
    Concatenate string result.

    :param number: int
    :param string: str
    :return: str
    """
    result: str = ''
    if number == 1:
        result = f'{number} {string}'
    elif number > 0:
        result = f'{number} {string}s'

    return result


def calc_seconds(seconds: int) -> int:
    """
    Calculate seconds.

    :param seconds: int
    :return: int
    """
    return seconds if seconds < 60 else seconds % 60


def calc_minutes(seconds: int) -> int:
    """
    Calculate minutes.

    :param seconds: int
    :return: int
    """
    minutes = seconds // 60
    return minutes if minutes < 60 else minutes % 60


def calc_hours(seconds: int) -> int:
    """
    Calculate hours.

    :param seconds: int
    :return: int
    """
    hours = seconds // (60 * 60)
    return hours if hours < 24 else hours % 24


def calc_days(seconds: int) -> int:
    """
    Calculate days.

    :param seconds: int
    :return: int
    """
    days = seconds // (60 * 60 * 24)
    return days if days < 365 else days % 365


def calc_years(seconds: int) -> int:
    """
    Calculate years.

    :param seconds: int
    :return: int
    """
    return seconds // (60 * 60 * 24 * 365)
