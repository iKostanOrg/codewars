"""
Solution for -. Permutations

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS PERMUTATIONS STRINGS

import pytest
import unittest
import allure
from utils.log_func import print_log
from kyu_4.permutations.permutations import permutations


# pylint: disable-msg=R0801
@allure.epic("4 kyu")
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story("Permutations")
@allure.tag('ALGORITHMS',
            'PERMUTATIONS',
            'STRINGS')
@allure.link(url='https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python',
             name='Source/Kata')
@pytest.mark.skip(reason="The solution is not ready")
# pylint: enable-msg=R0801
class PermutationsTestCase(unittest.TestCase):

    def test_permutations(self):
        """
        Testing permutations function

        Test that permutations function creates all
        permutations of an input string and
        remove duplicates, if present. This means, you
        have to shuffle all letters from the input in all
        possible orders.
        """

        allure.dynamic.title("Testing permutations function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing permutations function</p>"
            "<p>Test that permutations function creates all "
            "permutations of an input string and "
            "remove duplicates, if present. This means, you "
            "have to shuffle all letters from the input in all "
            "possible orders.</p>")

        test_data = [
            ('a', ['a']),
            ('ab', ['ab', 'ba']),
            ('aabb', ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']),
            ('abc', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']),
            ('abcd', ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb',
                      'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
                      'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba',
                      'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']),
            ('dcba', ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb',
                      'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
                      'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba',
                      'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'])
        ]
        # pylint: disable-msg=R0801
        for string, expected in test_data:
            actual_result = sorted(permutations(string))
            print_log(string=string,
                      expected=expected,
                      actual_result=actual_result)

            with allure.step(f"Enter a test string ({string}) and "
                             f"verify the output ({actual_result}) vs "
                             f"expected ({expected})"):
                self.assertListEqual(sorted(expected), actual_result)
        # pylint: enable-msg=R0801
