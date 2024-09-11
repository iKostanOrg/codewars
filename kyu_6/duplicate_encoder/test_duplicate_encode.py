"""
Test for -> Duplicate Encoder
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS STRINGS ARRAYS

import unittest
import allure
from utils.log_func import print_log
from kyu_6.duplicate_encoder.duplicate_encode import duplicate_encode


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
    url='',
    name='Source/Kata')
# pylint: enable-msg=R0801
class DuplicateEncodeTestCase(unittest.TestCase):
    """
    Testing duplicate_encode function
    """

    def test_duplicate_encode(self):
        """
        Testing duplicate_encode function
        with various test inputs
        :return:
        """

        allure.dynamic.title("Testing duplicate_encode function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")

        with allure.step("Enter test string and verify the output"):
            test_data = [
                ("din", "((("),
                ("recede", "()()()"),
                ("Success", ")())())"),
                ("(( @", "))((")
            ]

            for string, expected in test_data:
                print_log(string=string, expected=expected)
                self.assertEqual(expected, duplicate_encode(string))
