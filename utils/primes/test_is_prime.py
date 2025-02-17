"""
Test for -> is_prime util
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

import unittest
from parameterized import parameterized
import allure
from utils.log_func import print_log
from utils.primes.is_prime import is_prime


# pylint: disable=R0801
@allure.epic('No kyu')
@allure.parent_suite('Helper methods')
@allure.suite("No kyu helper methods")
@allure.sub_suite("Unit Tests")
@allure.feature("Utils")
@allure.story('Testing is_prime util')
@allure.tag('UTILS',
            "PRIME NUMBERS",
            "PRIMES")
@allure.link(
    url='https://github.com/ikostan/codewars/tree/master/utils',
    name='Source')
# pylint: enable=R0801
class IsPrimeTestCase(unittest.TestCase):
    """
    Testing is_prime function
    """

    @parameterized.expand([
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
        59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
        127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
        191, 193, 197, 199])
    def test_is_prime_positive(self, n):
        """
        Positive test cases for is_prime function testing
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title(
            "Positive test cases for is_prime function testing")
        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Positive test cases for is_prime function testing."
            "</p>")
        # pylint: enable=R0801
        result: bool = is_prime(n)
        with allure.step(
                f"Answer for n: {n} number from the test data is: {result}."):
            print_log(n=n, result=result)
            self.assertTrue(result)

    @parameterized.expand([
        1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28,
        30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52,
        54, 55, 56, 57, 58, 60, 62, 63])
    def test_is_prime_negative(self, n):
        """
        Negative test cases for is_prime function testing
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title(
            "Negative test cases for is_prime function testing")
        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Negative test cases for is_prime function testing."
            "</p>")
        result: bool = is_prime(n)
        with allure.step(
                f"Answer for n: {n} number from the test data is: {result}."):
            print_log(n=n, result=result)
            self.assertFalse(result)
        # pylint: enable=R0801
