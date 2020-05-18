#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS CLASSES BASIC LANGUAGE FEATURES OBJECT-ORIENTED PROGRAMMING
# FUNDAMENTALS RULES

import allure
import unittest
from utils.log_func import print_log
from kyu_4.the_greatest_warrior.warrior import Warrior


@allure.epic('4 kyu')
@allure.parent_suite('Competent')
@allure.suite('OOP')
@allure.sub_suite("Unit Tests")
@allure.feature('Classes')
@allure.story('The Greatest Warrior')
@allure.tag('ALGORITHMS', 'CLASSES', 'BASIC LANGUAGE FEATURES',
            'OBJECT-ORIENTED PROGRAMMING', 'FUNDAMENTALS', 'RULES')
@allure.link(
    url='https://www.codewars.com/kata/5941c545f5c394fef900000c/train/python',
    name='Source/Kata')
class BattleTestCase(unittest.TestCase):
    """
    Testing Battle method
    """

    def test_battle(self):
        """
        Testing Battle method
        """

        allure.dynamic.title("Testing Battle method")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing Battle method</p>")

        with allure.step("If a warrior level 1 fights an enemy level 1, "
                         "they will receive 10 experience points."):
            warrior_1 = Warrior()
            experience = warrior_1.experience
            warrior_1.battle(1)
            self.assertEqual(10, warrior_1.experience - experience)

        with allure.step("If a warrior level 1 fights an enemy level 3, "
                         "they will receive 80 experience points."):
            warrior_2 = Warrior()
            experience = warrior_2.experience
            warrior_2.battle(3)
            self.assertEqual(80, warrior_2.experience - experience)
