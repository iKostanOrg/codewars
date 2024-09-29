"""
Test for -> Sum of Digits / Digital Root
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS MATHEMATICS NUMBERS ARITHMETIC

import unittest
import allure
from utils.log_func import print_log
from kyu_6.sum_of_digits_digital_root.digital_root import digital_root


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Math")
@allure.story('Sum of Digits / Digital Root')
@allure.tag('ALGORITHMS',
            'MATHEMATICS',
            'NUMBERS',
            'ARITHMETIC')
@allure.link(
    url='https://www.codewars.com/kata/541c8630095125aba6000c00/train/python',
    name='Source/Kata')
class DigitalRootTestCase(unittest.TestCase):
    """
    Testing digital_root function
    """
    def test_digital_root(self):
        """
        In this kata, you must create a digital root function.

        A digital root is the recursive sum of all the digits
        in a number. Given n, take the sum of the digits of n.
        If that value has more than one digit, continue reducing
        in this way until a single-digit number is produced. This
        is only applicable to the natural numbers.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing digital_root function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Enter a number and verify the output"):
            test_data = [
                (16, 7),
                (456, 6),
                (942, 6),
                (132189, 6),
                (493193, 2)]

            for n, expected in test_data:
                print_log(n=n, expected=expected)
                self.assertEqual(expected, digital_root(n))
