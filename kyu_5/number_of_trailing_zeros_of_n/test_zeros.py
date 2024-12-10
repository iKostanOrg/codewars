"""
Test for -> Number of trailing zeros of N!.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS MATHEMATICS NUMBERS

import unittest
import allure
from kyu_5.number_of_trailing_zeros_of_n.zeros import zeros
from utils.log_func import print_log


# pylint: disable-msg=R0801
@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Math")
@allure.story('Number of trailing zeros of N!')
@allure.tag('ALGORITHMS',
            'MATHEMATICS',
            'NUMBERS')
@allure.link(
    url='https://www.codewars.com/kata/52f787eb172a8b4ae1000a34',
    name='Source/Kata')
# pylint: enable-msg=R0801
class ZerosTestCase(unittest.TestCase):
    """Testing zeros function."""

    def test_zeros(self):
        """
        Testing zeros function with various test data.

        Testing 'zeros' program that should calculate the number
        of trailing zeros in a factorial of a given number.
        :return: None
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing zeros function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Enter test number and verify the result"):
            test_data: tuple = (
                (0, 0, "Testing with n = 0"),
                (6, 1, "Testing with n = 6"),
                (10, 2, "Testing with n = 10"),
                (12, 2, "Testing with n = 12"),
                (30, 7, "Testing with n = 30"))

            for data in test_data:

                number: int = data[0]
                expected: int = data[1]
                message: str = data[2]

                print_log(message=message,
                          number=number,
                          expected=expected)

                self.assertEqual(expected,
                                 zeros(number))
