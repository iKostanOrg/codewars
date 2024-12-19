"""
Test for -> Character frequency.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS STRINGS UTILITIES

import unittest
import allure
from utils.log_func import print_log
from kyu_6.character_frequency.character_frequency \
    import letter_frequency


# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Character frequency')
@allure.tag('ALGORITHMS',
            'STRINGS',
            'UTILITIES')
@allure.link(
    url='https://www.codewars.com/kata/53e895e28f9e66a56900011a',
    name='Source/Kata')
# pylint: enable-msg=R0801
class LetterFrequencyTestCase(unittest.TestCase):
    """Testing letter_frequency function."""

    def test_letter_frequency_all_lower(self):
        """
        Testing letter_frequency function where all chars are in lower case.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("All chars are in lower case")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Pass a test string and verify the result"):
            string: str = 'wklv lv d vhfuhw phvvdjh'
            result: list = letter_frequency(string)
            expected: list = [('v', 5), ('h', 4), ('d', 2), ('l', 2),
                              ('w', 2), ('f', 1), ('j', 1), ('k', 1),
                              ('p', 1), ('u', 1)]

            print_log(string=string, expected=expected)
            self.assertEqual(expected, result)

    def test_letter_frequency_mixed(self):
        """
        Testing letter_frequency function where all chars are in mixed case.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("All chars are in mixed case")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Pass a test string and verify the result"):
            string: str = "As long as I'm learning something, " \
                          "I figure I'm OK - it's a decent day."
            result: list = letter_frequency(string)
            expected: list = [('i', 7), ('a', 5), ('e', 5), ('n', 5),
                              ('g', 4), ('s', 4), ('m', 3), ('o', 3),
                              ('t', 3), ('d', 2), ('l', 2), ('r', 2),
                              ('c', 1), ('f', 1), ('h', 1), ('k', 1),
                              ('u', 1), ('y', 1)]

            print_log(string=string, expected=expected)
            self.assertEqual(expected, result)

    def test_letter_frequency_all_caps(self):
        """
        Testing letter_frequency function where all chars are in upper case.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("All chars are in upper case")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Pass a test string and verify the result"):
            string: str = 'IWT LDGAS XH HIXAA P LTXGS EAPRT, ' \
                          'STHEXIT BN TUUDGIH ID BPZT RATPG ' \
                          'PCS ETGUTRI HTCHT DU XI.'
            result: list = letter_frequency(string)
            expected: list = [('t', 12), ('i', 7), ('h', 6), ('a', 5),
                              ('g', 5), ('p', 5), ('x', 5), ('d', 4),
                              ('s', 4), ('u', 4), ('e', 3), ('r', 3),
                              ('b', 2), ('c', 2), ('l', 2), ('n', 1),
                              ('w', 1), ('z', 1)]

            print_log(string=string, expected=expected)
            self.assertEqual(expected, result)
