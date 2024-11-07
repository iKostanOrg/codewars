"""
Test for -> Find the odd int
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


# FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_6.find_the_odd_int.find_the_odd_int import find_it


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Find the odd int')
@allure.tag('FUNDAMENTALS')
@allure.link(
    url='https://www.codewars.com/kata/54da5a58ea159efa38000836',
    name='Source/Kata')
class FindTheOddIntTestCase(unittest.TestCase):
    """
    Testing find_it function
    """
    def test_something(self):
        """
        Sample testing.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title(
            "Find the int that appears an odd number of times")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        test_data: tuple = (
            ([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5],
             5,
             'should return 5 (because it appears 3 times)'),
            ([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10],
             1,
             'should return 1 (because it appears 1 time)'),
            ([-15, -14, -11, -11, -7, -7, -7, -5, -11, -7, -7, -5, -7, -14,
              -7, -15, -7, -5, -11, -14, -5, -5, -7, -7, -14, -11, -15, -7,
              -5, -11, -7, -15, -15, -15, -5, -15, -15],
             -5,
             'Random tests'),
            ([14, 2, -3, -12, -17, 14, 2, 2, -17, -17, -12, -12, 14, -17, -1,
              2, -12, -3, -17, -12, -17, -1, 14, -12, 2],
             2,
             'Random tests'))

        with allure.step("Assert the result"):
            for data in test_data:
                lst, expected, msg = data
                print_log(list=lst, expected=expected, msg=msg)
                self.assertEqual(find_it(lst), expected, msg=msg)
