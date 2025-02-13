"""
Test for -> Grasshopper - Check for factor.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS MATHEMATICS ALGORITHMS NUMBERS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_8.grasshopper_check_for_factor.check_for_factor \
    import check_for_factor


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Math")
@allure.sub_suite("Unit Tests")
@allure.feature("Calculation")
@allure.story('Grasshopper - Check for factor')
@allure.tag('FUNDAMENTALS',
            'MATHEMATICS',
            'ALGORITHMS',
            'NUMBERS')
@allure.link(
    url='https://www.codewars.com/kata/55cbc3586671f6aa070000fb',
    name='Source/Kata')
# pylint: disable=R0801
class CheckForFactorTestCase(unittest.TestCase):
    """Testing check_for_factor function."""

    @parameterized.expand([
        (10, 2, True),
        (63, 7, True),
        (2450, 5, True),
        (24612, 3, True)])
    def test_check_for_factor_true(self, base, factor, expected):
        """
        Testing check_for_factor function.

        This function should test if the
        factor is a factor of base.

        Return true if it is a factor.
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing check_for_factor "
                             "function: positive flow")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="'
            'https://www.codewars.com/users/myFirstCode/badges/large'
            '">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable=R0801
        with allure.step("Return true if it is a factor"):
            print_log(base=base, factor=factor, expected=expected)
            self.assertEqual(expected, check_for_factor(base, factor))

    @parameterized.expand([
        (9, 2, False),
        (653, 7, False),
        (2453, 5, False),
        (24617, 3, False)])
    def test_check_for_factor_false(self, base, factor, expected):
        """
        Testing check_for_factor function.

        This function should test if the
        factor is a factor of base.

        Return false if it is not a factor.
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing check_for_factor "
                             "function: positive flow")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="'
            'https://www.codewars.com/users/myFirstCode/badges/large'
            '">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable=R0801
        with allure.step("Return false if it is not a factor"):
            print_log(base=base, factor=factor, expected=expected)
            self.assertEqual(expected, check_for_factor(base, factor))
