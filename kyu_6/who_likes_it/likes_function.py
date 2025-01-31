"""
Solution for -> Who likes it?.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def likes(names: list) -> str:
    """
    Likes.

    A function which must take in input array, containing the
    names of people who like an item. It must return the
    display text.

    For 4 or more names, the number in and 2 others simply
    increases.

    :param names: input array, containing the names of people
                  who like an item
    :return: the display text
    """
    if not names:
        return 'no one likes this'

    if len(names) == 1:
        return f'{names[0]} likes this'

    if 1 < len(names) <= 3:
        return (f"{', '.join(names[:len(names) - 1])} and "
                f"{names[-1]} like this")

    return (f"{', '.join(names[:2])} and "
            f"{len(names) - 2} others like this")
