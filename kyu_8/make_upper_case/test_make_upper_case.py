"""
Test for -> MakeUpperCase
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.make_upper_case.make_upper_case import make_upper_case


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('MakeUpperCase')
@allure.tag('FUNDAMENTALS')
@allure.link(
    url='https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7',
    name='Source/Kata')
# pylint: enable=R0801
class MakeUpperCaseTestCase(unittest.TestCase):
    """
    Testing make_upper_case function
    """

    def test_make_upper_case(self):
        """
        Sample Tests for make_upper_case function
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing make_upper_case function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable=R0801
        with allure.step("Pass lower case string and verify the output"):
            string: str = "hello"
            expected: str = "HELLO"
            print_log(string=string, expected=expected)
            self.assertEqual(make_upper_case(string), expected)
