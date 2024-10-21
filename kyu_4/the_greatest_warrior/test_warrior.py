"""
Test for -> The Greatest Warrior -> test warrior
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS CLASSES BASIC LANGUAGE FEATURES
# OBJECT-ORIENTED PROGRAMMING FUNDAMENTALS RULES

import unittest
import allure
from utils.log_func import print_log
from kyu_4.the_greatest_warrior.warrior import Warrior


# pylint: disable-msg=R0801
@allure.epic('4 kyu')
@allure.parent_suite('Competent')
@allure.suite('OOP')
@allure.sub_suite("Unit Tests")
@allure.feature('Classes')
@allure.story('The Greatest Warrior')
@allure.tag('ALGORITHMS',
            'CLASSES',
            'BASIC LANGUAGE FEATURES',
            'OBJECT-ORIENTED PROGRAMMING',
            'FUNDAMENTALS',
            'RULES')
@allure.link(
    url='https://www.codewars.com/kata/5941c545f5c394fef900000c',
    name='Source/Kata')
# pylint: enable-msg=R0801
class WarriorTestCase(unittest.TestCase):
    """
    Testing Warrior class
    """

    def test_warrior_tom(self):
        """
        Testing Warrior class >>> tom
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing Warrior class >>> tom")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Basic test: level, experience, rank</p>")
        # pylint: enable=R0801
        with allure.step("Instantiate a new warrior >>> tom"):
            tom = Warrior()

        with allure.step("Assert level"):
            print_log(level=tom.level)
            self.assertEqual(tom.level, 1)

        with allure.step("Assert experience"):
            print_log(experience=tom.experience)
            self.assertEqual(tom.experience, 100)

        with allure.step("Assert rank"):
            print_log(rank=tom.rank)
            self.assertEqual(tom.rank, "Pushover")

    def test_warrior_bruce_lee(self):
        """
        Testing Warrior class >>> bruce_lee
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing Warrior class >>> bruce_lee")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Advanced Warrior class assertions</p>")
        # pylint: enable=R0801
        with allure.step("Instantiate a new warrior >>> bruce_lee"):
            bruce_lee = Warrior()

        with allure.step("Assert level"):
            print_log(level=bruce_lee.level)
            self.assertEqual(bruce_lee.level, 1)

        with allure.step("Assert experience"):
            print_log(experience=bruce_lee.experience)
            self.assertEqual(bruce_lee.experience, 100)

        with allure.step("Assert rank"):
            print_log(rank=bruce_lee.rank)
            self.assertEqual(bruce_lee.rank, "Pushover")

        with allure.step("Assert achievements"):
            self.assertListEqual(bruce_lee.achievements, [])

        with allure.step("Assert training"):
            self.assertEqual(bruce_lee.training(
                ["Defeated Chuck Norris", 9000, 1]), "Defeated Chuck Norris")

        with allure.step("Assert experience"):
            self.assertEqual(bruce_lee.experience, 9100)

        with allure.step("Assert level"):
            self.assertEqual(91, bruce_lee.level)

        with allure.step("Assert rank"):
            self.assertEqual(bruce_lee.rank, "Master")

        with allure.step("Assert battle"):
            self.assertEqual(bruce_lee.battle(90), "A good fight")

        with allure.step("Assert experience"):
            self.assertEqual(bruce_lee.experience, 9105)

        with allure.step("Assert achievements"):
            self.assertEqual(bruce_lee.achievements, ["Defeated Chuck Norris"])
