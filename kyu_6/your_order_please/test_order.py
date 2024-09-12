"""
Test for -> Your order, please
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS STRINGS

import unittest
import allure
from utils.log_func import print_log
from kyu_6.your_order_please.order import order


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Your order, please')
@allure.tag('FUNDAMENTALS',
            'STRINGS')
@allure.link(
    url='https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python',
    name='Source/Kata')
class OrderTestCase(unittest.TestCase):
    """
    Testing 'order' function
    """

    def test_order(self):
        """
        Your task is to verify that 'order' function
        sorts a given string by following rules:

            1. Each word in the string will contain a single number.
               This number is the position the word should have in
               the result.

            2. Note: Numbers can be from 1 to 9. So 1 will be the
               first word (not 0).

            3. If the input string is empty, return an empty string.
               The words in the input String will only contain valid
               consecutive numbers.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'order' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3><p>Your task is to verify that \'order\' '
            'function sorts a given string by following rules:'
            '1. Each word in the string will contain a single number. '
            'This number is the position the word should have in the result.<br/>'
            '2. Note: Numbers can be from 1 to 9. So 1 will be the first word '
            '(not 0).<br/>'
            '3. If the input string is empty, return an empty string. '
            'The words in the input String will only contain valid consecutive '
            'numbers.</p>')
        # pylint: enable-msg=R0801
        test_data = (
            ("is2 Thi1s T4est 3a",
             "Thi1s is2 3a T4est"),
            ("4of Fo1r pe6ople g3ood th5e the2",
             "Fo1r the2 g3ood 4of th5e pe6ople"),
            ("", ""),
        )

        for (sentence, expected) in test_data:
            actual_result: str = order(sentence)

            with allure.step("Enter a string and verify the "
                             "expected output vs actual result"):

                print_log(sentence=sentence,
                          expected=expected,
                          result=actual_result)

                self.assertEqual(expected,
                                 actual_result)
