"""
Test for -> Keep Hydrated!.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS ALGORITHMS MATHEMATICS NUMBERS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_8.keep_hydrated.keep_hydrated import litres


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Math")
@allure.sub_suite("Unit Tests")
@allure.feature("Calculation")
@allure.story('Keep Hydrated!')
@allure.tag('FUNDAMENTALS',
            'ALGORITHMS',
            'MATHEMATICS',
            'NUMBERS')
@allure.link(
    url='https://www.codewars.com/kata/582cb0224e56e068d800003c',
    name='Source/Kata')
# pylint: disable=R0801
class KeepHydratedTestCase(unittest.TestCase):
    """Testing litres function."""

    @parameterized.expand([
        (2, 1, 'should return 1 litre'),
        (1.4, 0, 'should return 0 litres'),
        (12.3, 6, 'should return 6 litres'),
        (0.82, 0, 'should return 0 litres'),
        (11.8, 5, 'should return 5 litres'),
        (1787, 893, 'should return 893 litres'),
        (0, 0, 'should return 0 litres')])
    def test_keep_hydrated(self, hours, expected, message):
        """
        Testing litres function with various test inputs.

        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing litres function with various test inputs")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>"
            "Because Nathan knows it is important to stay hydrated, "
            " he drinks 0.5 litres of water per hour of cycling."
            "</p>"
            "<p>"
            "You get given the time in hours and you need to return "
            "the number of litres Nathan will drink, rounded "
            "to the smallest value."
            "</p>")
        # pylint: enable=R0801
        with allure.step(f"Enter hours: {hours} "
                         f"and verify the expected output: {expected}."):
            print_log(hours=hours, expected=expected)
            self.assertEqual(expected, litres(hours), message)
