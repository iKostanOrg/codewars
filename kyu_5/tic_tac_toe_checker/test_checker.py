"""
Testing is_solved function
"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS ARRAYS

import allure
import unittest
from utils.log_func import print_log
from kyu_5.tic_tac_toe_checker.checker import is_solved


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite('Algorithms')
@allure.sub_suite("Unit Tests")
@allure.feature('Lists')
@allure.story('Tic-Tac-Toe Checker')
@allure.tag('ALGORITHMS', 'ARRAY')
@allure.link(url='https://www.codewars.com/kata/525caa5c1bf619d28c000335/train/python',
             name='Source/Kata')
class IsSolvedTestCase(unittest.TestCase):
    """
    Testing is_solved function
    """

    def test_is_solved(self):
        """
        Testing is_solved function

        The function should return whether the
        board's current state is solved.

        We want our function to return:

            -1 if the board is not yet finished (there are empty spots),
            1 if "X" won,
            2 if "O" won,
            0 if it's a cat's game (i.e. a draw).
        """

        allure.dynamic.title("Testing done_or_not function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>The function should return whether the board's "
                                        "current state is solved.</p>")

        test_data = (
            ([[0, 0, 1],
              [0, 1, 2],
              [2, 1, 0]], -1, 'not yet finished'),
            ([[1, 1, 1],
              [0, 2, 2],
              [0, 0, 0]], 1, 'winning row'),
            ([[2, 1, 2],
              [2, 1, 1],
              [1, 1, 2]], 1, 'winning column'),
            ([[2, 1, 2],
              [2, 1, 1],
              [1, 2, 1]], 0, 'draw'),
        )

        for board, expected, message in test_data:
            result = is_solved(board)
            with allure.step("Enter Tic-Tac-Toe board and verify the output."):
                print_log(expected=expected, result=result, message=message)
                self.assertEqual(expected, result, msg=message)
