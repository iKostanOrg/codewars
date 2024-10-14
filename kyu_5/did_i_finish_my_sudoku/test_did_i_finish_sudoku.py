"""
Test for -> Did I Finish my Sudoku?
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# PUZZLES LISTS DATA STRUCTURES LOOPS CONTROL FLOW
# BASIC LANGUAGE FEATURES FUNDAMENTALS MATHEMATICS ALGORITHMS

import unittest
import allure
from utils.log_func import print_log
from kyu_5.did_i_finish_my_sudoku.is_sudoku_done import done_or_not


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite('Algorithms')
@allure.sub_suite("Unit Tests")
@allure.feature('Control Flow')
@allure.story('Did I Finish my Sudoku?')
@allure.tag('PUZZLES',
            'LISTS',
            'DATA STRUCTURES',
            'LOOPS',
            'CONTROL FLOW',
            'BASIC LANGUAGE FEATURES',
            'FUNDAMENTALS',
            'MATHEMATICS',
            'ALGORITHMS')
@allure.link(url='https://www.codewars.com/kata/53db96041f1a7d32dc0004d2/train/python',
             name='Source/Kata')
class DidIFinishedSudokuTestCase(unittest.TestCase):
    """
    Testing done_or_not function
    """

    def test_done_or_not(self):
        """
        Testing done_or_not function

        Testing a function done_or_not/DoneOrNot passing a board
        (list[list_lines]) as parameter. If the board is valid return
        'Finished!', otherwise return 'Try again!'
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing done_or_not function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing a function done_or_not/DoneOrNot passing a "
            "board (list[list_lines]) as parameter. If the board is "
            "valid return 'Finished!', otherwise return 'Try again!'</p>")
        test_data: tuple = (
            ([[1, 3, 2, 5, 7, 9, 4, 6, 8],
              [4, 9, 8, 2, 6, 1, 3, 7, 5],
              [7, 5, 6, 3, 8, 4, 2, 1, 9],
              [6, 4, 3, 1, 5, 8, 7, 9, 2],
              [5, 2, 1, 7, 9, 3, 8, 4, 6],
              [9, 8, 7, 4, 2, 6, 5, 3, 1],
              [2, 1, 4, 9, 3, 5, 6, 8, 7],
              [3, 6, 5, 8, 1, 7, 9, 2, 4],
              [8, 7, 9, 6, 4, 2, 1, 5, 3]],
             'Finished!'),
            ([[1, 3, 2, 5, 7, 9, 4, 6, 8],
              [4, 9, 8, 2, 6, 1, 3, 7, 5],
              [7, 5, 6, 3, 8, 4, 2, 1, 9],
              [6, 4, 3, 1, 5, 8, 7, 9, 2],
              [5, 2, 1, 7, 9, 3, 8, 4, 6],
              [9, 8, 7, 4, 2, 6, 5, 3, 1],
              [2, 1, 4, 9, 3, 5, 6, 8, 7],
              [3, 6, 5, 8, 1, 7, 9, 2, 4],
              [8, 7, 9, 6, 4, 2, 1, 3, 5]],
             'Try again!'),
            ([[1, 2, 3, 4, 5, 6, 7, 8, 9],
              [2, 3, 4, 5, 6, 7, 8, 9, 1],
              [3, 4, 5, 6, 7, 8, 9, 1, 2],
              [4, 5, 6, 7, 8, 9, 1, 2, 3],
              [5, 6, 7, 8, 9, 1, 2, 3, 4],
              [6, 7, 8, 9, 1, 2, 3, 4, 5],
              [7, 8, 9, 1, 2, 3, 4, 5, 6],
              [8, 9, 1, 2, 3, 4, 5, 6, 7],
              [9, 1, 2, 3, 4, 5, 6, 7, 8]],
             'Try again!'))
        # pylint: enable-msg=R0801
        for board, expected in test_data:
            result = done_or_not(board)

            with allure.step("Enter sudoku and verify the output."):
                print_log(expected=expected, result=result)
                self.assertEqual(expected, result)
