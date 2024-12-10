"""
Test for -> Moving Zeros To The End.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS INTERVIEW QUESTIONS ARRAYS SORTING

import unittest
import allure
from utils.log_func import print_log
from kyu_5.moving_zeros_to_the_end.move_zeros import move_zeros


# pylint: disable-msg=R0801
@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Moving Zeros To The End')
@allure.tag('ALGORITHMS',
            'INTERVIEW QUESTIONS',
            'ARRAYS',
            'SORTING')
@allure.link(
    url='https://www.codewars.com/kata/52597aa56021e91c93000cb0',
    name='Source/Kata')
# pylint: enable-msg=R0801
class MoveZerosTestCase(unittest.TestCase):
    """Testing move_zeros function."""

    def test_move_zeros(self):
        """
        Testing move_zeros function with various test data.

        Test an algorithm that takes an array and moves all of the
        zeros to the end, preserving the order of the other elements.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing move_zeros function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Enter test data (list) and verify the output"):
            test_data: tuple = (
                ([1, 2, 0, 1, 0, 1, 0, 3, 0, 1], [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]),
                ([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9],
                 [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                (["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9],
                 ["a", "b", "c", "d", 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                (["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0,
                  1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9],
                 ["a", "b", None, "c", "d", 1, False, 1, 3, [], 1,
                  9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                ([0, 1, None, 2, False, 1, 0], [1, None, 2, False, 1, 0, 0]),
                (["a", "b"], ["a", "b"]),
                (["a"], ["a"]),
                ([0, 0], [0, 0]),
                ([0], [0]),
                ([False], [False]),
                ([], []))

            for d in test_data:
                array: list = d[0]
                expected: list = d[1]
                print_log(array=array, expected=expected)
                self.assertEqual(expected, move_zeros(array))
