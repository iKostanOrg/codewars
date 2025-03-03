"""
Tests for -> Will there be enough space?.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS NUMBERS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_8.will_there_be_enough_space.enough import enough


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Math")
@allure.sub_suite("Unit Tests")
@allure.feature("Calculation")
@allure.story('Will there be enough space?')
@allure.tag('FUNDAMENTALS',
            'NUMBERS')
@allure.link(
    url='https://www.codewars.com/kata/5875b200d520904a04000003',
    name='Source/Kata')
# pylint: enable=R0801
class EnoughTestCase(unittest.TestCase):
    """Testing enough function."""

    @parameterized.expand([
        ((10, 5, 5), 0),
        ((100, 60, 50), 10),
        ((20, 5, 5), 0)])
    def test_enough(self, test_dat, expected):
        """
        Testing enough function with various test data.

        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing enough function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>If there is enough space, return 0, "
            "and if there isn't, return the number "
            "of passengers he can't take.</p>")
        # pylint: enable=R0801
        with allure.step(f"Enter test data: {test_dat} "
                         f"and verify the expected output: {expected}."):
            cap: int = test_dat[0]
            on: int = test_dat[1]
            wait: int = test_dat[2]
            print_log(cap=cap,
                      on=on,
                      wait=wait,
                      expected=expected)
            self.assertEqual(expected, enough(cap, on, wait))
