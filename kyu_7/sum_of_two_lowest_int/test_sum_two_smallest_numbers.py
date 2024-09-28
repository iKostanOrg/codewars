"""
Test for -> Sum of two lowest positive integers
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

import unittest
import allure
from kyu_7.sum_of_two_lowest_int.sum_two_smallest_int import sum_two_smallest_numbers

# FUNDAMENTALS, ARRAYS


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Sum of two lowest positive integers')
@allure.tag('FUNDAMENTALS',
            'ARRAYS')
@allure.link(
    url='https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python',
    name='Source/Kata')
class SumTwoSmallestNumbersTestCase(unittest.TestCase):
    """
    Testing sum_two_smallest_numbers function
    """

    def test_sum_two_smallest_numbers(self):
        """
        Test sum_two_smallest_numbers function
        The function should return the sum of
        the two lowest positive numbers
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title(
            "Two smallest numbers in the start of the list")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Simple test"):
            self.assertEqual(
                sum_two_smallest_numbers([5, 8, 12, 18, 22]),
                13)

        with allure.step("Two smallest numbers in the start/middle of the list"):
            self.assertEqual(
                sum_two_smallest_numbers([7, 15, 12, 18, 22]),
                19)

        with allure.step("Two smallest numbers in the middle of the list"):
            self.assertEqual(
                sum_two_smallest_numbers([25, 42, 12, 18, 22]),
                30)
