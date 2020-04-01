#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from utils.manhattan_distance import get_manhattan_distance


class Cell:

    def __init__(self, coord: tuple, is_agent: bool, agents: list, n: int, DISTANCES):

        self.row = coord[0]
        self.column = coord[1]
        self.is_agent = is_agent

        if not self.is_agent:
            self.distance = self.__calc_distance(agents=agents, n=n)
        else:
            self.distance = 0

        self.__update_distances(DISTANCES)

    def __update_distances(self, DISTANCES) -> None:
        if self.distance in DISTANCES:
            DISTANCES[self.distance].append((self.row, self.column))
        else:
            DISTANCES[self.distance] = [(self.row, self.column)]

    def __calc_distance(self, agents: list, n: int) -> int:
        distance = None
        for agent in agents:
            if agent[0] < n and agent[1] < n:
                if not distance:
                    distance = get_manhattan_distance(coord_a=(self.row, self.column), coord_b=agent)
                else:
                    temp = get_manhattan_distance(coord_a=(self.row, self.column), coord_b=agent)
                    if temp < distance:
                        distance = temp
        return distance


def create_map(n: int, agents: list, COORDINATES, DISTANCES):

    for row in range(0, n):
        for col in range(0, n):
            # print("\nrow: {}, col: {}".format(row, col))
            is_agent = False
            if (row, col) in agents:
                is_agent = True
            Cell((row, col), is_agent, agents, n, DISTANCES)
            COORDINATES.append((row, col))


def advice(agents: list, n: int) -> list:
    """
    The function should return a list of coordinates that are the
    furthest away (by Manhattan distance) from all agents.

    Edge cases:
        - If there is an agent on every grid cell, there is no safe space, so return an empty list.
        - If there are no agents, then every cell is a safe spaces, so return all coordinates.
        - if n is 0, return an empty list.
        - If agent coordinates are outside of the map, they are simply not considered.
        - There are no duplicate agents on the same square.

    :param agents: is an array of agent coordinates
    :param n: defines the size of the city that Bassi needs to hide in,
    in other words the side length of the square grid
    :return:
    """
    DISTANCES = dict()
    COORDINATES = list()

    # if n is 0, return an empty list
    if n == 0:
        return list()

    # If there is an agent on every grid cell, there is no safe space,
    # so return an empty list
    if len(agents) == n * n and max(agents)[0] < n and max(agents)[1] < n:
        return list()

    # If there are no agents, then every cell is a safe spaces,
    # so return all coordinates
    if not agents:
        pass

    create_map(n, agents, COORDINATES, DISTANCES)

    for key in DISTANCES:
        print('\nkey: {},\n{}'.format(key, DISTANCES[key]))

    if DISTANCES:
        return DISTANCES[max(DISTANCES.keys())]
    else:
        return COORDINATES
