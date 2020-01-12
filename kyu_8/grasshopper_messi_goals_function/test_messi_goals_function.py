#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

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
@allure.tag()
@allure.link(url='',
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

        with allure.step("Test with all zeroes"):
            la_liga = 0
            copa_del_rey = 0
            champions = 0
            expected = 0

            print_log(la_liga=la_liga,
                      copa_del_rey=copa_del_rey,
                      champions=champions,
                      expected=expected)

        self.assertEqual(goals(la_liga, copa_del_rey, champions),
                         expected)

        with allure.step("Test with positive integers"):
            la_liga = 5
            copa_del_rey = 10
            champions = 2
            expected = 17

            print_log(la_liga=la_liga,
                      copa_del_rey=copa_del_rey,
                      champions=champions,
                      expected=expected)

        self.assertEqual(goals(la_liga, copa_del_rey, champions),
                         expected)
