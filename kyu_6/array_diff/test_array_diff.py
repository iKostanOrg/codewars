"""
Test for -> Array.diff.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS ARRAYS

import unittest
import allure
from parameterized import parameterized
from kyu_6.array_diff.solution import array_diff
from utils.log_func import print_log


# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature('Lists')
@allure.story('Array.diff')
@allure.tag('FUNDAMENTALS',
            'ARRAYS',
            'LISTS')
@allure.link(
    url='https://www.codewars.com/kata/523f5d21c841566fde000009',
    name='Source/Kata')
# pylint: enable-msg=R0801
class ArrayDiffTestCase(unittest.TestCase):
    """
    Testing array_diff function.

    Your goal in this kata is to implement a difference function,
    which subtracts one list from another and returns the result.

    It should remove all values from list a, which are present
    in list b:
    array_diff([1,2],[1]) == [2]

    If a value is present in b, all of its occurrences must be
    removed from the other:
    array_diff([1,2,2,2,3],[2]) == [1,3]
    """

    @parameterized.expand([
        ([1, 2], [1], [2], "a was [1,2], b was [1], expected [2]"),
        ([1, 2, 2], [1], [2, 2], "a was [1,2,2], b was [1], expected [2,2]"),
        ([1, 2, 2], [2], [1], "a was [1,2,2], b was [2], expected [1]"),
        ([1, 2, 2], [], [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]"),
        ([], [1, 2], [], "a was [], b was [1,2], expected []")])
    def test_array_diff_function(self, a, b, expected, message):
        """
        Testing array_diff function.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing array_diff function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Test that function subtracts one list from another"
            "and returns the result. It should remove all values from "
            "list a, which are present in list b.</p>")
        # pylint: enable-msg=R0801
        with allure.step(f"Enter a test data: {a, b} and verify the "
                         f"expected output vs actual result: {expected}."):
            actual_result: list = array_diff(a, b)
            print_log(a=a,
                      b=b,
                      exp=expected,
                      message=message,
                      actual_result=actual_result)

            self.assertEqual(expected,
                             actual_result,
                             message)
