"""
Walker class: make moves, check directions, etc...

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


class Walker:
    """
    Walker class: make moves, check directions, etc...
    """

    def __init__(self, grid: list):
        # print('__init__')
        self.__grid: list = grid
        self.__is_start: bool = True
        self.__position: dict = self.__get_start_point()
        self.__direction = self.__set_initial_direction()

    def __set_initial_direction(self) -> dict:
        DIRECTION = {
            'left': False,
            'right': False,
            'up': False,
            'down': False,
        }

        # coordinates
        row: int = self.__position['row']
        col: int = self.__position['col']

        # up
        if row - 1 >= 0:
            if self.__grid[row - 1][col] in 'X|+':
                DIRECTION['up'] = True

        # down
        if row + 1 < len(self.__grid):
            if self.__grid[row + 1][col] in 'X|+':
                DIRECTION['down'] = True

        # left
        if col - 1 >= 0:
            if self.__grid[row][col - 1] in 'X+-':
                DIRECTION['left'] = True

        # right
        if col + 1 < len(self.__grid[row]):
            if self.__grid[row][col + 1] in 'X+-':
                DIRECTION['right'] = True

        print("\nINITIAL DIRECTION: {}".format(DIRECTION))
        return DIRECTION

    @property
    def position(self) -> str:
        """
        Return char from grid based on current position

        :return: str, current char
        """
        row: int = self.__position['row']
        col: int = self.__position['col']
        return self.__grid[row][col]

    def move(self) -> None:
        """
        Make one step if possible

        :return: None
        """
        if not self.is_done:
            # 1. update coordinates
            if self.__direction['left']:
                self.__position['prev_col'] = self.__position['col']
                self.__position['prev_row'] = self.__position['row']
                self.__position['col'] -= 1
            elif self.__direction['right']:
                self.__position['prev_col'] = self.__position['col']
                self.__position['prev_row'] = self.__position['row']
                self.__position['col'] += 1
            elif self.__direction['up']:
                self.__position['prev_col'] = self.__position['col']
                self.__position['prev_row'] = self.__position['row']
                self.__position['row'] -= 1
            elif self.__direction['down']:
                self.__position['prev_col'] = self.__position['col']
                self.__position['prev_row'] = self.__position['row']
                self.__position['row'] += 1
            # 2. update flag
            if self.__is_start:
                self.__is_start = False
            # 3. set direction
            # DEBUG ONLY
            row: int = self.__position['row']
            col: int = self.__position['col']
            print('\nchar: {}, '
                  'direction: {}, '
                  'row: {}, '
                  'col: {}, '
                  'is_done: {}\n'.format(self.__grid[row][col],
                                         [key for key in self.__direction if self.__direction[key]],
                                         row,
                                         col,
                                         self.is_done))
            self.__set_direction()

    @property
    def is_done(self) -> bool:
        """
        Check if get to the 'X' point
        or can make one move only

        :return: true/false
        """
        if self.__is_start:
            if len([val for val in self.__direction.values() if val]) != 1:
                print('\nRule #1')
                return True
        else:
            if self.position == 'X' and not self.__is_start:
                print('\nRule #2')
                return True

            if len([val for val in self.__direction.values() if val]) != 1:
                print('\nRule #3')
                print(self.__direction)
                return True

        return False

    def __get_start_point(self) -> dict:
        """
        Locate starting point

        :return: dict, starting point X
        """
        result: dict = dict()
        done: bool = False

        for row_i, row in enumerate(self.__grid):
            for col_i, col in enumerate(row):
                if col == 'X':
                    result = {'prev_row': row_i,
                              'prev_col': col_i,
                              'row': row_i,
                              'col': col_i}
                    done = True
                    break
            if done:
                break

        return result

    def __reset_direction(self) -> None:
        for key in self.__direction:
            self.__direction[key] = False

    def __set_direction(self) -> None:
        """
        Update directions based on current
        position and previous direction

        :return: None
        """
        prev_row = self.__position['prev_row']
        prev_col = self.__position['prev_col']
        previous_position = self.__grid[prev_row][prev_col]

        # reset all directions
        self.__reset_direction()
        print('prev: {}, pos: {}'.format(previous_position, self.position))

        if self.position == '+' and (previous_position == '-' or previous_position == 'X'):
            self.__direction['up'] = self.__test_up()
            self.__direction['down'] = self.__test_down()
        elif self.position == '+' and previous_position == '|':
            self.__direction['left'] = self.__test_left()
            self.__direction['right'] = self.__test_right()
        elif self.position == '+' and previous_position == '+':
            if self.__position['col'] == self.__position['prev_col']:
                self.__direction['left'] = self.__test_left()
                self.__direction['right'] = self.__test_right()
            elif self.__position['row'] == self.__position['prev_row']:
                self.__direction['up'] = self.__test_up()
                self.__direction['down'] = self.__test_down()
        elif self.position == '-' and (previous_position == '-' or previous_position == 'X'):
            if self.__position['col'] < self.__position['prev_col']:
                self.__direction['left'] = self.__test_left()
            elif self.__position['col'] > self.__position['prev_col']:
                self.__direction['right'] = self.__test_right()
        elif self.position == '-' and previous_position == '+':
            if self.__position['col'] < self.__position['prev_col']:
                self.__direction['left'] = self.__test_left()
            elif self.__position['col'] > self.__position['prev_col']:
                self.__direction['right'] = self.__test_right()
        elif self.position == '|' and (previous_position == '|' or previous_position == 'X'):
            if self.__position['row'] < self.__position['prev_row']:
                self.__direction['up'] = self.__test_up()
            elif self.__position['row'] > self.__position['prev_row']:
                self.__direction['down'] = self.__test_down()
        elif self.position == '|' and previous_position == '+':
            if self.__position['row'] < self.__position['prev_row']:
                self.__direction['up'] = self.__test_up()
            elif self.__position['row'] > self.__position['prev_row']:
                self.__direction['down'] = self.__test_down()

    def __test_up(self) -> bool:
        row: int = self.__position['row']
        col: int = self.__position['col']
        if row - 1 >= 0 and self.__grid[row - 1][col] in 'X|+':
            return True
        return False

    def __test_down(self) -> bool:
        row: int = self.__position['row']
        col: int = self.__position['col']
        if row + 1 < len(self.__grid) and self.__grid[row + 1][col] in 'X|+':
            return True
        return False

    def __test_left(self) -> bool:
        row: int = self.__position['row']
        col: int = self.__position['col']
        if col - 1 >= 0 and self.__grid[row][col - 1] in 'X+-':
            return True
        return False

    def __test_right(self) -> bool:
        row: int = self.__position['row']
        col: int = self.__position['col']
        if col + 1 < len(self.__grid[row]) and self.__grid[row][col + 1] in 'X+-':
            return True
        return False

    def __count_possible_directions(self) -> int:
        return len([val for val in [self.__test_left(),
                                    self.__test_right(),
                                    self.__test_up(),
                                    self.__test_down()] if val])
