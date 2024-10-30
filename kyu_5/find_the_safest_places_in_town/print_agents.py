"""
Prints city map with agents.
Use for debug purposes only.
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def print_map(agents: list, digit: int, expected: list) -> None:
    """
    Use for debug purposes only. Prints city map with agents (*)
    and expected results (longest distance as +) on it.

    :param agents: is an array of agent coordinates
    :param digit: defines the size of the city that Bassi needs to hide in,
                      in other words the side length of the square grid
    :param expected: expected results
    :return:
    """
    empty: str = ' |'
    agent: str = '-|'
    longest: str = '+|'

    for col in range(0, digit):
        temp = "|"
        for row in range(0, digit):
            if (row, col) in agents:
                temp += agent
            elif (row, col) in expected:
                temp += longest
            else:
                temp += empty
        print(temp)
