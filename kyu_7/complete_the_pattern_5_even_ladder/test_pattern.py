"""
Test for -> Complete The Pattern #5 - Even Ladder.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ASCII FUNDAMENTALS

import unittest
import allure  # pylint: disable=import-error
from parameterized import parameterized
from utils.log_func import print_log
from kyu_7.complete_the_pattern_5_even_ladder.solution import pattern


# pylint: disable-msg=R0801
@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Complete The Pattern #5 - Even Ladder')
@allure.tag('ASCII',
            'FUNDAMENTALS')
@allure.link(
    url='https://www.codewars.com/kata/55749101ae1cf7673800003e',
    name='Source/Kata')
# pylint: enable-msg=R0801
class PatternTestCase(unittest.TestCase):
    """Testing pattern function."""

    @parameterized.expand([
        (2, "22"),
        (1, ""),
        (5, "22\n4444"),
        (6, "22\n4444\n666666"),
        (0, ""),
        (-25, "")])
    def test_pattern(self, n, expected):
        """
        Basic test case for pattern func.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Basic test case for pattern func.")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>"
            "If n <= 1 then it should return "" (i.e. empty string)."
            "</p>"
            "<p>"
            "If any odd number is passed as argument then the pattern "
            "should last up to the largest even number which is smaller "
            "than the passed odd number."
            "</p>")
        # pylint: enable-msg=R0801
        with allure.step(f"Enter test number (n): {n} "
                         f"and verify the output: {expected}"):
            result = pattern(n)
            print_log(n=n, expected=expected, result=result)
            self.assertEqual(expected, result, msg=expected)

    @parameterized.expand([
        (8, "22\n4444\n666666\n88888888")])
    def test_pattern_has_no_spaces(self, n, expected):
        """
        Output should not have any spaces..

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Test no spaces in output.")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>"
            "There are no spaces in the pattern."
            "</p>")
        # pylint: enable-msg=R0801
        with allure.step(f"Enter test number (n): {n} "
                         "and verify the output has no spaces."):
            result = pattern(n)
            print_log(n=n, expected=expected, result=result)
            self.assertEqual(result, expected)
            self.assertEqual(result.count(' '), 0)
