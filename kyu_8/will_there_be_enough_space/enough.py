"""
Solution for -> Will there be enough space?
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

def enough(cap: int, on: int, wait: int) -> int:
    """
    The driver wants you to write a simple program telling him if
    he will be able to fit all the passengers.

    If there is enough space, return 0, and if there isn't,
    return the number of passengers he can't take.

    You have to write a function that accepts three parameters:

    cap is the amount of people the bus can hold excluding the driver.
    on is the number of people on the bus.
    wait is the number of people waiting to get on to the bus.

    :param cap:
    :param on:
    :param wait:
    :return:
    """
    if cap - on < wait:
        return wait - (cap - on)
    return 0
