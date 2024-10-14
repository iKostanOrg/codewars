"""
Test for -> Multiply
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS, INTRODUCTION

import unittest
import allure
from utils.log_func import print_log
from kyu_8.multiply.multiply import multiply


# pylint: disable-msg=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Math")
@allure.sub_suite("Unit Tests")
@allure.feature("Multiplication")
@allure.story('Multiply')
@allure.tag('FUNDAMENTALS',
            'INTRODUCTION')
@allure.link(
    url='https://www.codewars.com/kata/50654ddff44f800200000004',
    name='Source/Kata')
# pylint: enable-msg=R0801
class MultiplyTestCase(unittest.TestCase):
    """
    Testing multiply function
    """

    def test_multiply(self):
        """
        Verify that multiply function
        returns correct result
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("'multiply' function verification")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Assert (a * b) result"):
            a: int = 1
            b: int = 2
            expected: int = a * b
            print_log(a=a, b=b, expected=expected)
            self.assertEqual(expected, multiply(a, b))
