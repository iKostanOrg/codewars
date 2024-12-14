"""
Test for -> Not very secure.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# BUGS REGULAR EXPRESSIONS DECLARATIVE PROGRAMMING
# ADVANCED LANGUAGE FEATURES FUNDAMENTALS STRINGS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_5.not_very_secure.alphanumeric import alphanumeric


# pylint: disable-msg=R0801
@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Advanced Language Features")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Not very secure')
@allure.tag('BUGS',
            'REGULAR EXPRESSIONS',
            'DECLARATIVE PROGRAMMING',
            'ADVANCED LANGUAGE FEATURES',
            'FUNDAMENTALS',
            'STRINGS')
@allure.link(
    url='https://www.codewars.com/kata/526dbd6c8c0eb53254000110',
    name='Source/Kata')
# pylint: enable-msg=R0801
class AlphanumericTestCase(unittest.TestCase):
    """Testing alphanumeric function."""

    @parameterized.expand([
        ("hello _world", False),
        ("PassW0rd", True),
        ("     ", False)])
    def test_alphanumeric(self, password, expected):
        """
        Testing alphanumeric function with various test inputs.

        The string has the following conditions
        to be alphanumeric only:

        1. At least one character ("" is not valid).
        2. Allowed characters are uppercase or lowercase
           latin letters and digits from 0 to 9.
        3. No whitespaces or underscore or special chars.

        :return: None
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing alphanumeric function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Enter test string and verify the output"):
            print_log(password=password, expected=expected)
            self.assertEqual(expected, alphanumeric(password))
