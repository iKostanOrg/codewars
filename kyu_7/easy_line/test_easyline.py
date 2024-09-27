"""
Test for -> Easy Line
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

import unittest
import pytest
import allure
from utils.log_func import print_log
from kyu_7.easy_line.easyline import easy_line, calc_combination_per_row_item


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Math")
@allure.story("Easy Line")
@allure.tag('FUNDAMENTALS',
            'MATHEMATICS',
            'ALGORITHMS',
            'NUMBERS')
@allure.link(
    url='https://www.codewars.com/kata/56e7d40129035aed6c000632/train/python',
    name='Source/Kata')
class EasyLineTestCase(unittest.TestCase):
    """
    We want to calculate the sum of the squares of the binomial
    coefficients on a given line with a function called easyline
    (or easyLine or easy-line).

    Can you write a program which calculate easyline(n) where n
    is the line number?

    The function will take n (with: n>= 0) as parameter and will
    return the sum of the squares of the binomial coefficients on line n.
    """

    def test_easy_line_exception(self):
        """
        Testing easy line function exception
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title(
            "Testing easy_line function exception message")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>The function should raise exception for invalid "
            "n (n < 0) values.</p>")
        # pylint: enable-msg=R0801
        n: int = -1
        error_txt: str = f'ERROR: invalid n ({n}) value. n must be >= 0'

        # Source: https://dev.to/wangonya/asserting-exceptions-with-pytest-8hl
        with allure.step(f"Enter invalid n ({n}) "
                         f"and assert exception message: {error_txt})."):
            with pytest.raises(ValueError) as error:
                self.assertRaises(ValueError, easy_line(n))
                self.assertEqual(error_txt, error.value)

    def test_calc_combinations_per_row(self):
        """
        Testing calc_combinations_per_row function
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title(
            "Testing calc_combinations_per_row function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>The function should take row number and return "
            "Pascal's Triangle "
            "combination per that row "
            "coefficients on line n.</p>")
        # pylint: enable-msg=R0801
        test_data: tuple = (
            (0, 0, 1),
            (1, 1, 1),
            (2, 1, 2),
            (3, 2, 3),
            (4, 3, 4),
            (5, 4, 5),
            (6, 5, 6),
            (7, 6, 7))

        for data in test_data:
            n: int = data[0]
            i: int = data[1]
            expected: int = data[2]
            actual: int = calc_combination_per_row_item(n, i)

            with allure.step(f"Enter row number ({n}) "
                             f"and assert expected ({expected}) "
                             f"vs actual ({actual})."):
                print_log(n=n,
                          actual=actual,
                          expected=expected)

                self.assertEqual(expected, actual)

    def test_easy_line(self):
        """
        Testing easy_line function
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title(
            "Testing easy_line function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>The function should take n (with: n>= 0) as parameter "
            "and must return the sum of the squares of the binomial "
            "coefficients on line n.</p>")
        # pylint: enable-msg=R0801
        test_data: tuple = (
            (0, 1),
            (1, 2),
            (4, 70),
            (7, 3432),
            (13, 10400600),
            (17, 2333606220),
            (19, 35345263800),
            (22, 2104098963720),
            (24, 32247603683100),
            (50, 100891344545564193334812497256))

        for data in test_data:
            n: int = data[0]
            expected: int = data[1]
            actual: int = easy_line(n)

            with allure.step(f"Enter line number ({n}) "
                             f"and assert expected ({expected}) "
                             f"vs actual ({actual})."):

                print_log(n=n,
                          actual=actual,
                          expected=expected)

                self.assertEqual(expected, actual)
