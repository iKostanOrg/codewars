"""
Test for -> Fibonacci Streaming.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS

import unittest
import itertools
import allure
from utils.log_func import print_log
from kyu_5.fibonacci_streaming.all_fibonacci_numbers \
    import all_fibonacci_numbers


# pylint: disable-msg=R0801
@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Fibonacci Streaming')
@allure.tag('ALGORITHMS')
@allure.link(
    url='https://www.codewars.com/kata/55695bc4f75bbaea5100016b',
    name='Source/Kata')
# pylint: enable-msg=R0801
class AllFibonacciNumbersTestCase(unittest.TestCase):
    """Testing all_fibonacci_numbers function."""

    def test_all_fibonacci_numbers(self):
        """
        Testing all_fibonacci_numbers function.

        You're going to provide a needy programmer a
        utility method that generates an infinite sized,
        sequential IntStream (in Python generator)
        which contains all the numbers in a fibonacci
        sequence.

        A fibonacci sequence starts with two 1s.
        Every element afterwards is the sum of
        the two previous elements.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing all_fibonacci_numbers function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Run all_fibonacci_numbers function"
                         " and verify the result"):
            expected: list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
                              233, 377, 610, 987, 1597, 2584, 4181, 6765,
                              10946, 17711, 28657, 46368, 75025, 121393,
                              196418, 317811, 514229, 832040]
            result = list(itertools.islice(all_fibonacci_numbers(),30))
            print_log(result=result, expected=expected)
            self.assertEqual(expected, result)
