"""
Test for -> First character that repeats.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS STRINGS FUNDAMENTALS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_6.longest_repetition.longest_repetition \
    import longest_repetition


# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('First character that repeats')
@allure.tag('ALGORITHMS',
            'STRINGS',
            'FUNDAMENTALS')
@allure.link(
    url='https://www.codewars.com/kata/586d6cefbcc21eed7a001155',
    name='Source/Kata')
class LongestRepetitionTestCase(unittest.TestCase):
    """Testing longest_repetition function."""

    @parameterized.expand([
        # [input, expected],
        ["aaaabb", ('a', 4)],
        ["bbbaaabaaaa", ('a', 4)],
        ["cbdeuuu900", ('u', 3)],
        ["abbbbb", ('b', 5)],
        ["aabb", ('a', 2)],
        ["ba", ('b', 1)],
        ["", ('', 0)]])
    def test_longest_repetition(self, string, expected):
        """
        Test 'longest_repetition' with various test data.

        For a given string s find the character c (or C) with
        the longest consecutive repetition and return: (c, l)
        where l (or L) is the length of the repetition.

        For empty string return: ('', 0)
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'longest_repetition' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Pass string and verify the output"):
            print_log(string=string, expected=expected)
            self.assertEqual(expected, longest_repetition(string))
