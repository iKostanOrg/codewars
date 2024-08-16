"""
Solution for -> Will you make it?
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def zero_fuel(distance_to_pump: int, mpg: int, fuel_left: int) -> bool:
    """
    You were camping with your friends far away from home,
    but when it's time to go back, you realize that you fuel
    is running out and the nearest pump is 50 miles away!
    You know that on average, your car runs on about 25 miles
    per gallon. There are 2 gallons left. Considering these
    factors, write a function that tells you if it is possible
    to get to the pump or not. Function should return true
    (1 in Prolog) if it is possible and false (0 in Prolog)
    if not. The input values are always positive.

    :param distance_to_pump: int
    :param mpg: int
    :param fuel_left: int
    :return: bool
    """
    return distance_to_pump <= mpg * fuel_left
