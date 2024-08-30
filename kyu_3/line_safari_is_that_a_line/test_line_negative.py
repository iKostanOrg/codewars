"""
Testing Line Safari functionality
Negative test cases

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS STRINGS

import unittest
import pytest
import allure
from utils.log_func import print_log
from kyu_3.line_safari_is_that_a_line.line_safari import line


@allure.epic('3 kyu')
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Line Safari - Is that a line?')
@allure.tag('ALGORITHMS',
            'STRINGS')
@allure.link(
    url='https://www.codewars.com/kata/59c5d0b0a25c8c99ca000237/train/python',
    name='Source/Kata')
@pytest.mark.skip(reason="The solution is not ready")
class LineNegativeTestCase(unittest.TestCase):
    """
    Testing Line Safari functionality
    Negative test cases
    """

    def test_line_negative(self):
        """
        Testing Line Safari functionality
        Negative test cases
        """

        allure.dynamic.title("Testing Line Safari functionality - NEGATIVE")
        # pylint: disable-msg=R0801
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>The function should return true/false if it can detect a one "
            "and only one \"valid\" line joining those points.</p>")
        test_data = (
            ["X-----|----X"],
            [" X  ",
             " |  ",
             " +  ",
             " X  "],
            ["   |--------+    ",
             "X---        ---+ ",
             "               | ",
             "               X "],
            ["              ",
             "   +------    ",
             "   |          ",
             "X--+      X   ",
             "              "],
            ["      +------+",
             "      |      |",
             "X-----+------+",
             "      |       ",
             "      X       "],
        )
        # pylint: enable-msg=R0801
        expected = False
        for grid in test_data:
            actual_result = line(grid)

            print()
            for row in grid:
                print(row)

            print_log(expected=expected,
                      actual_result=actual_result)

            with allure.step("Enter a test grid and compare "
                             "the output vs expected result"):
                self.assertEqual(expected, actual_result)
