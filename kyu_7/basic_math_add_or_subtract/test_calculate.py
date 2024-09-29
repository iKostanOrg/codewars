"""
Test for -> Basic Math (Add or Subtract)
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS STRINGS

import unittest
import allure
from kyu_7.basic_math_add_or_subtract.calculate import calculate
from utils.log_func import print_log


# pylint: disable-msg=R0801
@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite('Fundamentals')
@allure.sub_suite('Unit Tests')
@allure.feature('String')
@allure.story('Basic Math (Add or Subtract)')
@allure.tag('FUNDAMENTALS',
            'STRINGS')
@allure.link(
    url='https://www.codewars.com/kata/5809b62808ad92e31b000031',
    name='Source/Kata')
# pylint: enable-msg=R0801
class CalculateTestCase(unittest.TestCase):
    """
    Testing calculate function
    """

    def test_calculate(self):
        """
        Testing calculate function with various test data
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing calculate function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>In this kata, you will do addition and subtraction "
            "on a given string. The return value must be also a "
            "string.</p>")
        # pylint: enable-msg=R0801
        test_data: tuple = (
            ('1plus2plus3plus4', '10'),
            ('1minus2minus3minus4', '-8'),
            ('1plus2plus3minus4', '2'))

        for s, expected in test_data:
            # pylint: disable-msg=R0801
            actual_result = calculate(s)
            with allure.step(f"Enter string ({s}) and verify the "
                             f"expected output ({expected}) vs "
                             f"actual result ({actual_result})"):
                print_log(s=s,
                          expected=expected,
                          result=actual_result)
            # pylint: enable-msg=R0801
                self.assertEqual(expected,
                                 actual_result)
