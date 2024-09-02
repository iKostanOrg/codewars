"""
Test for -> Range Extraction

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS STRING FORMATTING FORMATTING STRINGS

import unittest
import allure
from utils.log_func import print_log
from kyu_4.range_extraction.solution import solution


# pylint: disable-msg=R0801
@allure.epic("4 kyu")
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story("Range Extraction")
@allure.tag('ALGORITHMS',
            'STRING',
            'FORMATTING',
            'FORMATTING',
            'STRINGS')
@allure.link(url='https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python',
             name='Source/Kata')
# pylint: enable-msg=R0801
class SolutionTestCase(unittest.TestCase):

    def test_solution(self):
        """
        Testing solution function
        """

        allure.dynamic.title("Testing solution function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing permutations function</p>"
            "<p>Test the solution so that it takes a list of integers "
            "in increasing order and returns a correctly formatted "
            "string in the range format.</p>")

        test_data = [
            ([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9,
              10, 11, 14, 15, 17, 18, 19, 20],
             '-6,-3-1,3-5,7-11,14,15,17-20'),
            ([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20],
             '-3--1,2,10,15,16,18-20'),
            ([-91, -90, -87, -84, -81, -78, -77, -76, -74, -72,
              -70, -69, -66, -65, -63, -60, -58, -57, -54],
             '-91,-90,-87,-84,-81,-78--76,-74,-72,-70,-69,-66,-65,-63,-60,-58,-57,-54')
        ]

        for test_list, expected in test_data:
            actual_result = solution(test_list)
            print_log(test_listg=test_list,
                      expected=expected,
                      actual_result=actual_result)

            with allure.step(f"Enter a test list ({test_list}) and "
                             f"verify the output ({actual_result}) vs "
                             f"expected ({expected})"):
                self.assertEqual(expected, actual_result)
