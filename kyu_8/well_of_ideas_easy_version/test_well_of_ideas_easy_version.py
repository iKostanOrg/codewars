"""
Tests for -> Well of Ideas - Easy Version
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# REFACTORING FUNDAMENTALS ARRAYS STRINGS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.well_of_ideas_easy_version.well_of_ideas_easy_version import well


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Well of Ideas - Easy Version')
@allure.tag('REFACTORING', 'FUNDAMENTALS', 'ARRAYS', 'STRINGS')
@allure.link(url='https://www.codewars.com/kata/57f222ce69e09c3630000212/train/python',
             name='Source/Kata')
class WellTestCase(unittest.TestCase):
    """
    Testing well function
    """

    def test_well_fail(self):
        """
        If there are no good ideas,
        as is often the case, return 'Fail!'.
        :return:
        """

        allure.dynamic.title("Should return 'Fail!'s")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Pass list with no 'good' in it"):
            lst = ['bad', 'bad', 'bad']
            expected = 'Fail!'

            print_log(list=lst, expected=expected)
            self.assertEqual(well(lst), expected)

    def test_well_publish(self):
        """
        If there are one or two good ideas,
        return 'Publish!',
        :return:
        """

        allure.dynamic.title("Should return 'Publish!'")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Pass list with one 'good' in it"):
            lst = ['good', 'bad', 'bad', 'bad', 'bad']
            expected = 'Publish!'

            print_log(list=lst, expected=expected)
            self.assertEqual(well(lst), expected)

    def test_well_series(self):
        """
        if there are more than 2 return
        'I smell a series!'.
        :return:
        """

        allure.dynamic.title("Should return 'I smell a series!'")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Pass list with more than 2 'good' in it"):
            lst = ['good', 'bad', 'bad',
                   'bad', 'bad', 'good',
                   'bad', 'bad', 'good']
            expected = 'I smell a series!'

            print_log(list=lst, expected=expected)
            self.assertEqual(well(lst), expected)
