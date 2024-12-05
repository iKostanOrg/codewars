"""
Testing Battleship field validator.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS GAMES VALIDATION ARRAYS GAME BOARDS

import unittest
import allure
from kyu_3.battleship_field_validator.validator import validate_battlefield
from utils.log_func import print_log


@allure.epic('3 kyu')
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Battleship field validator')
@allure.tag('ALGORITHMS',
            'GAMES',
            'VALIDATION',
            'ARRAYS',
            'GAME BOARDS')
@allure.link(
    url='https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7',
    name='Source/Kata')
class BattleshipFieldValidatorTestCase(unittest.TestCase):
    """Testing Battleship field validator."""

    def test_validate_battlefield(self):
        """
        Testing Battleship field validator.

        Testing a method that takes a field for well-known board game "Battleship"
        as an argument and returns true if it has a valid disposition of ships,
        false otherwise. Argument is guaranteed to be 10*10 two-dimension array.
        Elements in the array are numbers, 0 if the cell is free and 1 if occupied
        by ship.
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing validate_battlefield function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>"
            "Testing a method that takes a field for well-known"
            " board game \"Battleship\" as an argument and"
            " returns true if it has a valid disposition of"
            " ships, false otherwise.</p>")
        # pylint: enable-msg=R0801
        test_data: tuple = (
            ([[0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
              [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]],
             True, "Must return TRUE for valid field"),
            ([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
              [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
              [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
              [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
              [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 1, 0, 0, 0]],
             True, 'Must return TRUE for valid field'),
            ([[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
              [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
              [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
             True, 'Must return TRUE for valid field'),
            ([[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
              [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
              [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
             False, 'Must return FALSE if unwanted ships are present'),
            ([[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
              [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
              [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
             False, "Must return FALSE if number of ships of some type is incorrect"),
            ([[0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
             False, 'Must return FALSE if some of ships is missing'),
            ([[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
             False, 'Must return FALSE if some of ships has incorrect shape (non-straight)'),
            ([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
              [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
              [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
             False, 'Must return FALSE if the number and length of ships is not ok'),
            ([[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
              [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
              [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
             False, 'Must return FALSE if ships are in contact'))

        for field, expected, message in test_data:
            actual_result: bool = validate_battlefield(field)

            print_log(field=field,
                      expected=expected,
                      message=message,
                      actual_result=actual_result)

            step_txt: str = (f"Field validation: expected -> {expected}, "
                             f"actual -> {actual_result}")

            with allure.step(step_txt):
                self.assertEqual(expected, actual_result, msg=message)
