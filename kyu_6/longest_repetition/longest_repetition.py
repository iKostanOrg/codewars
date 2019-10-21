#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def longest_repetition(chars):
    """
    For a given string s find the character c (or C)
    with longest consecutive repetition and return: (c, l)

    where l (or L) is the length of the repetition.
    If there are two or more characters with
    the same l return the first.

    For empty string return: ('', 0)
    :param chars:
    :return:
    """

    result = ('', 0)
    current = ['', 0]

    for c in chars:

        if c == current[0]:
            current[1] += 1
        else:
            current = [c, 1]

        if current[1] > result[1]:
            result = (c, current[1])

    return result
