"""
Solution for -> Jaden Casing Strings.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def to_jaden_case(string: str) -> str:
    """
    Jaden Casing Strings.

    Convert strings to how they would be written by Jaden Smith.
    The strings are actual quotes from Jaden Smith, but they are
    not capitalized in the same way he originally typed them.

    Example.

    Not Jaden-Cased: "How can mirrors be real if
    our eyes aren't real"

    Jaden-Cased: "How Can Mirrors Be Real If
    Our Eyes Aren't Real"
    :param string:
    :return:
    """
    list_string: list = string.split()
    for i, el in enumerate(list_string):
        list_string[i] = el.capitalize()

    return ' '.join(list_string)
