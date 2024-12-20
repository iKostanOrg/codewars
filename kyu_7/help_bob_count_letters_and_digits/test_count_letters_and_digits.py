"""
Test for -> Help Bob count letters and digits.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS STRINGS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_7.help_bob_count_letters_and_digits.count_letters_and_digits \
    import (count_letters_and_digits)


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite('Fundamentals')
@allure.sub_suite('Unit Tests')
@allure.feature('String')
@allure.story('Help Bob count letters and digits.')
@allure.tag('FUNDAMENTALS',
            'STRINGS')
@allure.link(
    url='https://www.codewars.com/kata/5738f5ea9545204cec000155',
    name='Source/Kata')
class CalculateTestCase(unittest.TestCase):
    """Testing count_letters_and_digits function."""

    @parameterized.expand([
        ('n!!ice!!123', 7),
        ('de?=?=tttes!!t', 8),
        ('', 0),
        ('!@#$%^&`~.', 0),
        ('u_n_d_e_r__S_C_O_R_E', 10)])
    def test_count_letters_and_digits(self, s, expected):
        """
        Testing the function with various test data.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing count_letters_and_digits function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Test a method that can determine how many letters "
            "and digits are in a given string.</p>")
        # pylint: enable-msg=R0801
        actual_result: int = count_letters_and_digits(s)
        with allure.step(f"Enter string ({s}) and verify the "
                         f"expected output ({expected}) vs "
                         f"actual result ({actual_result})"):
            print_log(s=s, expected=expected, result=actual_result)
            self.assertEqual(expected, actual_result)
