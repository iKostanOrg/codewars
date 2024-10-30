"""
Test for -> Sudoku Solution Validator
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""
# ALGORITHMS DATA STRUCTURES VALIDATION

import unittest
import allure
from utils.log_func import print_log
from kyu_4.sudoku_solution_validator.valid_solution \
    import valid_solution


@allure.epic('4 kyu')
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Validation")
@allure.story('Sudoku Solution Validator')
@allure.tag('ALGORITHMS',
            'DATA STRUCTURES',
            'VALIDATION')
@allure.link(url='https://www.codewars.com/kata/529bf0e9bdf7657179000008',
             name='Source/Kata')
class ValidSolutionTestCase(unittest.TestCase):
    """
    Testing validSolution function
    """

    def test_valid_solution(self):
        """
        Test a function validSolution/ValidateSolution/valid_solution()
        that accepts a 2D array representing a Sudoku board, and returns
        true if it is a valid solution, or false otherwise. The cells of
        the sudoku board may also contain 0's, which will represent empty
        cells. Boards containing one or more zeroes are considered to be
        invalid solutions.

        The board is always 9 cells by 9 cells, and every
        cell only contains integers from 0 to 9.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing validSolution")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Test a function valid_solution()"
            " that accepts a 2D array representing a Sudoku"
            " board, and returns true if it is a valid "
            "solution, or false otherwise. The cells of the"
            " sudoku board may also contain 0's, which will"
            " represent empty cells. Boards containing one"
            " or more zeroes are considered to be invalid"
            " solutions.</p>"
            "<p>The board is always 9 cells by 9 cells,"
            " and every cell only contains integers from"
            " 0 to 9.</p>")
        # pylint: enable-msg=R0801
        test_data: tuple = (
            ([[5, 3, 4, 6, 7, 8, 9, 1, 2],
              [6, 7, 2, 1, 9, 5, 3, 4, 8],
              [1, 9, 8, 3, 4, 2, 5, 6, 7],
              [8, 5, 9, 7, 6, 1, 4, 2, 3],
              [4, 2, 6, 8, 5, 3, 7, 9, 1],
              [7, 1, 3, 9, 2, 4, 8, 5, 6],
              [9, 6, 1, 5, 3, 7, 2, 8, 4],
              [2, 8, 7, 4, 1, 9, 6, 3, 5],
              [3, 4, 5, 2, 8, 6, 1, 7, 9]], True),

            ([[5, 3, 4, 6, 7, 8, 9, 1, 2],
              [6, 7, 2, 1, 9, 0, 3, 4, 9],
              [1, 0, 0, 3, 4, 2, 5, 6, 0],
              [8, 5, 9, 7, 6, 1, 0, 2, 0],
              [4, 2, 6, 8, 5, 3, 7, 9, 1],
              [7, 1, 3, 9, 2, 4, 8, 5, 6],
              [9, 0, 1, 5, 3, 7, 2, 1, 4],
              [2, 8, 7, 4, 1, 9, 6, 3, 5],
              [3, 0, 0, 4, 8, 1, 1, 7, 9]], False),

            ([[1, 2, 3, 4, 5, 6, 7, 8, 9],
              [2, 3, 4, 5, 6, 7, 8, 9, 1],
              [3, 4, 5, 6, 7, 8, 9, 1, 2],
              [4, 5, 6, 7, 8, 9, 1, 2, 3],
              [5, 6, 7, 8, 9, 1, 2, 3, 4],
              [6, 7, 8, 9, 1, 2, 3, 4, 5],
              [7, 8, 9, 1, 2, 3, 4, 5, 6],
              [8, 9, 1, 2, 3, 4, 5, 6, 7],
              [9, 1, 2, 3, 4, 5, 6, 7, 8]], False))

        for data in test_data:
            board = data[0]
            expected = data[1]
            actual_result = valid_solution(board)
            print_log(board=board,
                      expected=expected,
                      actual_result=actual_result)

            with allure.step(f"Enter test list ({board}) and "
                             f"verify the output ({actual_result}) vs "
                             f"expected ({expected})"):
                self.assertEqual(expected, actual_result)
