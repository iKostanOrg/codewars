"""
Test for Casino chips.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS MATHEMATICS ALGORITHMS NUMBERS

import unittest
import allure
from parameterized import parameterized
from kyu_6.casino_chips.solve import solve
from utils.log_func import print_log


# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Math")
@allure.story('Casino chips')
@allure.tag('FUNDAMENTALS',
            'MATHEMATICS',
            'ALGORITHMS',
            'NUMBERS')
@allure.link(
    url='https://www.codewars.com/kata/5e0b72d2d772160011133654',
    name='Source/Kata')
# pylint: enable-msg=R0801
class SolveTestCase(unittest.TestCase):
    """Testing solve function."""

    @parameterized.expand([
        ([8, 8, 8], 12),
        ([1, 1, 1], 1),
        ([8, 1, 4], 5),
        ([7, 4, 10], 10),
        ([12, 12, 12], 18),
        ([6, 6, 6], 9),
        ([1, 23, 2], 3),
        ([9, 8, 6], 11),
        ([10, 9, 6], 12),
        ([4, 4, 3], 5),
        ([1, 2, 1], 2),
        ([4, 1, 1], 2),
        ([8, 2, 8], 9)])
    def test_solve(self, arr, expected):
        """
        Testing 'solve' function with various test data.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing solve function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>You will be given an array representing the number "
            "of chips of each color and your task is to return the "
            "maximum number of days you can pick the chips. Each "
            "day you need to take exactly two chips.</p>")
        # pylint: enable-msg=R0801
        actual_result = solve(arr)
        with allure.step(f"Enter an array ({arr}) and verify the "
                         f"expected output ({expected}) vs "
                         f"actual result ({actual_result})"):
            print_log(arr=arr, expected=expected, result=actual_result)
            self.assertEqual(expected, actual_result)
