"""
Test for -> Strip Comments.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS STRINGS

import unittest
import allure
from utils.log_func import print_log
from kyu_4.strip_comments.solution import solution


@allure.epic("4 kyu")
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story("Strip Comments")
@allure.tag('ALGORITHMS',
            'STRINGS')
@allure.link(url='https://www.codewars.com/kata/51c8e37cee245da6b40000bd',
             name='Source/Kata')
class SolutionTestCase(unittest.TestCase):
    """Testing solution for Strip Comments problem."""

    def test_solution(self):
        """
        Testing 'solution' function.

        The solution should strips all text that follows any
        of a set of comment markers passed in. Any whitespace at
        the end of the line should also be stripped out.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'solution' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing permutations function</p>"
            "<p>The solution should strips all text that follows any "
            "of a set of comment markers passed in. Any whitespace at "
            "the end of the line should also be stripped out.</p>")
        # pylint: enable-msg=R0801
        test_data: tuple = (
            ("apples, pears # and bananas\ngrapes\nbananas !apples",
             ["#", "!"],
             "apples, pears\ngrapes\nbananas"),
            ("a #b\nc\nd $e f g",
             ["#", "$"],
             "a\nc\nd"))

        for string, markers, expected in test_data:
            actual_result = solution(string, markers)
            print_log(string=string,
                      expected=expected,
                      actual_result=actual_result)

            with allure.step(f"Enter a test string ({string}) and "
                             f"verify the output ({actual_result}) vs "
                             f"expected ({expected})"):
                self.assertEqual(expected, actual_result)
