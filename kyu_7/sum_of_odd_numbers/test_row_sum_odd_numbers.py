"""
Test for -> Sum of odd numbers
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS ARRAYS LISTS DATA STRUCTURES
# NUMBERS ARITHMETIC MATHEMATICS ALGORITHMS

import unittest
import allure
from utils.log_func import print_log
from kyu_7.sum_of_odd_numbers.row_sum_odd_numbers import row_sum_odd_numbers


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature('Math')
@allure.story('Sum of odd numbers')
@allure.tag('FUNDAMENTALS',
            'ARRAYS',
            'LISTS',
            'DATA STRUCTURES',
            'NUMBERS',
            'ARITHMETIC',
            'MATHEMATICS',
            'ALGORITHMS')
@allure.link(
    url='https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python',
    name='Source/Kata')
class OddRowTestCase(unittest.TestCase):
    """
    Testing row_sum_odd_numbers function
    """

    def test_row_sum_odd_numbers(self):
        allure.dynamic.title("Testing row_sum_odd_numbers function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Given the triangle of consecutive odd numbers "
            "verify that the function calculates the row sums "
            "of this triangle from the row index (starting at index 1)</p>")

        test_data: tuple = (
            (1, 1),
            (2, 8),
            (13, 2197),
            (19, 6859),
            (41, 68921))

        for n, expected in test_data:
            actual_result: int = row_sum_odd_numbers(n)
            with allure.step(f"Enter the triangle's row ({n}) and verify the "
                             f"expected output ({expected}) "
                             f"vs actual result ({actual_result})"):

                print_log(n=n,
                          expected=expected,
                          result=actual_result)

                self.assertEqual(expected,
                                 actual_result)
