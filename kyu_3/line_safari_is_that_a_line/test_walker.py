"""
Testing Walker Class
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS STRINGS

import unittest
import allure
from utils.log_func import print_log
from kyu_3.line_safari_is_that_a_line.walker_class import Walker


# pylint: disable-msg=R0801
@allure.epic('3 kyu')
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Line Safari - Is that a line?')
@allure.tag('ALGORITHMS',
            'STRINGS')
@allure.link(
    url='https://www.codewars.com/kata/59c5d0b0a25c8c99ca000237',
    name='Source/Kata')
# pylint: enable-msg=R0801
class WalkerClassTestCase(unittest.TestCase):
    """
    Testing Walker class.
    """
    def test_starting_position_from_positives(self):
        """
        Testing Walker class.
        Testing starting position property based on positive grids.
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title(
            "Testing Walker class - position property from positive grids")
        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing position property based on positive grids.</p>")
        # pylint: enable-msg=R0801
        test_data: tuple = (
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
                             f"result {expected}"):
                self.assertEqual(expected, actual_result)

    def test_starting_position_from_negatives(self):
        """
        Testing Walker class.
        Testing starting position property based on negative grids.
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title(
            "Testing Walker class - position property from negative grids")
        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing position property based on negative grids.</p>")
        # pylint: disable-msg=R0801
        test_data: tuple = (
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
             "      X       "])

        expected: str = 'X'
        for grid in test_data:
            walker: Walker = Walker(grid)
            actual_result: str = walker.position

            print_log(grid=grid,
                      expected=expected,
                      actual_result=actual_result)

            with allure.step("Enter a test grid and compare "
                             "the output/position vs expected "
                             f"result {expected}"):

                self.assertEqual(expected, actual_result)
