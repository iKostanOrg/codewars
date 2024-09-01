"""
Solution for -> Formatting decimal places #1
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS FORMATTING ALGORITHMS NUMBERS

import unittest
import allure
from utils.log_func import print_log
from kyu_7.formatting_decimal_places_1.two_decimal_places import two_decimal_places


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Formatting")
@allure.story('Formatting decimal places #1')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class TwoDecimalPlacesTestCase(unittest.TestCase):
    """
    Testing two_decimal_places function
    """

    def test_two_decimal_places(self):
        """
        Testing two_decimal_places function
        with various test inputs

        Each floating-point number should be
        formatted that only the first two
        decimal places are returned.

        You don't need to check whether the input
        is a valid number because only valid numbers
        are used in the tests.

        Don't round the numbers! Just cut them
        after two decimal places!

        :return:
        """

        allure.dynamic.title("Testing two_decimal_places function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Pass a number and verify the output"):

            test_data = [
                (10.1289767789, 10.12,
                 "didn't work for 10.1289767789"),
                (-7488.83485834983, -7488.83,
                 "didn't work for -7488.83485834983"),
                (4.653725356, 4.65,
                 "didn't work for 4.653725356"),
            ]

            for number, expected, msg in test_data:

                print_log(number=number,
                          expected=expected)

                self.assertEqual(expected,
                                 two_decimal_places(number),
                                 msg)
