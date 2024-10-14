"""
Solution for -> A wolf in sheep's clothing
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def warn_the_sheep(queue: list) -> str:
    """
    Warn the sheep in front of the wolf
    that it is about to be eaten.

    If the wolf is the closest animal to you,
    return "Pls go away and stop eating my sheep".

    Otherwise, return "Oi! Sheep number N!
    You are about to be eaten by a wolf!"
    where N is the sheep's position in the queue.

    :param queue: list
    :return: str
    """
    warning: str = "Pls go away and stop eating my sheep"
    alert_start: str = "Oi! Sheep number "
    alert_end: str = "! You are about to be eaten by a wolf!"
    wolf: str = 'wolf'

    if queue[-1] == wolf:
        return warning
    else:
        index = len(queue) - queue.index(wolf) - 1

    return f'{alert_start}{index}{alert_end}'
