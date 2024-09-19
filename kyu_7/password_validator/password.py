"""
Solution for -> Password validator
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def password(string: str) -> bool:
    """
    Your job is to create a simple password
    validation function, as seen on many websites.

    You are permitted to use any methods to
    validate the password.

    The rules for a valid password are as follows:

    1. There needs to be at least 1 uppercase letter.
    2. There needs to be at least 1 lowercase letter.
    3. There needs to be at least 1 number.
    4. The password needs to be at least 8 characters long.

    :param string:
    :return:
    """
    results: dict = {
        'uppercase': False,
        'lowercase': False,
        'number': False,
        'length': True if len(string) >= 8 else False}

    for char in string:
        if char.isdigit():
            results['number'] = True
        elif char.isalpha() and char.islower():
            results['lowercase'] = True
        elif char.isalpha() and char.isupper():
            results['uppercase'] = True
        elif all(results.values()):
            break

    return all(results.values())
