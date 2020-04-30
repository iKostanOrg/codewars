#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def likes(names: list) -> str:
    """
    A function which must take in input array, containing the names of people
    who like an item. It must return the display text.

    For 4 or more names, the number in and 2 others simply increases.

    :param names: input array, containing the names of people who like an item
    :return: the display text
    """
    if not names:
        return 'no one likes this'

    if len(names) == 1:
        return '{} likes this'.format(names[0])

    if 1 < len(names) <= 3:
        return '{} and {} like this'.format(', '.join(names[:len(names) - 1]), names[-1])

    if len(names) > 3:
        return '{} and {} others like this'.format(', '.join(names[:2]), len(names) - 2)
