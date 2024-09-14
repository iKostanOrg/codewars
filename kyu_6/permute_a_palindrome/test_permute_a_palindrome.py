"""
Test for -> Permute a Palindrome
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS ALGORITHMS

import unittest
import allure
from utils.log_func import print_log
from kyu_6.permute_a_palindrome.permute_a_palindrome import permute_a_palindrome


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Permute a Palindrome')
@allure.tag('FUNDAMENTALS',
            'ALGORITHMS')
@allure.link(url='',
             name='Source/Kata')
class PermutePalindromeTestCase(unittest.TestCase):
    """
    Testing permute_a_palindrome function
    """

    def test_permute_a_palindrome_positive(self):
        """
        Testing permute_a_palindrome function
        :return:
        """
        allure.dynamic.title(
            "Testing permute_a_palindrome (positive)")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")

        with allure.step("Enter test string and verify the result"):
            string = "a"
            expected = True

            print_log(string=string, expected=expected)

            self.assertEqual(permute_a_palindrome(string), expected)

        with allure.step("Enter test string and verify the result"):
            string = "aa"
            expected = True

            print_log(string=string, expected=expected)

            self.assertEqual(permute_a_palindrome(string), expected)

        with allure.step("Enter test string and verify the result"):
            string = "baa"
            expected = True

            print_log(string=string, expected=expected)

            self.assertEqual(permute_a_palindrome(string), expected)

        with allure.step("Enter test string and verify the result"):
            string = "aab"
            expected = True

            print_log(string=string, expected=expected)

            self.assertEqual(permute_a_palindrome(string), expected)

    def test_permute_a_palindrome_negative(self):
        """
        Negative testing permute_a_palindrome function
        :return:
        """
        allure.dynamic.title(
            "Testing permute_a_palindrome (negative)")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")

        with allure.step("Enter test string and verify the result"):
            string = "baabcd"
            expected = False

            print_log(string=string, expected=expected)

            self.assertEqual(permute_a_palindrome(string), expected)

        with allure.step("Enter test string and verify the result"):
            string = "racecars"
            expected = False

            print_log(string=string, expected=expected)

            self.assertEqual(permute_a_palindrome(string), expected)

        with allure.step("Enter test string and verify the result"):
            string = "abcdefghba"
            expected = False

            print_log(string=string, expected=expected)

            self.assertEqual(permute_a_palindrome(string), expected)

    def test_permute_a_palindrome_empty_string(self):
        """
        Testing permute_a_palindrome function with empty string
        :return:
        """
        allure.dynamic.title(
            "Testing permute_a_palindrome (empty string)")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")

        with allure.step("Enter empty string and verify the result"):
            string = ''
            expected = True

            print_log(string=string, expected=expected)

            self.assertEqual(permute_a_palindrome(string), expected)
