"""
Test for -> Logical Calculator
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS ARRAYS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.logical_calculator.logical_calculator \
    import logical_calc


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Logical Calculator')
@allure.tag('FUNDAMENTALS',
            'ARRAYS')
@allure.link(
    url='https://www.codewars.com/kata/57096af70dad013aa200007b',
    name='Source/Kata')
# pylint: enable=R0801
class LogicalCalculatorTestCase(unittest.TestCase):
    """
    Testing logical_calc function
    """

    def test_logical_calc_and(self):
        """
        And (∧) is the truth-functional
        operator of logical conjunction

        The and of a set of operands is true
        if and only if all of its operands are true.

        Source:
        https://en.wikipedia.org/wiki/Logical_conjunction

        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("AND logical operator")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable=R0801
        with allure.step("Pass an array with 2 members (negative)"):
            lst: list = [True, False]
            operator: str = 'AND'
            expected: bool = False
            print_log(list=lst, operator=operator, expected=expected)
            self.assertEqual(logical_calc(lst, operator), expected)

        with allure.step("Pass an array with 3 members (negative)"):
            lst: list = [True, True, False]
            operator: str = 'AND'
            expected: bool = False
            print_log(list=lst, operator=operator, expected=expected)
            self.assertEqual(logical_calc(lst, operator), expected)

        with (allure.step("Pass an array with 3 members (negative)")):
            lst: list = [False, False, False]
            operator: str = 'AND'
            expected: bool = False
            print_log(list=lst, operator=operator, expected=expected)
            self.assertEqual(logical_calc(lst, operator), expected)

        with allure.step("Pass an array with 3 members (positive)"):
            lst: list = [True, True, True]
            operator: str = 'AND'
            expected: bool = True
            print_log(list=lst, operator=operator, expected=expected)
            self.assertEqual(logical_calc(lst, operator), expected)

        with allure.step("Pass large array (negative)"):
            lst: list = [False, False, False, False, True, True, False,
                         True, True, False, False, True, True, False,
                         False, False, False, True, True, False, True,
                         False, False, True, True, True, False, True,
                         True, False, False, False, False, False, False,
                         True, True, True, True, False, True, True, False,
                         True, True, False, False, True, False, False]
            operator: str = 'AND'
            expected: bool = False
            print_log(list=lst, operator=operator, expected=expected)
            self.assertEqual(logical_calc(lst, operator), expected)

    def test_logical_calc_or(self):
        """
        In logic and mathematics, or is the
        truth-functional operator of (inclusive)
        disjunction, also known as alternation.

        The or of a set of operands is true if
        and only if one or more of its operands is true.

        Source:
        https://en.wikipedia.org/wiki/Logical_disjunction

        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("OR logical operator")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable=R0801
        with allure.step('Pass an array with 2 members (positive)'):
            lst: list = [True, False]
            operator: str = 'OR'
            expected: bool = True
            print_log(list=lst, operator=operator, expected=expected)
            self.assertEqual(logical_calc(lst, operator), expected)

        with allure.step('Pass an array with 3 members (positive)'):
            lst: list = [True, True, False]
            operator: str = 'OR'
            expected: bool = True
            print_log(list=lst, operator=operator, expected=expected)
            self.assertEqual(logical_calc(lst, operator), expected)

        with allure.step('Pass an array with 3 members (negative)'):
            lst: list = [False, False, False]
            operator: str = 'OR'
            expected: bool = False
            print_log(list=lst, operator=operator, expected=expected)
            self.assertEqual(logical_calc(lst, operator), expected)

        with allure.step('Pass large array (positive)'):
            lst: list = [False, True, True, False, False, False, True, False,
                         False, False, False, True, True, False, False, False,
                         True, False, False, True, True, True, True, True,
                         False, True, True, True, False, True, False, False,
                         True, True, True, True, True, True, False, True,
                         False, True, False, True, False, True, False, True,
                         True, True]
            operator: str = 'OR'
            expected: bool = True
            print_log(list=lst, operator=operator, expected=expected)
            self.assertEqual(logical_calc(lst, operator), expected)

    def test_logical_calc_xor(self):
        """
        Exclusive or or exclusive disjunction is a
        logical operation that outputs true only when
        inputs differ (one is true, the other is false).

        XOR outputs true whenever the inputs differ:

        Source:
        https://en.wikipedia.org/wiki/Exclusive_or
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("XOR logical operator")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable=R0801
        with allure.step('Pass an array with 2 members (positive)'):
            lst: list = [True, False]
            operator: str = 'OR'
            expected: bool = True
            print_log(list=lst, operator=operator, expected=expected)
            self.assertEqual(logical_calc(lst, operator), expected)

        with allure.step('Pass an array with 3 members (negative)'):
            lst: list = [True, True, False]
            operator: str = 'XOR'
            expected: bool = False
            print_log(list=lst, operator=operator, expected=expected)
            self.assertEqual(logical_calc(lst, operator), expected)

        with allure.step('Pass medium size array'):
            lst: list = [False, False, True, True, False,
                         False, False, False, True]
            operator: str = 'XOR'
            expected: bool = True
            print_log(list=lst, operator=operator, expected=expected)
            self.assertEqual(expected, logical_calc(lst, operator))

        with allure.step('Pass large size array #1'):
            lst: list = [False, False, True, False, False, True, True,
                         True, False, False, True, False, False, False,
                         False, True, False, True, False, False, True,
                         False, False, True, True, True, False, False,
                         False, False, True, False, False, False, False,
                         False, True, False, False, False, True, True,
                         False, True, False, True, False, False, True,
                         False]
            operator: str = 'XOR'
            expected: bool = False
            print_log(list=lst, operator=operator, expected=expected)
            self.assertEqual(expected, logical_calc(lst, operator))

        with allure.step('Pass large size array #2'):
            lst: list = [True, True, False, False, False, True, True, False,
                         False, True, False, False, True, False, False, True,
                         True, True, True, True, True, False, False, False,
                         False, True, True, False, False, True, True, True,
                         True, False, True, True, False, False, False, True,
                         False, True, False, True, False, False, True, False,
                         True, True]
            operator: str = 'XOR'
            expected: bool = False
            print_log(list=lst, operator=operator, expected=expected)
            self.assertEqual(expected, logical_calc(lst, operator))
