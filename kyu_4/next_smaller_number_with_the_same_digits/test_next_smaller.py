"""
Test for -> Next smaller number with the same digits
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS NUMBERS STRINGS INTEGERS MATHEMATICS

import unittest
import allure
from utils.log_func import print_log
from kyu_4.next_smaller_number_with_the_same_digits.next_smaller \
    import next_smaller


# pylint: disable-msg=R0801
@allure.epic("4 kyu")
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story("Next smaller number with the same digits")
@allure.tag('ALGORITHMS',
            'NUMBERS',
            'STRINGS',
            'INTEGERS',
            'MATHEMATICS')
@allure.link(url='https://www.codewars.com/kata/5659c6d896bc135c4c00021e',
             name='Source/Kata')
# pylint: enable-msg=R0801
class NextSmallerTestCase(unittest.TestCase):
    """
    Testing next_smaller function
    """

    def test_next_smaller(self):
        """
        Testing next_smaller function

        You have to test a function that takes a positive integer number
        and returns the next smaller number formed by the same digits:

        21 ==> 12
        531 ==> 513
        2071 ==> 2017

        If no smaller number can be composed using those digits, return -1
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing next_smaller function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing next_bigger function</p>"
            "<p>You have to test a function that takes a positive integer "
            "number and returns the next smaller number formed by the same"
            " digits:</p>"
            "<p>21 ==> 12</p>"
            "<p>531 ==> 513</p>"
            "<p>2071 ==> 2017</p>"
            "<p>If no smaller number can be composed using those digits,"
            " return -1</p>")
        # pylint: enable-msg=R0801
        test_data: tuple = (
            (1027, -1),
            (1262347, 1247632),
            (907, 790),
            (531, 513),
            (135, -1),
            (2071, 2017),
            (414, 144),
            (123456798, 123456789),
            (123456789, -1),
            (1234567908, 1234567890))

        for n, expected in test_data:
            actual_result = next_smaller(n)
            print_log(n=n,
                      expected=expected,
                      actual_result=actual_result)

            with allure.step(f"Enter an integer ({n}), "
                             f"calculate the result ({actual_result}) and "
                             f"compare it with expected ({expected})"):
                self.assertEqual(expected, actual_result)
