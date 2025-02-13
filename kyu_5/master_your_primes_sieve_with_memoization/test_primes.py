"""
Test for -> Master your primes: sieve with memoization.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS MEMOIZATION DESIGN PATTERNS
# DESIGN PRINCIPLES OPTIMIZATION

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_5.master_your_primes_sieve_with_memoization.primes \
    import is_prime


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Memoization")
@allure.story('Master your primes: sieve with memoization')
@allure.tag('ALGORITHMS',
            'MEMOIZATION',
            'DESIGN PATTERNS',
            'DESIGN PRINCIPLES',
            'OPTIMIZATION')
@allure.link(
    url='https://www.codewars.com/kata/58603c898989d15e9e000475',
    name='Source/Kata')
class PrimesTestCase(unittest.TestCase):
    """Testing is_prime function."""

    @parameterized.expand([
        (1, False),
        (2, True),
        (5, True),
        (143, False),
        (-1, False),
        (29, True),
        (53, True),
        (529, False),
        (4539131, True),
        (110268984695, False),
        (97444114757, False),
        (7301162915, False),
        (8033908462571, False),
        (8813991225347, False),
        (857561895605, False),
        (13, True),
        (17, True),
        (19, True),
        (23, True),
        (29, True)])
    def test_is_primes(self, number, expected):
        """
        Testing is_prime function with various test data.

        Testing a function that checks if a given number n is a prime
        looping through it and, possibly, expanding the array/list of
        known primes only if/when necessary (ie: as soon as you check
        for a potential prime which is greater than a given threshold
        for each n, stop).

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing is_prime function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step(f"Enter test number: {number} "
                         f"and verify the output: {expected}."):
            print_log(number=number, expected=expected)
            self.assertEqual(expected, is_prime(number))
