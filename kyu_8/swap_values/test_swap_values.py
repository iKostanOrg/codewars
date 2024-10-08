"""
Test  for -> Swap Values
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# BUGS ARRAYS FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.swap_values.swap_values import swap_values


# pylint: disable-msg=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Swap Values')
@allure.tag('BUGS',
            'ARRAYS',
            'FUNDAMENTALS')
@allure.link(
    url='https://www.codewars.com/kata/5388f0e00b24c5635e000fc6',
    name='Source/Kata')
# pylint: enable-msg=R0801
class SwapValuesTestCase(unittest.TestCase):
    """
    Testing swap_values function
    """

    def test_swap_values(self):
        """
        Testing swap_values function
        """
        allure.dynamic.title("Testing swap_values function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")

        with allure.step("Pass a list with 2 values and swap them"):
            swap: list = [1, 2]
            expected: list = [2, 1]
            swap_values(swap)

            print_log(list=swap, expected=expected)
            self.assertEqual(swap[0], 2)
            self.assertEqual(swap[1], 1)
