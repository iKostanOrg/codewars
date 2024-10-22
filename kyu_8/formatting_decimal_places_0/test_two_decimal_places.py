"""
Test for -> Formatting decimal places #0
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS FORMATTING ALGORITHMS NUMBERS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.formatting_decimal_places_0.two_decimal_places \
    import two_decimal_places


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Formatting")
@allure.story('Formatting decimal places #0')
@allure.tag('FUNDAMENTALS',
            'FORMATTING',
            'ALGORITHMS',
            'NUMBERS')
@allure.link(
    url='https://www.codewars.com/kata/5641a03210e973055a00000d',
    name='Source/Kata')
# pylint: enable=R0801
class TwoDecimalPlacesTestCase(unittest.TestCase):
    """
    Testing two_decimal_places function
    """

    def test_two_decimal_places(self):
        """
        Testing two_decimal_places function
        with various test inputs.

        Each number should be formatted that it is
        rounded to two decimal places. You don't
        need to check whether the input is a valid
        number because only valid numbers are used
        in the tests.
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing two_decimal_places function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable=R0801
        with allure.step("Pass a number and verify the output"):
            data: tuple = (
                (4.659725356,
                 4.66,
                 "didn't work for 4.659725356"),
                (173735326.3783732637948948,
                 173735326.38,
                 "didn't work for 173735326.3783732637948948"),
                (4.653725356,
                 4.65,
                 "didn't work for 4.653725356"))

            for n, expected, msg in data:
                print_log(n=n, expected=expected)
                self.assertEqual(expected,
                                 two_decimal_places(n),
                                 msg)
