
"""
Solution for -> Make a spiral.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


DIRECTIONS: dict = {
    'right': 'down',
    'down': 'left',
    'left': 'up',
    'up': 'right'
}


def right(spiral: list, coordinates: dict) -> bool:
    """
    Move spiral right.

    :param coordinates: starting point
    :param spiral: NxN spiral 2D array
    :return: boolean 'done'
    """
    done: bool = True

    while coordinates['col'] < len(spiral[coordinates['row']]):

        row = coordinates['row']
        col = coordinates['col']

        if col == len(spiral[0]) - 1 and \
                spiral[row][col] == 0:
            spiral[row][col] = 1
            done = False
            break

        if col + 1 == len(spiral[0]) - 1 and \
                spiral[row][col + 1] == spiral[row][col] == 0:
            spiral[row][col] = 1
            coordinates['col'] += 1
            done = False
        elif (col + 2 == len(spiral[0]) - 1 and
              spiral[row][col + 2] == spiral[row][col + 1] == spiral[row][col] == 0):
            spiral[row][col] = 1
            coordinates['col'] += 1
            done = False
        elif col + 2 == len(spiral[0]) - 1 and \
                spiral[row][col + 2] == 1 and \
                spiral[row][col + 1] == spiral[row][col] == 0:
            spiral[row][col] = 1
            done = False
            break
        elif (col + 2 < len(spiral[0]) - 1 and
              spiral[row][col + 2] == 1 and
              spiral[row][col + 1] == spiral[row][col] == 0
              and col + 2 < len(spiral[0])
              and spiral[row + 1][col] != 1):
            spiral[row][col] = 1
            done = False
            break
        elif (col + 2 < len(spiral[0]) - 1 and
              spiral[row][col + 2] == spiral[row][col + 1] == spiral[row][col] == 0
              and col + 2 < len(spiral[0])):
            spiral[row][col] = 1
            coordinates['col'] += 1
            done = False
        else:
            break

    return done


def down(spiral: list, coordinates: dict) -> bool:
    """
    Move spiral down.

    :param coordinates: starting point
    :param spiral: NxN spiral 2D array
    :return: boolean 'done'
    """
    done: bool = True

    while coordinates['row'] < len(spiral):

        row = coordinates['row']
        col = coordinates['col']

        if row == len(spiral) - 1 and spiral[row][col] == 0:
            spiral[row][col] = 1
            done = False
            break

        if row + 2 <= len(spiral) - 1 and \
                spiral[row + 2][col] == spiral[row + 1][col] == 0:
            spiral[row][col] = 1
            coordinates['row'] += 1
            done = False
        elif row + 1 == len(spiral) - 1 and \
                spiral[row + 1][col] == 0:
            spiral[row][col] = 1
            coordinates['row'] += 1
            done = False
        else:
            break

    return done


def left(spiral: list, coordinates: dict) -> bool:
    """
    Move spiral left.

    :param coordinates: starting point
    :param spiral: NxN spiral 2D array
    :return: bool
    """
    done: bool = True

    while coordinates['col'] >= 0:

        row = coordinates['row']
        col = coordinates['col']

        if col == spiral[row][col] == 0:
            spiral[row][col] = 1
            done = False
            break

        if col - 2 >= 0 and \
                spiral[row][col - 2] == 1 and \
                spiral[row][col - 1] == 0 and \
                spiral[row - 1][col] != 1:
            spiral[row][col] = 1
            done = False
            break

        if col - 2 >= 0 and \
                spiral[row][col - 2] == spiral[row][col - 1] == 0:
            spiral[row][col] = 1
            coordinates['col'] -= 1
            done = False
        elif col - 1 == spiral[row][col - 1] == spiral[row][col] == 0:
            spiral[row][col] = 1
            coordinates['col'] -= 1
            done = False
        else:
            break

    return done


def up(spiral: list, coordinates: dict) -> bool:
    """
    Move spiral up.

    :param coordinates: starting point
    :param spiral: NxN spiral 2D array
    :return: boole
    """
    done: bool = True

    while coordinates['row'] >= 0:

        row = coordinates['row']
        col = coordinates['col']

        if row - 2 >= 0 and spiral[row - 2][col] == spiral[row - 1][col] == 0:
            spiral[row][col] = 1
            coordinates['row'] -= 1
            done = False
        else:
            break

    return done


def set_initial_params(size: int) -> tuple:
    """
    Setting initial params.

    Initial parameters: line, spiral, direction, coordinate, done.
    :param size:
    :return: tuple
    """
    spiral: list = []
    while len(spiral) != size:
        line: list = [0] * size
        spiral.append(line)

    direction: str = 'right'
    coordinate: dict = {
        'row': 0,
        'col': 0
    }
    done: bool = False

    return spiral, direction, coordinate, done


def spiralize(size: int) -> list:
    """
    Creates a NxN spiral 2D list with a given size.

    :param size: size of the 2D array
    :return: list, NxN spiral 2D array
    """
    spiral, direction, coordinates, done = set_initial_params(size)

    while not done:
        # 1 Moving spiral:
        if direction == 'right':
            done = right(spiral, coordinates)
        elif direction == 'down':
            done = down(spiral, coordinates)
        elif direction == 'left':
            done = left(spiral, coordinates)
        elif direction == 'up':
            done = up(spiral, coordinates)
        # 2 Update direction:
        direction = DIRECTIONS[direction]

    return spiral
