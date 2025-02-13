"""
Test for -> 'Isograms'.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS STRINGS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_7.isograms.is_isogram import is_isogram


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Isograms')
@allure.tag('FUNDAMENTALS',
            'STRINGS')
@allure.link(
    url='https://www.codewars.com/kata/54ba84be607a92aa900000f1',
    name='Source/Kata')
class IsIsogramTestCase(unittest.TestCase):
    """Testing 'is_isogram' function."""

    @parameterized.expand([
        ("Dermatoglyphics", True, ''),
        ("isogram", True, ''),
        ("aba", False, "same chars may not be adjacent"),
        ("moOse", False, "same chars may not be same case"),
        ("isIsogram", False, ''),
        ('', True, "an empty string is a valid isogram")])
    def test_is_isogram(self, string, expected, message):
        """
        Testing 'is_isogram' function.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'is_isogram' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Verify that the function that determines corectly "
            "whether a string that contains only letters is an isogram. "
            "Assume the empty string is an isogram. Ignore letter case."
            "</p>")
        # pylint: enable-msg=R0801
        with allure.step(f"Enter a test string {string} "
                         f"and verify the expected result: {expected}."):
            actual_result: bool = is_isogram(string)
            print_log(expected=expected, value=string, message=message)
            self.assertEqual(expected, actual_result, message)
