"""
Test for -> Share prices
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS FORMATTING ARITHMETIC MATHEMATICS NUMBERS

import unittest
import allure
from utils.log_func import print_log
from kyu_7.share_prices.share_price import share_price


# pylint: disable-msg=R0801
@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Math")
@allure.story('Share prices')
@allure.tag('ALGORITHMS',
            'FORMATTING',
            'ARITHMETIC',
            'MATHEMATICS',
            'NUMBERS')
@allure.link(
    url='https://www.codewars.com/kata/5603a4dd3d96ef798f000068/train/python',
    name='Source/Kata')
# pylint: enable-msg=R0801
class SharePriceTestCase(unittest.TestCase):
    """
    Testing share_price function
    """

    def test_share_price(self):
        """
        Testing share_price function
        with multiple test inputs
        :return:
        """
        allure.dynamic.title("Testing share_price function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")

        with allure.step("Enter invested, changes "
                         "and verify the output"):
            test_data: tuple = (
                (100, [], '100.00'),
                (100, [-50, 50], '75.00'),
                (100, [-50, 100], '100.00'),
                (100, [-20, 30], '104.00'),
                (1000, [0, 2, 3, 6], '1113.64'))

            for invested, changes, expected in test_data:
                
                print_log(invested=invested,
                          changes=changes,
                          expected=False)

                self.assertEqual(expected,
                                 share_price(invested, changes))
