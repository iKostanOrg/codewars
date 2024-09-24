"""
Test for -> Powers of 3
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS LOOPS CONTROL FLOW BASIC LANGUAGE FEATURES
# FUNDAMENTALS MATHEMATICS NUMBERS

import unittest
import allure
from utils.log_func import print_log
from kyu_7.powers_of_3.largest_power import largestPower


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Flow Control")
@allure.story('Powers of 3')
@allure.tag('ALGORITHMS',
            'LOOPS',
            'CONTROL FLOW',
            'BASIC LANGUAGE FEATURES',
            'FUNDAMENTALS',
            'MATHEMATICS',
            'NUMBERS')
@allure.link(
    url='https://www.codewars.com/kata/57be674b93687de78c0001d9/train/python',
    name='Source/Kata')
class LargestPowerTestCase(unittest.TestCase):
    """
    Testing largestPower function
    """

    def test_largest_power(self):
        """
        Testing largestPower function
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing largestPower function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Pass an integer and verify the output"):
            n: int = 3
            expected: int = 0
            print_log(N=n, expected=expected)
            self.assertEqual(largestPower(n), expected)

        with allure.step("Pass an integer and verify the output"):
            n: int = 4
            expected: int = 1
            print_log(N=n, expected=expected)
            self.assertEqual(largestPower(n), expected)
