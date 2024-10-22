"""
Test for -> gen_primes util
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

import unittest
import allure
from utils.log_func import print_log
from utils.primes.primes_generator import gen_primes


# pylint: disable=R0801
@allure.epic('No kyu')
@allure.parent_suite('Helper methods')
@allure.suite("No kyu helper methods")
@allure.sub_suite("Unit Tests")
@allure.feature("Utils")
@allure.story('Testing gen_primes util')
@allure.tag('UTILS',
            "PRIME NUMBERS",
            "PRIMES")
@allure.link(
    url='https://github.com/ikostan/codewars/tree/master/utils',
    name='Source')
# pylint: enable=R0801
class GenPrimesTestCase(unittest.TestCase):
    """
    Testing gen_primes function
    """

    def test_gen_primes_positive(self):
        """
        Positive test cases for gen_primes function testing
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title(
            "Positive test cases for gen_primes function testing")
        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Positive test cases for gen_primes function testing.</p>")
        # pylint: enable=R0801
        test_data: list = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
            53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
            109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
            173, 179, 181, 191, 193, 197, 199]

        results: list = []
        for prime in gen_primes():
            results.append(prime)
            if len(test_data) == len(results):
                break

        with allure.step("Compare expected list with the list of actual results"):
            print_log(test_data=test_data, results=results)
            self.assertListEqual(test_data, results)

    def test_gen_primes_negative(self):
        """
        Negative test cases for gen_primes function testing
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title(
            "Negative test cases for gen_primes function testing")
        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Negative test cases for gen_primes function testing.</p>")
        # pylint: enable=R0801
        test_data: tuple = (
            3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
            61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
            131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
            193, 197, 199)

        primes: list = []
        for prime in gen_primes():
            primes.append(prime)
            if len(test_data) == len(primes):
                break

        results: list = []
        for t in test_data:
            if t in primes:
                results.append(True)
            else:
                results.append(False)

        actual: bool = all(results)

        with allure.step(
                f"Answer for all numbers from the test data is: {actual}."):
            print_log(actual=actual)
            self.assertFalse(actual)
