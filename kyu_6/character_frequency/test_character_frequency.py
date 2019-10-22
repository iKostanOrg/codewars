#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS STRINGS UTILITIES

import unittest
import allure
from utils.log_func import print_log
from kyu_6.character_frequency.character_frequency import letter_frequency


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Character frequency')
class LetterFrequencyTestCase(unittest.TestCase):
    """
    Testing letter_frequency function
    """
    def test_letter_frequency_all_lower(self):
        """
        Testing letter_frequency function
        where all chars are in lower case
        :return:
        """

        allure.dynamic.title("All chars are in lower case")
        allure.dynamic.severity(allure.severity_level.CRITICAL)

        with allure.step("Pass a test string and verify the result"):

            string = 'wklv lv d vhfuhw phvvdjh'

            result = letter_frequency(string)

            expected = [('v', 5), ('h', 4), ('d', 2), ('l', 2),
                        ('w', 2), ('f', 1), ('j', 1), ('k', 1),
                        ('p', 1), ('u', 1)]

            print_log(string=string, expected=expected)

            self.assertEqual(expected, result)

    def test_letter_frequency_mixed(self):
        """
        Testing letter_frequency function
        where all chars are in mixed case
        :return:
        """

        allure.dynamic.title("All chars are in mixed case")
        allure.dynamic.severity(allure.severity_level.CRITICAL)

        with allure.step("Pass a test string and verify the result"):
            string = "As long as I'm learning something, " \
                     "I figure I'm OK - it's a decent day."

            result = letter_frequency(string)

            expected = [('i', 7), ('a', 5), ('e', 5), ('n', 5),
                        ('g', 4), ('s', 4), ('m', 3), ('o', 3),
                        ('t', 3), ('d', 2), ('l', 2), ('r', 2),
                        ('c', 1), ('f', 1), ('h', 1), ('k', 1),
                        ('u', 1), ('y', 1)]

            print_log(string=string, expected=expected)

            self.assertEqual(expected, result)

    def test_letter_frequency_all_caps(self):
        """
        Testing letter_frequency function
        where all chars are in upper case
        :return:
        """

        allure.dynamic.title("All chars are in upper case")
        allure.dynamic.severity(allure.severity_level.CRITICAL)

        with allure.step("Pass a test string and verify the result"):

            string = 'IWT LDGAS XH HIXAA P LTXGS EAPRT, ' \
                     'STHEXIT BN TUUDGIH ID BPZT RATPG ' \
                     'PCS ETGUTRI HTCHT DU XI.'

            result = letter_frequency(string)

            expected = [('t', 12), ('i', 7), ('h', 6), ('a', 5),
                        ('g', 5), ('p', 5), ('x', 5), ('d', 4),
                        ('s', 4), ('u', 4), ('e', 3), ('r', 3),
                        ('b', 2), ('c', 2), ('l', 2), ('n', 1),
                        ('w', 1), ('z', 1)]

            print_log(string=string, expected=expected)

            self.assertEqual(expected, result)
