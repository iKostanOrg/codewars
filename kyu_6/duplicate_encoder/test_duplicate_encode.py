"""
Test for -> Duplicate Encoder.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS STRINGS ARRAYS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_6.duplicate_encoder.duplicate_encode \
    import duplicate_encode


# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Duplicate Encoder')
@allure.tag('FUNDAMENTALS',
            'STRINGS',
            'ARRAYS')
@allure.link(
    url='https://www.codewars.com/kata/54b42f9314d9229fd6000d9c',
    name='Source/Kata')
# pylint: enable-msg=R0801
class DuplicateEncodeTestCase(unittest.TestCase):
    """Testing duplicate_encode function."""

    @parameterized.expand([
        ("din", "((("),
        ("recede", "()()()"),
        ("Success", ")())())"),
        ("(( @", "))((")])
    def test_duplicate_encode(self, string, expected):
        """
        Testing duplicate_encode function with various test inputs.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing duplicate_encode function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step(f"Enter test string: {string} "
                         f"and verify the output: {expected}."):
            print_log(string=string, expected=expected)
            self.assertEqual(expected, duplicate_encode(string))
