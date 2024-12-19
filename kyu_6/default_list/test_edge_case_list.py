"""
Test for edge case -> DefaultList.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS CLASSES BASIC LANGUAGE FEATURES
# OBJECT-ORIENTED PROGRAMMING

import unittest
import allure
from utils.log_func import print_log
from kyu_6.default_list.default_list import DefaultList


# pylint: disable=duplicate-code
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Object-Oriented Programming")
@allure.sub_suite("Unit Tests")
@allure.feature("Classes")
@allure.story('DefaultList')
@allure.tag('FUNDAMENTALS',
            'CLASSES',
            'BASIC LANGUAGE FEATURES',
            'OBJECT-ORIENTED PROGRAMMING')
@allure.link(
    url='https://www.codewars.com/kata/5e882048999e6c0023412908',
    name='Source/Kata')
class EdgeCaseListTestCase(unittest.TestCase):
    """Testing 'DefaultList' class with edge cases."""
    # pylint: enable=duplicate-code

    def test_default_list_edge_cases_pop(self):
        """
        Testing 'DefaultList' class: pop.

        Tests regular pop operations and edge case of popping from empty list.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'DefaultList' class: edge cases for pop")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing edge cases for pop method.</p>")
        # pylint: enable-msg=R0801
        with allure.step("Create a default/empty list:"):
            default_value = 'default'
            empty_list = DefaultList([], default_value)

        with allure.step("Test popping from empty list without index:"):
            actual = empty_list.pop()
            print_log(lst=empty_list, i=None, expected=default_value, actual=actual)
            self.assertEqual(default_value, actual)

        with allure.step("Test popping from empty list with index:"):
            actual = empty_list.pop(0)
            print_log(lst=empty_list, i=0, expected=default_value, actual=actual)
            self.assertEqual(default_value, actual)

        with allure.step("Test popping from list with elements:"):
            test_list = DefaultList([1, 2, 3], default_value)

        with allure.step("Test popping from list with elements and no index:"):
            actual = test_list.pop()
            print_log(lst=test_list, i=None, expected=3, actual=actual)
            self.assertEqual(3, actual)

        with allure.step("Test popping from list with elements and index:"):
            actual = test_list.pop(0)
            print_log(lst=test_list, i=0, expected=1, actual=actual)
            self.assertEqual(1, actual)
