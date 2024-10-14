"""
Test for -> Greek Sort
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS

import unittest
import allure
from kyu_8.greek_sort.greek_comparator import greek_comparator
from utils.log_func import print_log


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Tuple")
@allure.story('Greek Sort')
@allure.tag('FUNDAMENTALS')
@allure.link(
    url='https://www.codewars.com/kata/56bc1acf66a2abc891000561',
    name='Source/Kata')
class GreekComparatorTestCase(unittest.TestCase):
    """
    Testing greek_comparator function
    """

    def test_greek_comparator(self):
        """
        Testing greek_comparator function
        with various test inputs
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing 'greek_comparator' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>A custom comparison function of two arguments (iterable elements) "
            "which should return a negative, zero or positive number depending on "
            "whether the first argument is considered smaller than, equal to, or "
            "larger than the second argument</p>")
        # pylint: enable=R0801
        test_data: tuple = (
            ('alpha', 'beta', '< 0'),
            ('psi', 'psi', '== 0'),
            ('upsilon', 'rho', '> 0'))

        for d in test_data:
            lhs, rhs, expected = d[0], d[1], d[2]
            result = greek_comparator(lhs, rhs)

            with allure.step(f"Enter test inputs({lhs}, {rhs}) "
                             f"and assert expected ({expected}) "
                             f"vs actual result ({result})"):

                expression: str = f'{result} {expected}'

                print_log(lhs=lhs,
                          rhs=rhs,
                          expected=expected,
                          result=result,
                          expression=expression)

                self.assertTrue(eval(expression))
