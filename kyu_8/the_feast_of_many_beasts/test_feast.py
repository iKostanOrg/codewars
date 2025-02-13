"""
Test for -> The Feast of Many Beasts.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS STRINGS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.the_feast_of_many_beasts.feast import feast


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('The Feast of Many Beasts')
@allure.tag('FUNDAMENTALS',
            'STRINGS')
@allure.link(
    url='https://www.codewars.com/kata/5aa736a455f906981800360d',
    name='Source/Kata')
# pylint: enable=R0801
class FeastTestCase(unittest.TestCase):
    """Testing 'feast' function."""

    def test_feast(self):
        """
        Testing 'feast' function with various test inputs.

        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing 'feast' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing a function feast that takes the animal's "
            "name and dish as arguments and returns true or "
            "false to indicate whether the beast is allowed "
            "to bring the dish to the feast.</p>"
            "<p>Assume that beast and dish are always lowercase strings, "
            "and that each has at least two letters. beast and dish "
            "may contain hyphens and spaces, but these will not appear "
            "at the beginning or end of the string. They will not "
            "contain numerals.</p>"
            "<p>There is just one rule: the dish must start and end with "
            "the same letters as the animal's name. For example, the "
            "great blue heron is bringing garlic naan and the chickadee "
            "is bringing chocolate cake.</p>")
        # pylint: enable=R0801
        with allure.step("Enter animal's name and dish "
                         "as arguments and assert the output"):
            data: tuple = (
                ("great blue heron", "garlic naan", True),
                ("chickadee", "chocolate cake", True),
                ("brown bear", "bear claw", False))

            for beast, dish, expected in data:
                print_log(beast=beast, dish=dish, expected=expected)
                self.assertEqual(expected, feast(beast, dish))
