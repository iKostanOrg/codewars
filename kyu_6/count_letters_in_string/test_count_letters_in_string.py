"""
Test for -> Count letters in string
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS STRINGS HASHES DATA STRUCTURES

import unittest
import allure
from utils.log_func import print_log
from kyu_6.count_letters_in_string.count_letters_in_string import letter_count


# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Count letters in string')
@allure.tag('FUNDAMENTALS',
            'STRINGS',
            'HASHES',
            'DATA STRUCTURES')
@allure.link(
    url='https://www.codewars.com/kata/5808ff71c7cfa1c6aa00006d/train/python',
    name='Source/Kata')
# pylint: enable-msg=R0801
class CountLettersInStringTestCase(unittest.TestCase):
    """
    Testing 'letter_count' function
    """
    def test_count_letters_in_string(self):
        """
        Testing 'letter_count' function
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'letter_count' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Enter test string and verify the output"):
            string = "codewars"
            expected = {"a": 1, "c": 1, "d": 1, "e": 1,
                        "o": 1, "r": 1, "s": 1, "w": 1}

            print_log(string=string, expected=expected)
            self.assertEqual(expected, letter_count(string))

        with allure.step("Enter test string and verify the output"):
            string = "activity"
            expected = {"a": 1, "c": 1, "i": 2, "t": 2,
                        "v": 1, "y": 1}

            print_log(string=string, expected=expected)
            self.assertEqual(expected, letter_count(string))

        with allure.step("Enter test string and verify the output"):
            string = "arithmetics"
            expected = {"a": 1, "c": 1, "e": 1, "h": 1,
                        "i": 2, "m": 1, "r": 1, "s": 1, "t": 2}

            print_log(string=string, expected=expected)
            self.assertEqual(expected, letter_count(string))

        with allure.step("Enter test string and verify the output"):
            string = "traveller"
            expected = {"a": 1, "e": 2, "l": 2,
                        "r": 2, "t": 1, "v": 1}

            print_log(string=string, expected=expected)
            self.assertEqual(expected, letter_count(string))

        with allure.step("Enter test string and verify the output"):
            string = "daydreamer"
            expected = {"a": 2, "d": 2, "e": 2,
                        "m": 1, "r": 2, "y": 1}

            print_log(string=string, expected=expected)
            self.assertEqual(expected, letter_count(string))
