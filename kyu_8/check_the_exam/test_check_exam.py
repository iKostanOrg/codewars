"""
Test for -> Check the exam.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS ARRAYS NUMBERS BASIC LANGUAGE FEATURES

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_8.check_the_exam.check_exam import check_exam


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Check the exam')
@allure.tag('FUNDAMENTALS',
            'ARRAYS',
            'NUMBERS',
            'BASIC LANGUAGE FEATURES')
@allure.link(
    url='https://www.codewars.com/kata/5a3dd29055519e23ec000074',
    name='Source/Kata')
# pylint: enable=R0801
class CheckExamTestCase(unittest.TestCase):
    """Testing check_exam function."""

    @parameterized.expand([
        (["a", "a", "b", "b"], ["a", "c", "b", "d"], 6),
        (["a", "a", "c", "b"], ["a", "a", "b", ""], 7),
        (["a", "a", "b", "c"], ["a", "a", "b", "c"], 16),
        (["b", "c", "b", "a"], ["", "a", "a", "c"], 0)])
    def test_check_exam(self, arr1, arr2, expected):
        """
        Testing check_exam function with various test data.

        The function should return the score for this
        array of answers, giving +4 for each correct answer,
        -1 for each incorrect answer, and +0 for each blank
        answer(empty string).
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing check_exam function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="'
            'https://www.codewars.com/users/myFirstCode/badges/large'
            '">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable=R0801
        with allure.step("Enter arr1 and arr2 and verify the output"):
            print_log(arr1=arr1, arr2=arr2, expected=expected)
            self.assertEqual(expected, check_exam(arr1, arr2))
