"""
Solution -> Keep up the hoop
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def hoop_count(n) -> str:
    """
    A program where Alex can input (n) how many times the
    hoop goes round and it will return him an encouraging message
    
    :param n: int
    :return: str
    """

    if n < 10:
        return "Keep at it until you get it"

    return "Great, now move on to tricks"
