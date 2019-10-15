#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def greet(name, owner) -> str:
    """
    Function that gives a personalized greeting.
    This function takes two parameters: name and owner.

    :param name:
    :param owner:
    :return:
    """

    if name.lower() == owner.lower():
        return 'Hello boss'

    return 'Hello guest'
