"""
Test for -> Pokemon Damage Calculator
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# PUZZLES ARRAYS GAMES STRINGS NUMBERS FUNCTIONS
# CONTROL FLOW BASIC LANGUAGE FEATURES FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_6.pokemon_damage_calculator.calculate_damage import calculate_damage


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Games")
@allure.sub_suite("Unit Tests")
@allure.feature("Numbers")
@allure.story('Pokemon Damage Calculator')
@allure.tag('PUZZLES',
            'ARRAYS',
            'GAMES',
            'STRINGS',
            'NUMBERS',
            'FUNCTIONS',
            'CONTROL FLOW',
            'BASIC LANGUAGE FEATURES',
            'FUNDAMENTALS')
@allure.link(
    url='https://www.codewars.com/kata/536e9a7973130a06eb000e9f/train/python',
    name='Source/Kata')
class CalculateDamageTestCase(unittest.TestCase):
    """
    Testing calculate_damage function:
    damage = 50 * (attack / defense) * effectiveness
    """
    def test_calculate_damage(self):
        """
        Testing calculate_damage with various test data
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing calculate_damage function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Verify that the function calculates the damage "
            "that a particular move would do using the following"
            " formula (not the actual one from the game): "
            "damage = 50 * (attack / defense) * effectiveness</p>")
        # pylint: enable-msg=R0801
        test_data = [
            (("fire", "water", 100, 100), 25),
            (("grass", "water", 100, 100), 100),
            (("electric", "fire", 100, 100), 50),
            (("grass", "electric", 57, 19), 150),
            (("grass", "water", 40, 40), 100),
            (("grass", "fire", 35, 5), 175),
            (("fire", "electric", 10, 2), 250),
        ]

        for test_data, expected in test_data:
            your_type = test_data[0]
            opponent_type = test_data[1]
            attack = test_data[2]
            defense = test_data[3]
            actual_result = calculate_damage(
                your_type,
                opponent_type,
                attack,
                defense)

            with allure.step(f"Enter a test data ({test_data}) and verify the "
                             f"expected output ({expected}) vs "
                             f"actual result ({actual_result})"):

                print_log(test_data=test_data,
                          expected=expected,
                          result=actual_result)

                self.assertEqual(expected,
                                 actual_result)
