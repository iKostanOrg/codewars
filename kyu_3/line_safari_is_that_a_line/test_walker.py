"""
Testing Walker Class
"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS STRINGS

import allure
import unittest

import pytest

from utils.log_func import print_log
from kyu_3.line_safari_is_that_a_line.walker_class import Walker


@allure.epic('3 kyu')
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Line Safari - Is that a line?')
@allure.tag('ALGORITHMS', 'STRINGS')
@allure.link(
    url='https://www.codewars.com/kata/59c5d0b0a25c8c99ca000237/train/python',
    name='Source/Kata')
@pytest.mark.skip(reason="The solution is not ready")
class WalkerClassTestCase(unittest.TestCase):
    """
    Testing Walker class
    """

    def test_starting_position_from_positives(self):
        """
        Testing Walker class
        Testing starting position property based on positive grids
        """

        allure.dynamic.title("Testing Walker class - position property from positive grids")
        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing position property based on positive grids.</p>")

        test_data = (
            ["           ",
             "X---------X",
             "           ",
             "           "],
            ["     ",
             "  X  ",
             "  |  ",
             "  |  ",
             "  X  "],
            ["                    ",
             "     +--------+     ",
             "  X--+        +--+  ",
             "                 |  ",
             "                 X  ",
             "                    "],
            ["                     ",
             "    +-------------+  ",
             "    |             |  ",
             " X--+      X------+  ",
             "                     "],
            ["                      ",
             "   +-------+          ",
             "   |      +++---+     ",
             "X--+      +-+   X     "]
        )

        expected = 'X'
        for grid in test_data:
            walker = Walker(grid)
            actual_result = walker.position
            print_log(grid=grid,
                      expected=expected,
                      actual_result=actual_result)

            with allure.step("Enter a test grid and compare "
                             "the output/position vs expected "
                             "result {}".format(expected)):
                self.assertEqual(expected, actual_result)

    def test_starting_position_from_negatives(self):
        """
        Testing Walker class
        Testing starting position property based on negative grids
        """

        allure.dynamic.title("Testing Walker class - position property from negative grids")
        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing position property based on negative grids.</p>")

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

        expected = 'X'
        for grid in test_data:
            walker = Walker(grid)
            actual_result = walker.position
            print_log(grid=grid,
                      expected=expected,
                      actual_result=actual_result)

            with allure.step("Enter a test grid and compare "
                             "the output/position vs expected "
                             "result {}".format(expected)):
                self.assertEqual(expected, actual_result)
