"""
Solution for -> Battleship field validator.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def validate_battlefield(field: list) -> bool:
    """
    Validate battlefield.

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
        4: []}

    ship_counter_by_row(field, ships)
    ship_counter_by_col(field, ships)

    return all([len(ships[1]) == 4,
                len(ships[2]) == 3,
                len(ships[3]) == 2,
                len(ships[4]) == 1])


def ship_counter_by_row(field: list, ships: dict):
    """
    Ship counter by row.

    :param field: list
    :param ships: dict
    :return:
    """
    for index_row, row in enumerate(field):
        ship: list = []

        for cell in enumerate(row):
            if row[cell[0]] == 1:
                ship.append([index_row, cell[0]])
            else:
                # Allowed ship sizes between 1 and 4 cells
                if (len(ship) == 1 and all_cells_valid(ships=ships,
                                                       field=field,
                                                       direction='submarine',
                                                       ship=ship)):
                    ships[len(ship)].append(ship)
                elif (1 < len(ship) <= 4 and all_cells_valid(ships=ships,
                                                             field=field,
                                                             direction='horizontal',
                                                             ship=ship)):
                    ships[len(ship)].append(ship)

                ship = []

        # Allowed ship sizes between 1 and 4 cells
        if (len(ship) == 1 and all_cells_valid(ships=ships,
                                               field=field,
                                               direction='submarine',
                                               ship=ship)):
            ships[len(ship)].append(ship)
        elif (1 < len(ship) <= 4 and all_cells_valid(ships=ships,
                                                     field=field,
                                                     direction='horizontal',
                                                     ship=ship)):
            ships[len(ship)].append(ship)


def ship_counter_by_col(field: list, ships: dict):
    """
    Ship counter by col.

    :param field: list
    :param ships: dict
    :return:
    """
    for index_col in range(len(field[0])):
        ship: list = []
        for index_row, row in enumerate(field):
            if row[index_col] == 1:
                ship.append([index_row, index_col])
            else:
                # Allowed ship sizes between 1 and 4 cells
                if (len(ship) == 1 and all_cells_valid(ships=ships,
                                                       field=field,
                                                       direction='submarine',
                                                       ship=ship)):
                    ships[len(ship)].append(ship)
                elif (1 < len(ship) <= 4 and all_cells_valid(ships=ships,
                                                             field=field,
                                                             direction='vertical',
                                                             ship=ship)):
                    ships[len(ship)].append(ship)
                ship = []

        # Allowed ship sizes between 1 and 4 cells
        if (len(ship) == 1 and all_cells_valid(ships=ships,
                                               field=field,
                                               direction='submarine',
                                               ship=ship)):
            ships[len(ship)].append(ship)
        elif (1 < len(ship) <= 4 and all_cells_valid(ships=ships,
                                                     field=field,
                                                     direction='vertical',
                                                     ship=ship)):
            ships[len(ship)].append(ship)


def all_cells_valid(**kwargs):
    """
    Validate all cells.

    :param kwargs:
    :return:
    """
    return all(
        is_valid_cell(ships=kwargs['ships'],
                      field=kwargs['field'],
                      cell=cell,
                      direction=kwargs['direction']) for cell in kwargs['ship'])


def check_vertical(row, col, field) -> bool:
    """
    Verify vertical direction.

    :param row:
    :param col:
    :param field: list, board game "Battleship" (list)
    :return:
    """
    for row_id in range(row - 1, row + 2):
        for col_id in range(col - 1, col + 2):
            if 0 <= row_id < len(field) \
                    and 0 <= col_id < len(field) \
                    and col_id != col \
                    and field[row_id][col_id] == 1:
                return False
    return True


def check_horizontal(row, col, field) -> bool:
    """
    Verify horizontal direction.

    :param row:
    :param col:
    :param field: list, board game "Battleship" (list)
    :return:
    """
    for row_id in range(row - 1, row + 2):
        for col_id in range(col - 1, col + 2):
            if 0 <= row_id < len(field) \
                    and 0 <= col_id < len(field) \
                    and row_id != row \
                    and field[row_id][col_id] == 1:
                return False
    return True


def check_submarine(**kwargs) -> bool:
    """
    Check submarine.

    Check if submarine already in list (avoid duplicates)
    Validates if submarine cell has contacts with other ships/cells
    ships: dict, collection of valid ships (dict)
    field: list, board game "Battleship" (list)
    cell: list, candidate for single ship/submarine
    :return: bool
    """
    # check if submarine already in list (avoid duplicates)
    for submarine in kwargs['ships'][1]:
        if [kwargs['cell']] == submarine:
            return False

    # validates if submarine cell has contacts with other ships/cells
    for row_id in range(kwargs['row'] - 1, kwargs['row'] + 2):
        for col_id in range(kwargs['col'] - 1, kwargs['col'] + 2):
            if 0 <= row_id < len(kwargs['field']) \
                    and 0 <= col_id < len(kwargs['field']) \
                    and (col_id != kwargs['col'] or row_id != kwargs['row']) \
                    and kwargs['field'][row_id][col_id] == 1:
                return False
    return True


def is_valid_cell(**kwargs) -> bool:
    """
    Check if cell is valid.

    Validates if single cell result is valid
    (valid submarine or single ship cell)
    :return: bool
    """
    row, col = kwargs['cell'][0], kwargs['cell'][1]

    if kwargs['direction'] == 'submarine':
        if not check_submarine(row=row,
                               col=col,
                               ships=kwargs['ships'],
                               field=kwargs['field'],
                               cell=kwargs['cell']):
            return False
    elif kwargs['direction'] == 'horizontal':
        if not check_horizontal(row=row,
                                col=col,
                                field=kwargs['field']):
            return False
    elif kwargs['direction'] == 'vertical':
        if not check_vertical(row=row,
                              col=col,
                              field=kwargs['field']):
            return False

    return True
