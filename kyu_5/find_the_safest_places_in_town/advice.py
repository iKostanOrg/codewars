"""
Solution for -> Find the safest places in town
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def create_city_map(n: int) -> set:
    """
    Generate city map with coordinates
    :param:n defines the size of the city that Bassi needs to hide in
    :return:set
    """
    return set((row, col) for row in range(0, n) for col in range(0, n))


def agents_cleanup(agents, n) -> set:
    """
    Remove all agents that are outside of the city boundaries.
    If agent coordinates are outside of the map, they are simply not considered.
    :param agents: array of agent coordinates
    :param n: defines the size of the city that Bassi needs to hide in
    :return:
    """
    return set(agent for agent in agents if agent[0] < n and agent[1] < n)


def city_map_processing(city: set, agents: set) -> None:
    """
    :param city: the full city map (set)
    :param agents: is an set of agent coordinates.
    :return:
    """
    while agents and city > agents:
        # Remove all agents from city map
        city -= agents
        # print('\nCITY\n', city)  # debug only
        temp = set()
        # Recalculate distance from each agent
        for x, y in agents:
            # Manhattan distance kind a calculation
            for pos in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if pos in city:
                    temp.add(pos)
        agents = temp


def advice(agents: set, n: int) -> list:
    """
    The function should return a list of coordinates that are the
    furthest away (by Manhattan distance) from all agents.
    Edge cases
    - If there is an agent on every grid cell, there is no safe space, so return an empty list.
    - If there are no agents, then every cell is a safe spaces, so return all coordinates.
    - if n is 0, return an empty list.
    - If agent coordinates are outside of the map, they are simply not considered.
    - There are no duplicate agents on the same square.
    :param agents: is an array of agent coordinates
    :param n: defines the size of the city that Bassi needs to hide in
    :return:
    """
    # if n is 0, return an empty list
    if n == 0:
        return []

    # If agent coordinates are outside of the map, they are simply not considered.
    # There are no duplicate agents on the same square.
    agents = agents_cleanup(agents, n)

    # If there is an agent on every grid cell, there is no safe space,
    # so return an empty list
    if len(agents) == n * n:
        return []

    # If there are no agents, then every cell is a safe spaces,
    # so return all coordinates
    city = create_city_map(n)
    if not agents:
        return list(city)

    city_map_processing(city, agents)

    return list(city)
