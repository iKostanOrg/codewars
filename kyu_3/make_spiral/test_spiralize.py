"""
Testing spiralizer function
Created by Egor Kostan.

GitHub: https://github.com/ikostan
"""

# ALGORITHMS ARRAYS CONTROL FLOW BASIC LANGUAGE FEATURES FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_3.make_spiral.solution import spiralize


# pylint: disable-msg=R0801
@allure.epic('3 kyu')
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Make a spiral')
@allure.tag('ALGORITHMS',
            'ARRAYS',
            'CONTROL FLOW',
            'BASIC LANGUAGE FEATURES',
            'FUNDAMENTALS')
@allure.link(
    url='https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/train/python',
    name='Source/Kata')
# pylint: enable-msg=R0801
class SpiralizeTestCase(unittest.TestCase):
    """
    Testing spiralize function
    """

    def test_spiralize(self):
        """
        Testing spiralize function
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing spiralize function")
        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>The function should create a NxN spiral with a given size.</p>")
        # pylint: enable-msg=R0801
        test_data: tuple = (
            (5, [[1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 1],
                 [1, 1, 1, 0, 1],
                 [1, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1]]),
            (6, [[1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 0, 1],
                 [1, 0, 0, 1, 0, 1],
                 [1, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1]]),
            (7, [[1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 0, 1],
                 [1, 0, 0, 0, 1, 0, 1],
                 [1, 0, 1, 1, 1, 0, 1],
                 [1, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1]]),
            (8, [[1, 1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 0, 1],
                 [1, 0, 0, 0, 0, 1, 0, 1],
                 [1, 0, 1, 0, 0, 1, 0, 1],
                 [1, 0, 1, 1, 1, 1, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1]]),
            (9, [[1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1, 0, 1],
                 [1, 0, 0, 0, 0, 0, 1, 0, 1],
                 [1, 0, 1, 1, 1, 0, 1, 0, 1],
                 [1, 0, 1, 0, 0, 0, 1, 0, 1],
                 [1, 0, 1, 1, 1, 1, 1, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1]])
        )

        for size, expected in test_data:
            with allure.step("Enter spiral list size and verify the result"):
                result: list = spiralize(size)
                print_log(size=size,
                          result=result,
                          expected=expected)
                self.assertListEqual(expected, result)
