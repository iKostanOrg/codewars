"""
Test for -> Substituting Variables Into Strings: Padded Numbers.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS STRINGS STRING FORMATTING FORMATTING ALGORITHMS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_7.substituting_variables_into_strings_padded_numbers.solution import solution


# pylint: disable-msg=R0801
@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Substituting Variables Into Strings: Padded Numbers')
@allure.tag('FUNDAMENTALS',
            'STRINGS',
            'STRING FORMATTING',
            'FORMATTING',
            'ALGORITHMS')
@allure.link(
    url='https://www.codewars.com/kata/54ba84be607a92aa900000f1',
    name='Source/Kata')
# pylint: enable-msg=R0801
class SolutionTestCase(unittest.TestCase):
    """Testing 'solution' function."""

    @parameterized.expand([
        (0, 'Value is 00000'),
        (5, 'Value is 00005'),
        (109, 'Value is 00109'),
        (1204, 'Value is 01204')])
    def test_solution(self, value, expected):
        """
        Testing 'solution' function with various test data.

        The function should return a formatted string.
        The return value should equal "Value is VALUE"
        where value is a 5 digit padded number.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'solution' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step(f"Enter a number: {value} "
                         f"and verify the expected result: {expected}."):
            print_log(expected=expected, value=value)
            self.assertEqual(expected, solution(value))
