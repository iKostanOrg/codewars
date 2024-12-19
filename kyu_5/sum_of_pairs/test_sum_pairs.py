"""
Test for -> Sum of Pairs.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS PARSING ALGORITHMS STRINGS MEMOIZATION
# DESIGN PATTERNS DESIGN PRINCIPLES

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_5.sum_of_pairs.sum_pairs import sum_pairs


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite('Algorithms')
@allure.sub_suite("Unit Tests")
@allure.feature('Memoization')
@allure.story('Sum of Pairs')
@allure.tag('FUNDAMENTALS',
            'PARSING ALGORITHMS',
            'STRINGS',
            'MEMOIZATION',
            'DESIGN PATTERNS',
            'DESIGN PRINCIPLES')
@allure.link(
    url='https://www.codewars.com/kata/54d81488b981293527000c8f',
    name='Source/Kata')
class SumPairsTestCase(unittest.TestCase):
    """Testing 'sum_pairs' function."""

    @parameterized.expand([
        ([1, 4, 8, 7, 3, 15], 8, [1, 7],
         "should return [1, 7] for sum = 8"),
        ([1, -2, 3, 0, -6, 1], -6, [0, -6],
         "should return [0, -6] for sum = -6"),
        ([20, -13, 40], -7, None,
         "should return None for sum = -7"),
        ([1, 2, 3, 4, 1, 0], 2, [1, 1],
         "should return [1, 1] for sum = 2"),
        ([10, 5, 2, 3, 7, 5], 10, [3, 7],
         "should return [3, 7] for sum = 10"),
        ([4, -2, 3, 3, 4], 8, [4, 4],
         "should return [4, 4] for sum = 8"),
        ([0, 2, 0], 0, [0, 0],
         "should return [0, 0] for sum = 0"),
        ([5, 9, 13, -3], 10, [13, -3],
         "should return [13, -3] for sum = 10")])
    def test_sum_pairs(self, ints, s, expected, message):
        """
        Testing 'sum_pairs' function.

        Given a list of integers and a single sum value,
        the function should return the first two values
        (parse from the left please) in order of appearance
        that add up to form the sum.
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing done_or_not function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p> Given a list of integers and a single sum value, "
            "the function should return the first two values (parse "
            "from the left please) in order of appearance that add up "
            "to form the sum.</p>")
        # pylint: enable-msg=R0801

        with allure.step(f"Enter a test list {ints}"
                         f"and verify the output {expected}."):
            result = sum_pairs(ints, s)
            print_log(ints=ints,
                      s=s,
                      message=message,
                      expected=expected,
                      result=result)
            self.assertEqual(expected, result)
