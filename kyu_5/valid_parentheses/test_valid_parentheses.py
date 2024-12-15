"""
Test for -> Valid Parentheses.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS VALIDATION UTILITIES

import unittest
import allure
from parameterized import parameterized
from kyu_5.valid_parentheses.valid_parentheses \
    import valid_parentheses
from utils.log_func import print_log


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Validation")
@allure.story('Valid Parentheses')
@allure.tag('ALGORITHMS',
            'VALIDATION',
            'UTILITIES')
@allure.link(
    url='https://www.codewars.com/kata/52774a314c2333f0a7000688',
    name='Source/Kata')
class ValidParenthesesTestCase(unittest.TestCase):
    """Testing valid_parentheses function."""

    @parameterized.expand([
        ("  (", False),
        (")test", False),
        ("", True),
        ("hi())(", False),
        ("hi(hi)()", True),
        ("()", True),
        (")(()))", False),
        ("(", False),
        ("(())((()())())", True)])
    def test_valid_parentheses(self, test_input, expected):
        """
        Testing valid_parentheses with various test data.

        Test the valid_parentheses function that takes a string
        of parentheses, and determines if the order of the
        parentheses is valid. The function should return true
        if the string is valid, and false if it's invalid.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing valid_parentheses function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step(f"Enter test string: {test_input}"
                         f"and verify the expected output: {expected}."):
            print_log(test_input=test_input, expected=expected)
            self.assertEqual(expected, valid_parentheses(test_input))
