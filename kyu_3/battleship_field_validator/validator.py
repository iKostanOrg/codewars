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
    Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

    :param field: board game "Battleship" (2D list)
    :return: returns true if it has a valid disposition of ships, false otherwise
    """
    if sum([row.count(1) for row in field]) != 20:
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
    # ship counter by row
    for index_row, row in enumerate(field):
        ship: list = []
        for index_col, cell in enumerate(row):
            if field[index_row][index_col] == 1:
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
                    else:
                        return False
                ship = []

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
    # ship counter by col
    for index_col in range(0, len(field[0])):
        ship: list = list()
        for index_row, row in enumerate(field):
            if field[index_row][index_col] == 1:
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
                    else:
                        return False
                ship = []

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


def is_valid_cell(ships: dict, field: list, cell: list, direction: str) -> bool:
    """
    Validates if single cell result is valid
    (valid submarine or single ship cell)

    :param ships: collection of valid ships (dict)
    :param field: board game "Battleship" (list)
    :param cell: candidate for single ship/submarine
    :param direction: str -> horizontal, vertical, submarine
    :return:
    """
    row, col = cell[0], cell[1]

    if direction == 'submarine':

        # check if submarine already in list (avoid duplicates)
        for submarine in ships[1]:
            if [cell] == submarine:
                return False

        # validates if submarine cell has contacts with other ships/cells
        for row_id in range(row - 1, row + 2):
            for col_id in range(col - 1, col + 2):
                if (0 <= row_id < len(field)) and (0 <= col_id < len(field)):
                    if (col_id != col or row_id != row) and field[row_id][col_id] == 1:
                        return False

    if direction == 'horizontal':
        for row_id in range(row - 1, row + 2):
            for col_id in range(col - 1, col + 2):
                if (0 <= row_id < len(field)) and (0 <= col_id < len(field)):
                    if (row_id != row) and field[row_id][col_id] == 1:
                        return False

    if direction == 'vertical':
        for row_id in range(row - 1, row + 2):
            for col_id in range(col - 1, col + 2):
                if (0 <= row_id < len(field)) and (0 <= col_id < len(field)):
                    if (col_id != col) and field[row_id][col_id] == 1:
                        return False

    return True
