"""
Test for -> Basic Math (Add or Subtract).

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS STRINGS

import unittest
import allure
from parameterized import parameterized
from kyu_7.basic_math_add_or_subtract.calculate import (
    calculate,
    string_to_math)
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
    """Testing calculate function."""

    @parameterized.expand([
        ('1plus2plus3plus4', '10'),
        ('1minus2minus3minus4', '-8'),
        ('1plus2plus3minus4', '2'),
        ('1plus2minus3plus4minus5', '-1'),
        # Large numbers
        ('100plus200plus300', '600'),
        ('1000minus500plus25', '525'),
        # Floating point numbers
        ('1.5plus2.7', '4.2'),
        ('10.5minus5.25', '5.25'),
        # Spaces in input
        (' 1plus2 plus3 ', '6'),
        ('5 minus 3plus2 ', '4'),
        # Negative numbers
        ('-1plus5minus2', '2'),
        ('-10plus20minus-5', '15'),
        # Leading/trailing spaces
        ('  10plus5  ', '15'),
        ('  20minus10  ', '10')])
    def test_calculate(self, s, expected):
        """
        Testing 'calculate' function with various test data.

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
        actual_result = calculate(s)
        with allure.step(f"Enter string ({s}) and verify the "
                         f"expected output ({expected}) vs "
                         f"actual result ({actual_result})"):
            print_log(s=s, expected=expected, result=actual_result)
            # pylint: enable-msg=R0801
            self.assertEqual(expected, actual_result)

    @parameterized.expand([
        ('1plus2plus3plus4', '1+2+3+4'),
        ('1minus2minus3minus4', '1-2-3-4'),
        ('1plus2plus3minus4', '1+2+3-4'),
        ('1plus2minus3plus4minus5', '1+2-3+4-5')])
    def test_string_to_math(self, s, expected):
        """
        Testing 'string_to_math' function with various test data.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'string_to_math' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>"
            '1. convert "plus" into "+"<br>'
            '2. convert "minus" into "-"'
            "</p>")
        actual_result = string_to_math(s)
        with allure.step(f"Enter string ({s}) and verify the "
                         f"expected output ({expected}) vs "
                         f"actual result ({actual_result})"):
            print_log(s=s, expected=expected, result=actual_result)
            # pylint: enable-msg=R0801
            self.assertEqual(expected, actual_result)
