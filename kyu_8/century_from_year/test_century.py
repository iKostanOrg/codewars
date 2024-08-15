"""
Century From Year

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS NUMBERS MATHEMATICS ALGORITHMS BASIC LANGUAGE FEATURES DATES/TIME

import unittest
import allure

from kyu_8.century_from_year.century import century
from utils.log_func import print_log


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Numbers")
@allure.sub_suite("Unit Tests")
@allure.feature("Math")
@allure.story('Century From Year')
@allure.tag('FUNDAMENTALS' 'NUMBERS' 'MATHEMATICS' 'ALGORITHMS' 'BASIC LANGUAGE FEATURES' 'DATES/TIME')
@allure.link(url='https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python',
             name='Source/Kata')
class CenturyTestCase(unittest.TestCase):
    """
    The first century spans from the year 1 up to and
    including the year 100, The second - from the year
    101 up to and including the year 200, etc.
    """

    def test_century(self):
        """
        Testing century function
        """
        allure.dynamic.title("Testing century function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Given a year, the function should return the century it is in.</p>")

        test_data = [
            (1705, 18, 'Testing for year 1705'),
            (1900, 19, 'Testing for year 1900'),
            (1601, 17, 'Testing for year 1601'),
            (2000, 20, 'Testing for year 2000'),
            (356, 4, 'Testing for year 356'),
            (89, 1, 'Testing for year 89')
        ]

        for year, expected, message in test_data:
            print('\n', message)
            result = century(year)
            with allure.step("Enter test year ({}) and verify "
                             "the output ({}) vs expected ({})".format(year,
                                                                       result,
                                                                       expected)):
                print_log(year=year,
                          result=result,
                          expected=expected)

                self.assertEqual(expected,
                                 result)
