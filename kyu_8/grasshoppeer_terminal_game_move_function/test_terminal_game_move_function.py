"""
Test for -> Grasshopper - Terminal game move function.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.grasshoppeer_terminal_game_move_function.terminal_game_move_function \
    import move


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Math")
@allure.sub_suite("Unit Tests")
@allure.feature("Calculation")
@allure.story('Grasshopper - Terminal game move function')
@allure.tag('FUNDAMENTALS')
@allure.link(
    url='https://www.codewars.com/kata/563a631f7cbbc236cf0000c2',
    name='Source/Kata')
# pylint: enable=R0801
class MoveTestCase(unittest.TestCase):
    """Testing move function."""

    def test_move(self):
        """
        Testing 'move' function with various test data.

        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("move function tests")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>The player rolls the dice and moves the number"
            "of spaces indicated by the dice two times.</p>"
            "<p>Pass position and roll and compare the output"
            "to the expected result.</p>")
        # pylint: enable=R0801
        with allure.step("Test start position zero"):
            position: int = 0
            roll: int = 4
            expected: int = 8

            print_log(position=position,
                      roll=roll,
                      expected=expected)
            self.assertEqual(move(position, roll), expected)

        with allure.step("Test start position even number"):
            position = 3
            roll = 6
            expected = 15

            print_log(position=position,
                      roll=roll,
                      expected=expected)
            self.assertEqual(move(position, roll), expected)

        with allure.step("Test start position odd number"):
            position = 2
            roll = 5
            expected = 12

            print_log(position=position,
                      roll=roll,
                      expected=expected)
            self.assertEqual(move(position, roll), expected)
