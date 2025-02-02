"""
Test for -> Pyramid Array.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS

import unittest
import allure
from utils.log_func import print_log
from kyu_6.pyramid_array.pyramid_array import pyramid


# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Pyramid Array')
@allure.tag('ALGORITHMS')
@allure.link(
    url='https://www.codewars.com/kata/515f51d438015969f7000013',
    name='Source/Kata')
# pylint: enable-msg=R0801
class PyramidTestCase(unittest.TestCase):
    """Testing 'pyramid' function."""

    def test_pyramid(self):
        """
        Testing 'pyramid' function with various test data.

        The 'pyramid' function should return
        an Array of ascending length sub-arrays.

        Note: the sub-arrays should be filled with 1s.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing the 'pyramid' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Pass zero:"):
            n: int = 0
            expected: list = []
            print_log(n=n, expected=expected)
            self.assertEqual(pyramid(n), expected)

        with allure.step("Pass one:"):
            n = 1
            expected = [[1]]
            print_log(n=n, expected=expected)
            self.assertEqual(pyramid(n), expected)

        with allure.step("Pass two:"):
            n = 2
            expected = [[1], [1, 1]]
            print_log(n=n, expected=expected)
            self.assertEqual(pyramid(n), expected)

        with allure.step("Pass three:"):
            n = 3
            expected = [[1], [1, 1], [1, 1, 1]]
            print_log(n=n, expected=expected)
            self.assertEqual(pyramid(n), expected)
