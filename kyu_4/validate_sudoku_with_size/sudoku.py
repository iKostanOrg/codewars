"""
Solution for -> Validate Sudoku with size `NxN`

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


from kyu_5.did_i_finish_my_sudoku.sudoku_by_row import assert_sudoku_by_row
from kyu_5.did_i_finish_my_sudoku.sudoku_by_column import assert_sudoku_by_column
from kyu_5.did_i_finish_my_sudoku.sudoku_by_regions import assert_sudoku_by_region


class Sudoku:
    """
    Given a Sudoku data structure with size `NxN, N > 0
    and √N == integer`, write a method to validate if it
    has been filled out correctly.
    """

    def __init__(self, data: list):
        self.__data: list = data

    def is_valid(self) -> bool:
        """
        A method to validate if given a Sudoku has been filled out correctly.
        Sudoku -> data structure with size NxN, N > 0 and √N == integer.
        :return: bool
        """
        if not self.is_data_valid() \
                or not assert_sudoku_by_row(self.__data) \
                or not assert_sudoku_by_column(self.__data):
            return False

        if len(self.__data) > 1:
            if not assert_sudoku_by_region(self.__data):
                return False

        return True

    def is_data_valid(self) -> bool:
        """
        Verify data validity
        :return: bool
        """
        if not self.__data:
            return False

        if len(self.__data) == 1:
            if self.__data[0][0] != 1 or isinstance(self.__data[0][0], bool):
                return False

        return isinstance(self.__data, list)
