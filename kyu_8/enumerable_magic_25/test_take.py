#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.enumerable_magic_25.take import take


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Enumerable Magic #25 - Take the First N Elements')
@allure.tag("FUNDAMENTALS")
@allure.link(url='https://www.codewars.com/kata/545afd0761aa4c3055001386/train/python',
             name='Source/Kata')
class TakeTestCase(unittest.TestCase):
    """
    Testing take function
    """

    def test_take(self):
        allure.dynamic.title("Testing take function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>Create a method take that accepts a list/array and a number n, "
                                        "and returns a list/array array of the first n elements from the "
                                        "list/array. If you need help, here's a reference: "
                                        "https://docs.python.org/3/library/stdtypes"
                                        ".html#sequence-types-list-tuple-range</p>")

        test_data = [
            ([0, 1, 2, 3, 5, 8, 13],
             3,
             [0, 1, 2]),
            ([51],
             35,
             [51]),
            ([],
             3,
             []),
            ([0, 1, 2, 3, 5, 8, 13],
             0,
             []),
        ]

        for arr, n, expected in test_data:
            actual_result = take(arr, n)
            with allure.step("Enter a list ({}) and verify the "
                             "expected output ({}) vs actual result ({})".format(arr,
                                                                                 expected,
                                                                                 actual_result)):
                print_log(rr=arr,
                          n=n,
                          expected=expected,
                          result=actual_result)

                self.assertEqual(expected,
                                 actual_result)
