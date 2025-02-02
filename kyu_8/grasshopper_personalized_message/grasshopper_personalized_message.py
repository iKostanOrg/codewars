"""
Solution for -> Personalized greeting.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def greet(name: str, owner: str) -> str:
    """
    Return a personalized greeting.

    This function takes two parameters: name and owner.
    :param name: str
    :param owner: str
    :return:
    """
    if name.lower() == owner.lower():
        return 'Hello boss'

    return 'Hello guest'
