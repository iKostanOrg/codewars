#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS ARRAYS FUNDAMENTALS OPTIMIZATION

import unittest
import allure
from utils.log_func import print_log
from kyu_5.integers_recreation_one.solution import list_squared


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Optimization")
@allure.story('Integers: Recreation One')
@allure.tag('ALGORITHMS', 'ARRAYS', 'FUNDAMENTALS', 'OPTIMIZATION')
@allure.link(url='https://www.codewars.com/kata/55aa075506463dac6600010d/train/python',
             name='Source/Kata')
class ListSquaredTestCase(unittest.TestCase):
    """
    Integers: Recreation One

    Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors
    squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the
    squared divisors is 2500 which is 50 * 50, a square!

    Given two integers m, n (1 <= m <= n) we want to find all integers
    between m and n whose sum of squared divisors is itself a square.
    42 is such a number.

    The result should be an array of arrays or of tuples (in C an array of Pair)
    or a string, each sub-array having two elements, first the number whose squared
    divisors is a square and then the sum of the squared divisors.
    """

    def test_flatten(self):
        """
        Testing list_squared function

        :return:
        """

        allure.dynamic.title("Testing list_squared function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>Given two integers m, n (1 <= m <= n) we want to find "
                                        "all integers between m and n whose sum of squared divisors "
                                        "is itself a square.</p>")

        test_data = (
            (1, 250,
             [[1, 1], [42, 2500], [246, 84100]]),
            (42, 250,
             [[42, 2500], [246, 84100]]),
            (250, 500,
             [[287, 84100]]),
            (960, 5024,
             [[1434, 2856100], [1673, 2856100], [1880, 4884100], [4264, 24304900]]),
            (689, 5666,
             [[728, 722500], [1434, 2856100], [1673, 2856100], [1880, 4884100], [4264, 24304900]]),
            (257, 4195, [[287, 84100], [728, 722500], [1434, 2856100], [1673, 2856100], [1880, 4884100]])
        )

        for m, n, expected in test_data:
            with allure.step("Enter test data and verify the output..."):
                actual_result = list_squared(m, n)
                print_log(m=m, n=n, expected=expected, actual_result=actual_result)
                self.assertListEqual(expected, actual_result)
