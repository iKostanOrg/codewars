"""
Testing for altERnaTIng cAsE <=> ALTerNAtiNG CaSe.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_8.alternating_case.alternating_case \
    import to_alternating_case


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('altERnaTIng cAsE <=> ALTerNAtiNG CaSe')
@allure.tag('FUNDAMENTALS')
@allure.link(
    url='https://www.codewars.com/kata/56efc695740d30f963000557',
    name='Source/Kata')
# pylint: enable=R0801
class AlternatingCaseTestCase(unittest.TestCase):
    """Testing to_alternating_case function."""

    @parameterized.expand([
        ("hello world", "HELLO WORLD"),
        ("HELLO WORLD", "hello world"),
        ("HeLLo WoRLD", "hEllO wOrld"),
        ("hello WORLD", "HELLO world"),
        ("12345", "12345"),
        ("1a2b3c4d5e", "1A2B3C4D5E"),
        ("String.prototype.toAlternatingCase",
         "sTRING.PROTOTYPE.TOaLTERNATINGcASE"),
        ("Hello World", "hELLO wORLD"),
        ("altERnaTIng cAsE", "ALTerNAtiNG CaSe")])
    def test_alternating_case(self, string, expected):
        """
        Testing to_alternating_case function with various test data.

        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing to_alternating_case function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="'
            'https://www.codewars.com/users/myFirstCode/badges/large'
            '">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable=R0801
        with allure.step(f"Enter test string: {string} "
                         f"and verify the expected output: {expected}."):
            print_log(string=string, expected=expected)
            self.assertEqual(to_alternating_case(string), expected)
