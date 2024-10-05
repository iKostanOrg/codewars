"""
Test for -> Messi goals function
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.grasshopper_messi_goals_function.messi_goals_function import goals


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Math")
@allure.sub_suite("Unit Tests")
@allure.feature("Addition")
@allure.story('Messi goals function')
@allure.tag('FUNDAMENTALS')
@allure.link(
    url='https://www.codewars.com/kata/55f73be6e12baaa5900000d4',
    name='Source/Kata')
class GoalsTestCase(unittest.TestCase):
    """
    Testing goals function
    """

    def test_goals(self):
        """
        Verify that the function returns Messi's
        total number of goals in all three leagues.
        :return:
        """
        allure.dynamic.title("goals function verification")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")

        with allure.step("Test with all zeroes"):
            la_liga: int = 0
            copa_del_rey: int = 0
            champions: int = 0
            expected: int = 0

            print_log(la_liga=la_liga,
                      copa_del_rey=copa_del_rey,
                      champions=champions,
                      expected=expected)

        self.assertEqual(goals(la_liga, copa_del_rey, champions),
                         expected)

        with allure.step("Test with positive integers"):
            la_liga: int = 5
            copa_del_rey: int = 10
            champions: int = 2
            expected: int = 17

            print_log(la_liga=la_liga,
                      copa_del_rey=copa_del_rey,
                      champions=champions,
                      expected=expected)

        self.assertEqual(goals(la_liga, copa_del_rey, champions),
                         expected)
