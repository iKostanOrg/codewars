#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS, ALGORITHMS

import unittest
import allure
from utils.log_func import print_log
from kyu_7.beginner_series_sum_of_numbers.sum_of_numbers import get_sum


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Addition")
@allure.story('Sum of Numbers')
@allure.tag('FUNDAMENTALS', 'ALGORITHMS')
@allure.link(url='',
             name='Source/Kata')
class SumOfNumbersTestCase(unittest.TestCase):
    """
    Testing get_sum function
    """

    def test_get_sum_equal_numbers(self):
        """
        a and b are equal
        :return:
        """

        allure.dynamic.title("a and b are equal")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Assert the result"):
            a = b = expected = 1

            print_log(a=a, b=b, expected=expected)

            self.assertEqual(get_sum(a, b), expected)

    def test_get_sum_positive_numbers(self):
        """
        a an b are positive numbers
        :return:
        """

        allure.dynamic.title("a an b are positive numbers")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Assert the result"):
            a = 0
            b = expected = 1

            print_log(a=a, b=b, expected=expected)

            self.assertEqual(get_sum(a, b), expected)

        with allure.step("Assert the result"):
            a = expected = 1
            b = 0

            print_log(a=a, b=b, expected=expected)

            self.assertEqual(get_sum(a, b), expected)

        with allure.step("Assert the result"):
            a = 1
            b = 2
            expected = a + b

            print_log(a=a, b=b, expected=expected)

            self.assertEqual(get_sum(a, b), expected)

    def test_get_sum_negative_numbers(self):
        """
        a or b is negative
        :return:
        """

        allure.dynamic.title("a or b is negative")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Assert the result"):
            a = 0
            b = -1
            expected = -1

            print_log(a=a, b=b, expected=expected)

            self.assertEqual(get_sum(a, b), expected)

        with allure.step("Assert the result"):
            a = -1
            b = 0
            expected = a + b

            print_log(a=a, b=b, expected=expected)

            self.assertEqual(get_sum(a, b), expected)

        with allure.step("Assert the result"):
            a = -1
            b = 2
            expected = 2

            print_log(a=a, b=b, expected=expected)

            self.assertEqual(get_sum(a, b), expected)
