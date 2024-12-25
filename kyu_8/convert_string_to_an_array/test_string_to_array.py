"""
Test for -> Convert a string to an array.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS ARRAYS STRINGS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_8.convert_string_to_an_array.string_to_array \
    import string_to_array


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Convert a string to an array')
@allure.tag('FUNDAMENTALS',
            'ARRAYS',
            'STRINGS')
@allure.link(
    url='https://www.codewars.com/kata/57e76bc428d6fbc2d500036d',
    name='Source/Kata')
# pylint: enable=R0801
class StringToArrayTestCase(unittest.TestCase):
    """Testing string_to_array function."""

    @parameterized.expand([
        ("Robin Singh", ["Robin", "Singh"]),
        ("CodeWars", ["CodeWars"]),
        ("I love arrays they are my favorite",
         ["I", "love", "arrays", "they", "are", "my", "favorite"]),
        ("1 2 3", ["1", "2", "3"]),
        ("", [""])])
    def test_string_to_array(self, s, expected):
        """
        Testing string_to_array function.

        A function to split a string and
        convert it into an array of words.
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing string_to_array function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable=R0801
        with allure.step(f"Enter a test string: {s} "
                         f"and verify the output: {expected}."):
            print_log(s=s, expected=expected)
            self.assertEqual(expected, string_to_array(s))
