#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from kyu_5.find_the_safest_places_in_town.manhattan_distance import get_manhattan_distance


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

        if DISTANCES:
            max_distance = max(DISTANCES.keys())

            if self.distance > max_distance:
                DISTANCES[self.distance] = [(self.row, self.column)]
            elif self.distance == max_distance:
                DISTANCES[self.distance].append((self.row, self.column))

            new_max_distance = max(DISTANCES.keys())
            keys = list(DISTANCES.keys())

            for key in keys:
                if key < new_max_distance:
                    del DISTANCES[key]

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
