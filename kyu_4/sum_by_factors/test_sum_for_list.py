"""
Testing sum_for_list function

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS NUMBERS ARRAYS

import unittest
import allure
from utils.log_func import print_log
from kyu_4.sum_by_factors.sum_for_list import sum_for_list


@allure.epic('4 kyu')
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Sum by Factors')
@allure.tag('ALGORITHMS',
            'NUMBERS',
            'ARRAYS')
@allure.link(
    url='https://www.codewars.com/kata/54d496788776e49e6b00052f/train/python',
    name='Source/Kata')
class SumForListTestCase(unittest.TestCase):
    """
    Testing sum_for_list function
    """

    def test_sum_for_list(self):
        """
        Testing sum_for_list function
        :return:
        """

        allure.dynamic.title("Testing sum_for_list function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Verify that one given an array of positive "
            "or negative integers I= [i1,..,in] the function "
            "produces a sorted array P of the form "
            "[[p, sum of all ij of I for which p is a prime factor (p positive) of ij]...]"
            "</p>")

        test_data = (
            ([12, 15],
             [[2, 12], [3, 27], [5, 15]]),
            ([15, 21, 24, 30, 45],
             [[2, 54], [3, 135], [5, 90], [7, 21]]),
            ([107, 158, 204, 100, 118, 123, 126, 110, 116, 100],
             [[2, 1032], [3, 453], [5, 310], [7, 126], [11, 110],
              [17, 204], [29, 116], [41, 123], [59, 118], [79, 158],
              [107, 107]]),
            ([-29804, -4209, -28265, -72769, -31744],
             [[2, -61548], [3, -4209], [5, -28265], [23, -4209], [31, -31744],
              [53, -72769], [61, -4209], [1373, -72769], [5653, -28265], [7451, -29804]]),
            ([15, -36, -133, -61, -54, 78, -126, -113, -106, -158],
             [[2, -402], [3, -123], [5, 15], [7, -259], [13, 78], [19, -133],
              [53, -106], [61, -61], [79, -158], [113, -113]]),
            ([154, -150, -196, -164, -57, 133, -110, -126, -191, -171, 131, -55, -85, -37, -113],
             [[2, -592], [3, -504], [5, -400], [7, -35], [11, -11], [17, -85], [19, -95],
              [37, -37], [41, -164], [113, -113], [131, 131], [191, -191]]),
            ([12, -138, -175, -64, -153, 11, -11, -126, -67, -30, 153, -72, -102],
             [[2, -520], [3, -456], [5, -205], [7, -301], [11, 0], [17, -102], [23, -138],
              [67, -67]])
        )

        for lst, expected in test_data:

            actual_result = sum_for_list(lst)
            print_log(expected=expected,
                      actual_result=actual_result)

            with allure.step(f"Enter test list ({lst}) and "
                             f"verify the output ({actual_result}) vs "
                             f"expected ({expected})"):
                self.assertListEqual(expected, actual_result)
