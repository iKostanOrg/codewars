#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS ALGORITHMS MATHEMATICS NUMBERS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.keep_hydrated.keep_hydrated import litres


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Math")
@allure.sub_suite("Unit Tests")
@allure.feature("Calculation")
@allure.story('Keep Hydrated!')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class KeepHydratedTestCase(unittest.TestCase):
    """
    Testing litres function
    """

    def test_keep_hydrated(self):
        """
        Testing litres function with various test inputs
        :return:
        """

        allure.dynamic.title("Testing litres function with various test inputs")
        allure.dynamic.severity(allure.severity_level.CRITICAL)

        with allure.step("Enter hours and verify the output"):

            data = [
                (2, 1, 'should return 1 litre'),
                (1.4, 0, 'should return 0 litres'),
                (12.3, 6, 'should return 6 litres'),
                (0.82, 0, 'should return 0 litres'),
                (11.8, 5, 'should return 5 litres'),
                (1787, 893, 'should return 893 litres'),
                (0, 0, 'should return 0 litres')
            ]

            for hours, expected, message in data:
                print_log(hours=hours, expected=expected)
                self.assertEqual(expected, litres(hours), message)
