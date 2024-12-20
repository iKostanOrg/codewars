"""
Test for -> Always perfect.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS STRINGS STRING FORMATTING
# FORMATTING ALGORITHMS ARRAYS MATHEMATICS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_7.always_perfect.check_root import check_root


# pylint: disable-msg=R0801
@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite('Data Structures')
@allure.sub_suite('Unit Tests')
@allure.feature('Lists')
@allure.story('Always perfect')
@allure.tag('FUNDAMENTALS',
            'STRINGS',
            'STRING FORMATTING',
            'FORMATTING',
            'ALGORITHMS',
            'ARRAYS',
            'MATHEMATICS')
@allure.link(
    url='https://www.codewars.com/kata/55f3facb78a9fd5b26000036',
    name='Source/Kata')
# pylint: enable-msg=R0801
class CheckRootTestCase(unittest.TestCase):
    """Testing 'check_root' function."""

    @parameterized.expand([
        ('4,5,6,7', '841, 29'),
        ('3,s,5,6', 'incorrect input'),
        ('11,13,14,15', 'not consecutive'),
        ('10,11,12,13,15', 'incorrect input'),
        ('10,11,12,13', '17161, 131'),
        ('::*-3,-2,-1,0', 'incorrect input')])
    def test_check_root(self,string, expected):
        """
        Testing 'check_root' function with various test inputs.

        A function which takes numbers separated by commas
        in string format and returns the number which is a
        perfect square and the square root of that number.

        If string contains other characters than number, or
        it has more or less than 4 numbers separated by comma
        function returns 'incorrect input'.

        If string contains 4 numbers but not consecutive it
        returns 'not consecutive'.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing check_root function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="'
            'https://www.codewars.com/users/myFirstCode/badges/large'
            '">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step(f"Enter test string: {string} "
                         f"and verify the output: {expected}."):
            print_log(string=string, expected=expected)
            self.assertEqual(expected, check_root(string))
