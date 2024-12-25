"""
Test for -> Logical Calculator ValueError.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS ARRAYS

import unittest
import allure
import pytest
from utils.log_func import print_log
from kyu_8.logical_calculator.logical_calculator \
    import logical_calc


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Logical Calculator')
@allure.tag('FUNDAMENTALS',
            'ARRAYS'
            "ValueError")
@allure.link(
    url='https://www.codewars.com/kata/57096af70dad013aa200007b',
    name='Source/Kata')
# pylint: enable=R0801
class LogicalCalculatorValueErrorTestCase(unittest.TestCase):
    """Testing ValueError."""

    def test_logical_calc_value_error(self):
        """
        Testing ValueError for logical_calc function.
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing ValueError for logical_calc function.")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="'
            'https://www.codewars.com/users/myFirstCode/badges/large'
            '">'
            '<h3>Test Description:</h3>'
            "<p>"
            "Test Python Exception Handling Using 'pytest.raises'."
            "</p>")
        # pylint: enable=R0801
        with (allure.step("Pass an array with invalid operator.")):
            arr: list = []
            op: str = 'RO'  # invalid operator
            operators: list = ['AND', 'OR', 'XOR']
            err = (f'ERROR: {op} is not a valid operator. '
                   f'Please use one of the followings: {operators}')
            with pytest.raises(ValueError) as calc_err:
                logical_calc(arr, op)
            self.assertEqual(str(calc_err.value), err)
