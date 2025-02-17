"""
Test for -> Compare within margin.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS LOGIC

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_8.compare_within_margin.solution import close_compare


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Logic")
@allure.sub_suite("Unit Tests")
@allure.feature("Conditions")
@allure.story('Compare within margin')
@allure.tag('FUNDAMENTALS',
            'LOGIC')
@allure.link(
    url='https://www.codewars.com/kata/56453a12fcee9a6c4700009c',
    name='Source/Kata')
# pylint: enable=R0801
class CloseCompareTestCase(unittest.TestCase):
    """Test close_compare function."""

    @parameterized.expand([
        ((4, 5), -1, "No margin"),
        ((5, 5), 0, "No margin"),
        ((6, 5), 1, "No margin")])
    def test_close_compare_no_margin(self, test_data, expected, msg):
        """
        Test close_compare function with no margin.

        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing 'close_compare' function (no margin).")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="'
            'https://www.codewars.com/users/myFirstCode/badges/large'
            '">'
            '<h3>Test Description:</h3>'
            "<p>"
            "The function should return whether a is lower than, "
            "close to, or higher than b."
            "</p>"
            "<p>"
            "Please note the following:<br>"
            "- If margin is not given, treat it as if it were zero."
            "</p>")
        # pylint: enable=R0801
        with allure.step(f"Enter test data: {test_data} "
                         f"and verify the expected output: {expected}."):
            a, b = test_data
            result: int = close_compare(a, b)
            print_log(a=a, b=b, result=result, expected=expected, msg=msg)
            self.assertEqual(result, expected, msg=msg)

    @parameterized.expand([
        ((2, 5, 3), 0, "With margin of 3"),
        ((5, 5, 3), 0, "With margin of 3"),
        ((8, 5, 3), 0, "With margin of 3"),
        ((8.1, 5, 3), 1, "With margin of 3"),
        ((1.99, 5, 3), -1, "With margin of 3")])
    def test_close_compare_margin_3(self, test_data, expected, msg):
        """
        Test close_compare function with margin = 3.

        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing 'close_compare' function (margin is 3).")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="'
            'https://www.codewars.com/users/myFirstCode/badges/large'
            '">'
            '<h3>Test Description:</h3>'
            "<p>"
            "The function should return whether a is lower than, "
            "close to, or higher than b."
            "</p>"
            "<p>"
            "Please note the following:<br>"
            "- When a is close to b, return 0.<br>"
            "- When a is less than b, return -1.<br>"
            "- When a is greater than b, return 1."
            "</p>")
        # pylint: enable=R0801
        with allure.step(f"Enter test data: {test_data} "
                         f"and verify the expected output: {expected}."):
            a, b, margin = test_data
            result: int = close_compare(a, b, margin)
            print_log(a=a, b=b, result=result, expected=expected, msg=msg)
            self.assertEqual(result, expected, msg=msg)
