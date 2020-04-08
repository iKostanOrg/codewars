#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest
from utils.log_func import print_log
from kyu_5.master_your_primes_sieve_with_memoization.primes import is_prime


@allure.epic('No kyu')
@allure.parent_suite('Helper methods')
@allure.suite("No kyu helper methods")
@allure.sub_suite("Unit Tests")
@allure.feature("Utils")
@allure.story('Testing is_prime util')
@allure.tag('UTILS')
@allure.link(url='https://github.com/ikostan/codewars/tree/master/utils',
             name='Source')
class IsPrimeTestCase(unittest.TestCase):
    """
    Testing is_prime function
    """

    def test_is_prime_positive(self):
        """
        Positive test cases for is_prime function testing
        :return:
        """

        allure.dynamic.title("Positive test cases for is_prime function testing")
        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>Positive test cases for is_prime function testing.</p>")

        test_data = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
                     83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
                     173, 179, 181, 191, 193, 197, 199)

        results = list()
        for n in test_data:
            results.append(is_prime(n))

        actual: bool = all(results)

        with allure.step("Answer for all numbers from the test data is: {}.".format(actual)):
            print_log(actual=actual)
            self.assertTrue(actual)

    def test_is_prime_negative(self):
        """
        Negative test cases for is_prime function testing
        :return:
        """

        allure.dynamic.title("Negative test cases for is_prime function testing")
        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>Negative test cases for is_prime function testing.</p>")

        test_data = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
                     83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
                     173, 179, 181, 191, 193, 197, 199)

        results = list()
        for n in test_data:
            results.append(is_prime(n + 1))

        actual: bool = all(results)

        with allure.step("Answer for all numbers from the test data is: {}.".format(actual)):
            print_log(actual=actual)
            self.assertFalse(actual)
