"""
Test for -> First non-repeating character.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS STRINGS SEARCH

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_5.first_non_repeating_character.first_non_repeating_letter import (
    first_non_repeating_letter
)


# pylint: disable-msg=R0801
@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('First non-repeating character')
@allure.tag('ALGORITHMS',
            'STRINGS',
            'SEARCH')
@allure.link(
    url='https://www.codewars.com/kata/52bc74d4ac05d0945d00054e',
    name='Source/Kata')
# pylint: enable-msg=R0801
class FirstNonRepeatingLetterTestCase(unittest.TestCase):
    """Testing first_non_repeating_letter function."""

    @parameterized.expand([
        ('a', 'a'),
        ('stress', 't'),
        ('moonmen', 'e'),
        ('', ''),
        ('abba', ''),
        ('aa', ''),
        ('~><#~><', '#'),
        ('hello world, eh?', 'w'),
        ('sTreSS', 'T'),
        ('Go hang a salami, I\'m a lasagna hog!', ',')])
    def test_first_non_repeating_letter(self, string, expected):
        """
        Testing a function named first_non_repeating_letter.

        The function takes a string input, and returns the first character
        that is not repeated anywhere in the string.

        For example, if given the input 'stress', the function
        should return 't', since the letter t only occurs once
        in the string, and occurs first in the string.

        As an added challenge, upper- and lowercase letters are
        considered the same character, but the function should
        return the correct case for the initial letter. For example,
        the input 'sTreSS' should return 'T'.

        If a string contains all repeating characters, it should
        return an empty string ("") or None -- see sample tests.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing first_non_repeating_letter function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step(f"Enter test string: {string} "
                         f"and verify the output: {expected}"):
            print_log(string=string, expected=expected)
            self.assertEqual(expected, first_non_repeating_letter(string))
