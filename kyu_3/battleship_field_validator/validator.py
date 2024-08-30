"""
Solution for -> Battleship field validator

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def validate_battlefield(field: list) -> bool:
    """
    A method that takes a field for well-known board game "Battleship"
    as an argument and returns true if it has a valid disposition of ships,
    false otherwise. Argument is guaranteed to be 10*10 two-dimension array.
    Elements in the array are numbers, 0 if the cell is free
    and 1 if occupied by ship.

    :param field: 2D list,  board game "Battleship"
    :return: bool, true if there is a valid disposition of ships
    """
    counters: list = [row.count(1) for row in field]
    if sum(counters) != 20:
        return False

    ships: dict = {
        1: [],
        2: [],
        3: [],
        4: [],
    }

    ship_counter_by_row(field, ships)
    ship_counter_by_col(field, ships)

    return len(ships[1]) == 4 and len(ships[2]) == 3 and len(ships[3]) == 2 and len(ships[4]) == 1


def ship_counter_by_row(field: list, ships: dict):
    """
    Ship counter by row

    :param field: list
    :param ships: dict
    :return:
    """
    for index_row, row in enumerate(field):
        ship: list = []
        for index_col, cell in enumerate(row):
            if row[index_col] == 1:
                ship.append([index_row, index_col])
            else:
                # Allowed ship sizes between 1 to 4 cells
                if len(ship) == 1 and all(is_valid_cell(ships=ships,
                                                        field=field,
                                                        cell=cell,
                                                        direction='submarine') for cell in ship):
                    ships[len(ship)].append(ship)
                elif 1 < len(ship) <= 4:
                    if all(is_valid_cell(ships=ships,
                                         field=field,
                                         cell=cell,
                                         direction='horizontal') for cell in ship):
                        ships[len(ship)].append(ship)
                ship: list = []

        # Allowed ship sizes between 1 to 4 cells
        if len(ship) == 1 and all(is_valid_cell(ships=ships,
                                                field=field,
                                                cell=cell,
                                                direction='submarine') for cell in ship):
            ships[len(ship)].append(ship)
        elif 1 < len(ship) <= 4 and all(is_valid_cell(ships=ships,
                                                      field=field,
                                                      cell=cell,
                                                      direction='horizontal') for cell in ship):
            ships[len(ship)].append(ship)


def ship_counter_by_col(field: list, ships: dict):
    """
    Ship counter by col

    :param field: list
    :param ships: dict
    :return:
    """
    for index_col in range(0, len(field[0])):
        ship: list = []
        for index_row, row in enumerate(field):
            if row[index_col] == 1:
                ship.append([index_row, index_col])
            else:
                # Allowed ship sizes between 1 to 4 cells
                if len(ship) == 1 and all(is_valid_cell(ships=ships,
                                                        field=field,
                                                        cell=cell,
                                                        direction='submarine') for cell in ship):
                    ships[len(ship)].append(ship)
                elif 1 < len(ship) <= 4:
                    if all(is_valid_cell(ships=ships,
                                         field=field,
                                         cell=cell,
                                         direction='vertical') for cell in ship):
                        ships[len(ship)].append(ship)
                ship: list = []

        # Allowed ship sizes between 1 to 4 cells
        if len(ship) == 1 and all(is_valid_cell(ships=ships,
                                                field=field,
                                                cell=cell,
                                                direction='submarine') for cell in ship):
            ships[len(ship)].append(ship)
        elif 1 < len(ship) <= 4 and all(is_valid_cell(ships=ships,
                                                      field=field,
                                                      cell=cell,
                                                      direction='vertical') for cell in ship):
            ships[len(ship)].append(ship)


def is_valid_cell(**kwargs) -> bool:
    """
    Validates if single cell result is valid
    (valid submarine or single ship cell)

    :param ships: dict, collection of valid ships (dict)
    :param field: list, board game "Battleship" (list)
    :param cell: list, candidate for single ship/submarine
    :param direction: str, horizontal, vertical, submarine
    :return: bool
    """
    row, col = kwargs['cell'][0], kwargs['cell'][1]

    if kwargs['direction'] == 'submarine':

        # check if submarine already in list (avoid duplicates)
        for submarine in kwargs['ships'][1]:
            if [kwargs['cell']] == submarine:
                return False

        # validates if submarine cell has contacts with other ships/cells
        for row_id in range(row - 1, row + 2):
            for col_id in range(col - 1, col + 2):
                if (((0 <= row_id < len(kwargs['field'])) and (0 <= col_id < len(kwargs['field'])))
                        and ((col_id != col or row_id != row) and kwargs['field'][row_id][col_id] == 1)):
                    return False

    if kwargs['direction'] == 'horizontal':
        for row_id in range(row - 1, row + 2):
            for col_id in range(col - 1, col + 2):
                if (((0 <= row_id < len(kwargs['field'])) and (0 <= col_id < len(kwargs['field'])))
                        and ((row_id != row) and kwargs['field'][row_id][col_id] == 1)):
                    return False

    if kwargs['direction'] == 'vertical':
        for row_id in range(row - 1, row + 2):
            for col_id in range(col - 1, col + 2):
                if (((0 <= row_id < len(kwargs['field'])) and (0 <= col_id < len(kwargs['field'])))
                        and ((col_id != col) and kwargs['field'][row_id][col_id] == 1)):
                    return False

    return True
