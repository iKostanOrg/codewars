"""
Test for -> First character that repeats
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS STRINGS FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_6.longest_repetition.longest_repetition import longest_repetition


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
    url='https://www.codewars.com/kata/586d6cefbcc21eed7a001155/train/python',
    name='Source/Kata')
# pylint: enable-msg=R0801
class LongestRepetitionTestCase(unittest.TestCase):
    """
    Testing longest_repetition function
    """
    def test_longest_repetition(self):
        """
        For a given string s find the character c (or C) with
        longest consecutive repetition and return: (c, l)
        where l (or L) is the length of the repetition.

        For empty string return: ('', 0)
        :return:
        """
        allure.dynamic.title("Testing 'longest_repetition' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")

        with allure.step("Pass string and verify the output"):
            test_data = [
                # [input, expected],
                ["aaaabb", ('a', 4)],
                ["bbbaaabaaaa", ('a', 4)],
                ["cbdeuuu900", ('u', 3)],
                ["abbbbb", ('b', 5)],
                ["aabb", ('a', 2)],
                ["ba", ('b', 1)],
                ["", ('', 0)],
            ]

            for t in test_data:
                print_log(string=t[0], expected=t[1])
                self.assertEqual(t[1], longest_repetition(t[0]))
