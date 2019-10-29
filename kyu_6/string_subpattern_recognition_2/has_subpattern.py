#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def has_subpattern(string: str) -> bool:
    """
    String subpattern recognition II

    if a subpattern has been used, it will be repeated at least twice,
    meaning the subpattern has to be shorter than the original string;

    the strings you will be given might or might not be created
    repeating a given subpattern, then shuffling the result.

    :param string:
    :return:
    """

    length = len(string)

    if length < 2:
        return False

    if len(set(string)) == 1:
        return True

    n = 2
    while n < (length // 2) + 1:

        if length % n != 0:
            n += 1
            continue

        if string[0:length // n] * n == string:
            return True
        n += 1

    return False
