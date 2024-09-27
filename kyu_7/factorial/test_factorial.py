"""
Test for -> Sum of Numbers
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS ALGORITHMS NUMBERS

import unittest
import allure
from utils.log_func import print_log
from kyu_7.factorial.factorial import factorial


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Addition")
@allure.story('Sum of Numbers')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class FactorialTestCase(unittest.TestCase):
    """
    Testing 'factorial' function
    """

    def test_factorial(self):
        """
        Testing 'factorial' function

        In mathematics, the factorial of a non-negative integer n,
        denoted by n!, is the product of all positive integers less
        than or equal to n. For example: 5! = 5 * 4 * 3 * 2 * 1 = 120.
        By convention the value of 0! is 1.

        Write a function to calculate factorial for a given input.
        If input is below 0 or above 12 throw an exception of type
        ValueError (Python).
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'factorial' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Enter a number and verify the output"):
            data: tuple = (
                (0, 1, "factorial for 0 is 1"),
                (1, 1, "factorial for 1 is 1"),
                (2, 2, "factorial for 2 is 2"),
                (3, 6, "factorial for 3 is 6"))

            for n, expected, msg in data:

                print_log(n=n,
                          expected=expected,
                          msg=msg)

                self.assertEqual(expected,
                                 factorial(n),
                                 msg)
