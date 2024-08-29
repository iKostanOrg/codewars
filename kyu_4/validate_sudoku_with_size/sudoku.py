"""
Solution for -> Validate Sudoku with size `NxN`

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


from kyu_5.did_i_finish_my_sudoku.sudoku_by_row import assert_sudoku_by_row
from kyu_5.did_i_finish_my_sudoku.sudoku_by_column import assert_sudoku_by_column
from kyu_5.did_i_finish_my_sudoku.sudoku_by_regions import assert_sudoku_by_region


class Sudoku:

    def __init__(self, data: list):
        self.__data: list = data

    def is_valid(self) -> bool:
        """
        A method to validate if given a Sudoku has been filled out correctly.
        Sudoku -> data structure with size NxN, N > 0 and √N == integer.
        :return: bool
        """
        if not self.__is_data_valid() \
                or not assert_sudoku_by_row(self.__data) \
                or not assert_sudoku_by_column(self.__data):
            return False

        print('# 4')
        if len(self.__data) > 1:
            if not assert_sudoku_by_region(self.__data):
                return False

        return True

    def __is_data_valid(self) -> bool:
        if not self.__data:
            return False

        if len(self.__data) == 1:
            # print('if self.__data[0][0]: {}'.format(self.__data[0][0]))
            if self.__data[0][0] != 1 or isinstance(self.__data[0][0], bool):
                return False

        return isinstance(self.__data, list)
