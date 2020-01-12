#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# BUGS ARRAYS FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.swap_values.swap_values import swap_values


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Swap Values')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class SwapValuesTestCase(unittest.TestCase):
    """
    Testing swap_values function
    """
    def test_swap_values(self):
        """
        Testing swap_values function
        """

        allure.dynamic.title("Testing swap_values function")
        allure.dynamic.severity(allure.severity_level.CRITICAL)

        with allure.step("Pass a list with 2 values and swap them"):

            swap = [1, 2]
            expected = [2, 1]
            swap_values(swap)

            print_log(list=swap, expected=expected)

            self.assertEqual(swap[0], 2)
            self.assertEqual(swap[1], 1)
