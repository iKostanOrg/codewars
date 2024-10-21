"""
Test for -> Remove First and Last Character
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS  BASIC LANGUAGE FEATURES  STRINGS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.remove_first_and_last_character.remove_char \
    import remove_char


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Remove First and Last Character')
@allure.tag('FUNDAMENTALS',
            'BASIC LANGUAGE FEATURES',
            'STRINGS')
@allure.link(
    url='https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0',
    name='Source/Kata')
# pylint: enable=R0801
class RemoveCharTestCase(unittest.TestCase):
    """
    Testing remove_char function
    """

    def test_remove_char(self):
        """
        Test that 'remove_char' function
        removes the first and
        last characters of a string.
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing remove_char function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable=R0801
        with allure.step("Pass 'eloquent' string and verify the output"):
            string: str = 'eloquent'
            expected: str = 'loquen'
            print_log(string=string, expected=expected)
            self.assertEqual(remove_char(string), expected)

        with allure.step("Pass 'country' string and verify the output"):
            string: str = 'country'
            expected: str = 'ountr'
            print_log(string=string, expected=expected)
            self.assertEqual(remove_char(string), expected)

        with allure.step("Pass 'person' string and verify the output"):
            string: str = 'person'
            expected: str = 'erso'
            print_log(string=string, expected=expected)
            self.assertEqual(remove_char(string), expected)

        with allure.step("Pass 'place' string and verify the output"):
            string: str = 'place'
            expected: str = 'lac'
            print_log(string=string, expected=expected)
            self.assertEqual(remove_char(string), expected)

        with allure.step("Pass 'ok' string and verify the output"):
            string: str = 'ok'
            expected: str = ''
            print_log(string=string, expected=expected)
            self.assertEqual(remove_char(string), expected)
