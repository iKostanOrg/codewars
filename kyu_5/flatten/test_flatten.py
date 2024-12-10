"""
Solution for -> flatten().

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS ARRAYS

import unittest
import allure
from kyu_5.flatten.flatten import flatten
from utils.log_func import print_log


# pylint: disable-msg=R0801
@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('flatten()')
@allure.tag('ALGORITHMS',
            'ARRAYS')
@allure.link(
    url='https://www.codewars.com/kata/513fa1d75e4297ba38000003',
    name='Source/Kata')
# pylint: enable-msg=R0801
class FlattenTestCase(unittest.TestCase):
    """Testing flatten function."""

    def test_flatten(self):
        """
        Testing flatten function with various test data.

        For this exercise you will create a global flatten method.
        The method takes in any number of arguments and flattens
        them into a single array. If any of the arguments passed in
        are an array then the individual objects within the array
        will be flattened so that they exist at the same level as
        the other arguments. Any nested arrays, no matter how deep,
        should be flattened into the single array result.

        The following are examples of how this function would be
        used and what the expected results would be:

        flatten(1, [2, 3], 4, 5, [6, [7]]) # returns [1, 2, 3, 4, 5, 6, 7]
        flatten('a', ['b', 2], 3, None, [[4], ['c']]) # returns
        ['a', 'b', 2, 3, None, 4, 'c']
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing flatten function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Enter test data #1 and verify the output"):
            expected: list = []
            print_log(args=None,
                      expected=expected)
            self.assertListEqual(expected,
                                 flatten())

        with allure.step("Enter test data #2 and verify the output"):
            expected = [1, 2, 3]
            print_log(args=(1, 2, 3),
                      expected=expected)
            self.assertListEqual(expected,
                                 flatten(1, 2, 3))

        with allure.step("Enter test data #3 and verify the output"):
            expected = [1, 2, 3, 4, 5, 6, 7, 8]
            print_log(args=([1, 2], [3, 4, 5], [6, [7], [[8]]]),
                      expected=expected)
            self.assertListEqual(expected,
                                 flatten([1, 2], [3, 4, 5], [6, [7], [[8]]]))

        with allure.step("Enter test data #4 and verify the output"):
            expected = [1, 2, '9', None]
            print_log(args=(1, 2, ['9', [], []], None),
                      expected=expected)
            self.assertListEqual(expected,
                                 flatten(1, 2, ['9', [], []], None))

        with allure.step("Enter test data #5 and verify the output"):
            expected = ['hello', 2, 'text', 4, 5, '[list]']
            print_log(args=(['hello', 2, ['text', [4, 5]]], [[]], '[list]'), expected=expected)
            self.assertListEqual(expected, flatten(['hello', 2, ['text', [4, 5]]], [[]], '[list]'))
