#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# PUZZLES ARRAYS GAMES ALGORITHMS VALIDATION

import allure
import unittest
from utils.log_func import print_log
from kyu_4.validate_sudoku_with_size.sudoku import Sudoku


@allure.epic('4 kyu')
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Control Flow")
@allure.story('Validate Sudoku with size `NxN`')
@allure.tag('PUZZLES', 'ARRAYS', 'GAMES', 'ALGORITHMS', 'VALIDATION')
@allure.link(url='https://www.codewars.com/kata/540afbe2dc9f615d5e000425/train/python',
             name='Source/Kata')
class SudokuTestCase(unittest.TestCase):
    """
    Testing Sudoku class
    """

    def test_sudoku_class(self):
        """
        Testing Sudoku class

        Given a Sudoku data structure with size NxN, N > 0 and √N == integer,
        assert a method that validates if it has been filled out correctly.
        :return:
        """

        allure.dynamic.title("Testing Sudoku class")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>Testing Sudoku class</p>"
                                        "<p>Given a Sudoku data structure with size NxN, "
                                        "N > 0 and √N == integer, assert a method that validates "
                                        "if it has been filled out correctly.</p>")

        test_data = [
            ([
                 [7, 8, 4, 1, 5, 9, 3, 2, 6],
                 [5, 3, 9, 6, 7, 2, 8, 4, 1],
                 [6, 1, 2, 4, 3, 8, 7, 5, 9],

                 [9, 2, 8, 7, 1, 5, 4, 6, 3],
                 [3, 5, 7, 8, 4, 6, 1, 9, 2],
                 [4, 6, 1, 9, 2, 3, 5, 8, 7],

                 [8, 7, 6, 3, 9, 4, 2, 1, 5],
                 [2, 4, 3, 5, 6, 1, 9, 7, 8],
                 [1, 9, 5, 2, 8, 7, 6, 3, 4]
             ], True, 'Testing valid 9x9'),

            ([
                 [1, 4, 2, 3],
                 [3, 2, 4, 1],

                 [4, 1, 3, 2],
                 [2, 3, 1, 4]
             ], True, 'Testing valid 4x4'),

            ([
                 [0, 2, 3, 4, 5, 6, 7, 8, 9],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9],

                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9],

                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9]
             ], False, 'Values in wrong order'),

            ([
                 [1, 2, 3, 4, 5],
                 [1, 2, 3, 4],
                 [1, 2, 3, 4],
                 [1]
             ],
             False, '4x5 (invalid dimension)'),

            ([[7, 8, 4, 1, 5, 9, 3, 2, 6],
              [5, 3, 9, 6, 7, 2, 8, 4, 1],
              [6, 1, 2, 4, 3, 8, 7, 5, 9],
              [9, 2, 8, 7, 1, 5, 4, 6, 3],
              [3, 5, 7, 8, 4, 6, 1, 9, 2],
              [4, 6, 1, 9, 2, 3, 5, 8, 7],
              [8, 7, 6, 3, 9, 4, 2, 1, 5],
              [2, 4, 3, 5, 6, 1, 9, 7, 8],
              [1, 9, 5, 2, 8, 7, 6, 3, 4]],
             True, 'Testing valid 9x9'),

            ([[1, 4, 2, 3],
              [3, 2, 4, 1],
              [4, 1, 3, 2],
              [2, 3, 1, 4]],
             True, 'Testing valid 4x4'),

            ([[1]],
             True, 'Testing valid 1x1'),

            ([[0, 2, 3, 4, 5, 6, 7, 8, 9],
              [1, 2, 3, 4, 5, 6, 7, 8, 9],
              [1, 2, 3, 4, 5, 6, 7, 8, 9],
              [1, 2, 3, 4, 5, 6, 7, 8, 9],
              [1, 2, 3, 4, 5, 6, 7, 8, 9],
              [1, 2, 3, 4, 5, 6, 7, 8, 9],
              [1, 2, 3, 4, 5, 6, 7, 8, 9],
              [1, 2, 3, 4, 5, 6, 7, 8, 9],
              [1, 2, 3, 4, 5, 6, 7, 8, 9]],
             False, 'Values in wrong order'),

            ([[1, 2, 3, 4, 5],
              [1, 2, 3, 4],
              [1, 2, 3, 4],
              [1]], False, '4x5 (invalid dimension)'),

            ([[2], ], False, '1x1 with wrong value'),

            ([[''], ],
             False, 'Empty field(s)'),

            ([[0], ],
             False, 'Values not in valid range 1..N'),

            ([[True], ],
             False, 'Invalid value types (boolean)'),

            ([[1, 4, 4, 3, 'a'],
              [3, 2, 4, 1],
              [4, 1, 3, 3],
              [2, 0, 1, 4],
              ['', False, None, '4']],
             False, 'Sudoku breaking all rules at once'),

            ([[1, 2, 3, 4, 5, 6, 7, 8, 9],
              [2, 3, 1, 5, 6, 4, 8, 9, 7],
              [3, 1, 2, 6, 4, 5, 9, 7, 8],
              [4, 5, 6, 7, 8, 9, 1, 2, 3],
              [5, 6, 4, 8, 9, 7, 2, 3, 1],
              [6, 4, 5, 9, 7, 8, 3, 1, 2],
              [7, 8, 9, 1, 2, 3, 4, 5, 6],
              [8, 9, 7, 2, 3, 1, 5, 6, 4],
              [9, 7, 8, 3, 1, 2, 6, 4, 5]],
             False, 'Sudoku with invalid boxes (little squares), but valid rows and columns'),

        ]

        for data, expected, message in test_data:
            with allure.step("Enter a Sudoku solution and verify if it a valid one."):

                print('\n Sudoku:')
                # for row in data:
                    # print(row)

                actual_result = Sudoku(data).is_valid()

                print_log(expected=expected,
                          actual_result=actual_result,
                          message=message)

            with allure.step("Assert expected result vs actual."):
                self.assertEqual(expected, actual_result)
