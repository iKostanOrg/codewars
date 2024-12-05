"""
Walker class: make moves, check directions, etc.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


class Walker:
    """Walker class: make moves, check directions, etc."""

    def __init__(self, grid: list):
        """
        Create a new Walker instance.

        :param grid:
        """
        self.__grid: list = grid
        self.__is_start: bool = True
        self.__position: dict = self.__get_start_point()
        self.__direction = self.__set_initial_direction()

    def __set_initial_direction(self) -> dict:
        """
        Set initial direction.

        :return: dict
        """
        direction: dict = {
            'left': False,
            'right': False,
            'up': False,
            'down': False}

        # coordinates
        row: int = self.__position['row']
        col: int = self.__position['col']

        # up
        if row >= 1 and self.__grid[row - 1][col] in 'X|+':
            direction['up'] = True

        # down
        if row + 1 < len(self.__grid) and self.__grid[row + 1][col] in 'X|+':
            direction['down'] = True

        # left
        if col >= 1 and self.__grid[row][col - 1] in 'X+-':
            direction['left'] = True

        # right
        if col + 1 < len(self.__grid[row]) and self.__grid[row][col + 1] in 'X+-':
            direction['right'] = True

        return direction

    @property
    def position(self) -> str:
        """
        Return char from grid based on current position.

        :return: str, current char
        """
        row: int = self.__position['row']
        col: int = self.__position['col']
        return self.__grid[row][col]

    def move(self) -> None:
        """
        Make one step if possible.

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
            self.__set_direction()

    @property
    def is_done(self) -> bool:
        """
        Check if get to the 'X' point or can make one move only.

        :return: bool
        """
        if self.__is_start:
            if len([val for val in self.__direction.values() if val]) != 1:
                return True
        else:
            if self.position == 'X' and not self.__is_start:
                return True

            if len([val for val in self.__direction.values() if val]) != 1:
                return True

        return False

    def __get_start_point(self) -> dict:
        """
        Locate starting point.

        :return: dict, starting point X
        """
        result: dict = {}
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

    def position_plus(self, previous_position: str) -> None:
        """
        Process cells if current position is +.

        :param previous_position: str
        :return: None
        """
        if self.position == '+' and previous_position in '-X':
            self.__direction['up'] = self.__test_up()
            self.__direction['down'] = self.__test_down()

        if self.position == '+' and previous_position == '|':
            self.__direction['left'] = self.__test_left()
            self.__direction['right'] = self.__test_right()

        if self.position == previous_position == '+' and \
                self.__position['col'] == self.__position['prev_col']:
            self.__direction['left, '] = self.__test_left()
            self.__direction['right'] = self.__test_right()

        if self.position == previous_position == '+' and \
                self.__position['row'] == self.__position['prev_row']:
            self.__direction['up'] = self.__test_up()
            self.__direction['down'] = self.__test_down()

    def position_minus(self, previous_position: str) -> None:
        """
        Process cells if current position is -.

        :param previous_position: str
        :return: None
        """
        if self.position == '-' and previous_position in '-X+':
            if self.__position['col'] < self.__position['prev_col']:
                self.__direction['left'] = self.__test_left()
            elif self.__position['col'] > self.__position['prev_col']:
                self.__direction['right'] = self.__test_right()

    def position_pipe(self, previous_position: str) -> None:
        """
        Process cells if current position is '|'.

        :param previous_position: str
        :return: None
        """
        if self.position == '|' and previous_position in '|X+':
            if self.__position['row'] < self.__position['prev_row']:
                self.__direction['up'] = self.__test_up()
            elif self.__position['row'] > self.__position['prev_row']:
                self.__direction['down'] = self.__test_down()

    def __set_direction(self) -> None:
        """
        Update directions based on current position and previous direction.

        :return: None
        """
        prev_row = self.__position['prev_row']
        prev_col = self.__position['prev_col']
        previous_position = self.__grid[prev_row][prev_col]

        # reset all directions
        self.__reset_direction()
        self.position_plus(previous_position)
        self.position_minus(previous_position)
        self.position_pipe(previous_position)

    def __test_up(self) -> bool:
        """
        Test up.

        :return:
        """
        row: int = self.__position['row']
        col: int = self.__position['col']
        return row >= 1 and self.__grid[row - 1][col] in 'X|+'

    def __test_down(self) -> bool:
        row: int = self.__position['row']
        col: int = self.__position['col']
        return row + 1 < len(self.__grid) and self.__grid[row + 1][col] in 'X|+'

    def __test_left(self) -> bool:
        row: int = self.__position['row']
        col: int = self.__position['col']
        return col >= 1 and self.__grid[row][col - 1] in 'X+-'

    def __test_right(self) -> bool:
        row: int = self.__position['row']
        col: int = self.__position['col']
        return col + 1 < len(self.__grid[row]) and self.__grid[row][col + 1] in 'X+-'
