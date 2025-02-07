"""
Solution for -> Decipher this!.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def last_digit_index(word: str) -> int:
    """
    Find last digit index.

    :param word:
    :return:
    """
    index: int = 0
    for char in word:
        if char.isdigit():
            index += 1
        else:
            break
    return index


def decipher_this(string: str) -> str:
    """
    Given a secret message that you need to decipher.

    For each word:
     * the second and the last letter is switched (e.g. Hello becomes Holle)
     * the first letter is replaced by its character code (e.g. H becomes 72)

    Note: there are no special characters used, only letters and spaces

    :param string:
    :return:
    """
    if not string:
        return ""

    results: list = []
    for word in string.split(' '):
        last_digit: int = last_digit_index(word)
        char: str = chr(int(word[0: last_digit]))

        if len(word[last_digit:]) == 0:
            results.append(f"{char}")
        elif len(word[last_digit:]) == 1:
            results.append(f"{char}{word[last_digit:]}")
        elif len(word[last_digit:]) == 2:
            results.append(f"{char}{word[-1]}{word[last_digit]}")
        else:
            results.append(f"{char}"
                           f"{word[-1]}"
                           f"{word[last_digit + 1: -1]}"
                           f"{word[last_digit]}")

    return ' '.join(results)
