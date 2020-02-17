#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS NUMBERS MATHEMATICS ALGORITHMS ARITHMETIC

import unittest
import allure
from utils.log_func import print_log
from kyu_7.sum_of_triangular_numbers.sum_triangular_numbers import sum_triangular_numbers


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Math")
@allure.story('Sum of Triangular Numbers')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class SumTriangularNumbersTestCase(unittest.TestCase):
    """
    Testing 'sum_triangular_numbers' function
    """

    def test_sum_triangular_numbers_negative_numbers(self):
        """
        Testing 'sum_triangular_numbers' function
        with negative numbers
        :return:
        """

        allure.dynamic.title("Testing 'sum_triangular_numbers' "
                             "with negative numbers")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Enter negative number and verify the output"):
            n = -291
            expected = 0

            print_log(n=n, expected=expected)
            self.assertEqual(sum_triangular_numbers(n), expected)

        with allure.step("Enter negative number and verify the output"):
            n = -971
            expected = 0

            print_log(n=n, expected=expected)
            self.assertEqual(sum_triangular_numbers(n), expected)

    def test_sum_triangular_numbers_zero(self):
        """
        Testing 'sum_triangular_numbers' function
        with zero as an input
        :return:
        """

        allure.dynamic.title("Testing 'sum_triangular_numbers' with zero")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Enter zero and verify the output"):
            n = 0
            expected = 0

            print_log(n=n, expected=expected)
            self.assertEqual(sum_triangular_numbers(n), expected)

    def test_sum_triangular_numbers_positive_numbers(self):
        """
        Testing 'sum_triangular_numbers' function
        with positive numbers
        :return:
        """

        allure.dynamic.title("Testing 'sum_triangular_numbers' "
                             "with positive numbers")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Enter a positive number as an input "
                         "and verify the output"):
            n = 6
            expected = 56

            print_log(n=n, expected=expected)
            self.assertEqual(sum_triangular_numbers(n), expected)

        with allure.step("Enter a positive number as an input "
                         "and verify the output"):
            n = 34
            expected = 7140

            print_log(n=n, expected=expected)
            self.assertEqual(sum_triangular_numbers(n), expected)

    def test_sum_triangular_numbers_big_number(self):
        """
        Testing 'sum_triangular_numbers' function
        with big number as an input
        :return:
        """

        allure.dynamic.title("Testing 'sum_triangular_numbers' "
                             "with big number as an input")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Enter a big number as an input "
                         "and verify the output"):
            n = 943
            expected = 140205240

            print_log(n=n, expected=expected)
            self.assertEqual(sum_triangular_numbers(n), expected)
