"""
Test for -> Next bigger number with the same digits

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# REFACTORING NUMBERS STRINGS INTEGERS

import unittest
import allure
from utils.log_func import print_log
from kyu_4.next_bigger_number_with_the_same_digits.next_bigger import next_bigger


@allure.epic("4 kyu")
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story("Next bigger number with the same digits")
@allure.tag('ALGORITHMS',
            'NUMBERS',
            'STRINGS',
            'INTEGERS',
            'MATHEMATICS')
@allure.link(url='https://www.codewars.com/kata/55983863da40caa2c900004e/train/python',
             name='Source/Kata')
class NextBiggerTestCase(unittest.TestCase):

    def test_next_bigger(self):
        """
        Testing next_bigger function

        You have to test a function that takes a positive integer
        number and returns the next bigger number formed by the same digits:

        12 ==> 21
        513 ==> 531
        2017 ==> 2071

        If no bigger number can be composed using those digits, return -1
        """

        allure.dynamic.title("Testing next_bigger function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing next_bigger function</p>"
            "<p>You have to test a function that takes"
            " a positive integer number and returns "
            "the next bigger number formed by the same "
            "digits:</p>"
            "<p>12 ==> 21</p>"
            "<p>513 ==> 531</p>"
            "<p>2017 ==> 2071</p>"
            "<p>If no bigger number can be composed using"
            " those digits, return -1</p>")

        test_data = [
            (6, -1),
            (12, 21),
            (513, 531),
            (2017, 2071),
            (414, 441),
            (144, 414),
            (6938652, 6952368),
            (123456789, 123456798)
        ]

        for n, expected in test_data:
            actual_result = next_bigger(n)
            print_log(n=n,
                      expected=expected,
                      actual_result=actual_result)

            with allure.step(f"Enter an integer ({n}), "
                             f"generate the result ({actual_result}) and "
                             f"compare it with expected ({expected})"):
                self.assertEqual(expected, actual_result)
