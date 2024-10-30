"""
Test for -> Sort the odd
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS ARRAYS

import unittest
import allure
from kyu_6.sort_the_odd.solution import sort_array
from utils.log_func import print_log


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Sort the odd')
@allure.tag('FUNDAMENTALS',
            'ARRAYS')
@allure.link(
    url='https://www.codewars.com/kata/578aa45ee9fd15ff4600090d',
    name='Source/Kata')
class SortArrayTestCase(unittest.TestCase):
    """
    Testing 'sort_array' function
    """
    def test_sort_array(self):
        """
        The 'sort_array' function.

        The task is to sort ascending odd numbers but
        even numbers must be on their places.

        Zero isn't an odd number and you don't need to
        move it. If you have an empty array, you need
        to return it.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title(
            "Testing the 'sort_array' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>The task is to sort ascending odd numbers but "
            "even numbers must be on their places.</p>")
        # pylint: enable-msg=R0801
        test_data: tuple = (
            ([5, 3, 2, 8, 1, 4], [1, 3, 2, 8, 5, 4]),
            ([5, 3, 1, 8, 0], [1, 3, 5, 8, 0]),
            ([], []))

        for source_array, expected in test_data:
            actual_result: list = sort_array(source_array)

            with allure.step(
                    "Enter a list and verify the expected "
                    "output vs actual result"):

                print_log(source_array=source_array,
                          expected=expected,
                          result=actual_result)

                self.assertListEqual(expected, actual_result)
