"""
Test for -> You\'re a square
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS, MATH

import unittest
import allure
from kyu_7.you_are_square.you_are_square import is_square


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Math")
@allure.sub_suite("Unit Tests")
@allure.feature("Square Calculation")
@allure.story('You\'re a square')
@allure.tag('FUNDAMENTALS',
            'MATH')
@allure.link(
    url='https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python',
    name='Source/Kata')
class YouAreSquareTestCase(unittest.TestCase):
    """
    Testing is_square function

    The tests will always use some integral number,
    so don't worry about that in dynamic typed languages.
    """

    def test_is_square_negative_numbers(self):
        """
        -1: Negative numbers cannot be square numbers
        :return:
        """
        allure.dynamic.title("Negative numbers")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")

        with allure.step("Test -1"):
            self.assertEqual(is_square(-1),
                             False,
                             "-1: Negative numbers cannot be square numbers")

    def test_is_square_zero(self):
        """
        0 is a square number
        :return:
        """
        allure.dynamic.title("Zero")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")

        with allure.step("0 is a square number"):
            self.assertEqual(is_square(0),
                             True,
                             "0 is a square number")

    def test_is_square_negative_test(self):
        """
        3 is not a square number
        :return:
        """
        allure.dynamic.title("Non square numbers (negative)")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")

        with allure.step("Test non square number: 3"):
            self.assertEqual(is_square(3),
                             False,
                             "3 is not a square number")

    def test_is_square_four(self):
        """
        4 is a square number
        :return:
        """
        allure.dynamic.title("Square numbers (positive)")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")

        with allure.step("Test square number: 4"):
            self.assertEqual(is_square(4),
                             True,
                             "4 is a square number")

    def test_is_square_25(self):
        """
        25 is a square number
        :return:
        """
        allure.dynamic.title("Square numbers (positive)")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")

        with allure.step("Test square number: 25"):
            self.assertEqual(is_square(25),
                             True,
                             "25 is a square number")

    def test_is_square_26(self):
        """
        26 is not a square number
        :return:
        """
        allure.dynamic.title("Non square numbers (negative)")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")

        with allure.step("Test non square number: 26"):
            self.assertEqual(is_square(26),
                             False,
                             "26 is not a square number")
