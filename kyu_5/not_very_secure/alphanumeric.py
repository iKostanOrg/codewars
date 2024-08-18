#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan


def alphanumeric(password: str) -> bool:
    """
    The string has the following conditions to be alphanumeric:

    1. At least one character ("" is not valid)

    2. Allowed characters are uppercase or
    lowercase latin letters and digits from 0 to 9

    3. No whitespaces or underscore

    :param password: string
    :return: bool
    """

    if password == "":
        return False

    for char in password:
        if char.isalpha() or char.isdigit():
            continue
        return False

    return True
