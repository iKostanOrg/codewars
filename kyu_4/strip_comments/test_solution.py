"""
Test for -> Strip Comments

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS STRINGS

import allure
import unittest
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
@allure.link(url='https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python',
             name='Source/Kata')
class SolutionTestCase(unittest.TestCase):

    def test_solution(self):
        """
        Testing 'solution' function

        The solution should strips all text that follows any
        of a set of comment markers passed in. Any whitespace at
        the end of the line should also be stripped out.
        """

        allure.dynamic.title("Testing 'solution' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>Testing permutations function</p>"
                                        "<p>The solution should strips all text that follows any "
                                        "of a set of comment markers passed in. Any whitespace at "
                                        "the end of the line should also be stripped out.</p>")

        test_data = (
             ("apples, pears # and bananas\ngrapes\nbananas !apples",
              ["#", "!"],
              "apples, pears\ngrapes\nbananas"),
             ("a #b\nc\nd $e f g",
              ["#", "$"],
              "a\nc\nd"),
        )

        for string, markers, expected in test_data:
            actual_result = solution(string, markers)
            print_log(string=string,
                      expected=expected,
                      actual_result=actual_result)

            with allure.step("Enter a test string ({}) and "
                             "verify the output ({}) vs "
                             "expected ({})".format(string,
                                                    actual_result,
                                                    expected)):
                self.assertEqual(expected, actual_result)
