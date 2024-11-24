"""
Test for -> Sums of Parts
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# Fundamentals Performance Algorithms

import unittest
import allure
from utils.log_func import print_log
from kyu_6.sums_of_parts.solution import parts_sums


# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Algorithms")
@allure.story('Sums of Parts')
@allure.tag('FUNDAMENTALS',
            'PERFORMANCE',
            'ALGORITHMS')
@allure.link(
    url='https://www.codewars.com/kata/5ce399e0047a45001c853c2b',
    name='Source/Kata')
# pylint: enable-msg=R0801
class PartsSumTestCase(unittest.TestCase):
    """
    Testing 'parts_sums' function
    """

    # pylint: disable-msg=R0801
    def test_parts_sum(self):
        """
        Testing 'parts_sums' function with various test data
        :return:
        """
        allure.dynamic.title("Testing 'parts_sums' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Test a function that take as parameter a list ls and "
            "return a list of the sums of its parts as defined below:<br>"
            "ls = [1, 2, 3, 4, 5, 6]<br>"
            "parts_sums(ls) -> [21, 20, 18, 15, 11, 6, 0]"
            "</p>")
        # pylint: enable-msg=R0801
        test_data: tuple = (
            ([], [0]),
            ([1, 2, 3, 4, 5, 6], [21, 20, 18, 15, 11, 6, 0]),
            ([0, 1, 3, 6, 10], [20, 20, 19, 16, 10, 0]),
            ([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358],
             [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414,
              9291270, 2581057, 2580168, 2579358, 0]))

        for input_ls, expected in test_data:
            actual_result = parts_sums(input_ls)
            # pylint: disable-msg=R0801
            with allure.step(f"Enter a list ls ({input_ls}) and verify the "
                             f"expected output ({expected}) vs "
                             f"actual result ({actual_result})"):

                print_log(input_ls=input_ls,
                          expected=expected,
                          result=actual_result)

                self.assertEqual(expected,
                                 actual_result)
            # pylint: enable-msg=R0801
