"""
Test for -> Valid Parentheses
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# STRINGS PARSING ALGORITHMS

import unittest
import allure
from utils.log_func import print_log
from kyu_7.valid_parentheses.solution import valid_parentheses


# pylint: disable=R0801
@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Valid Parentheses')
@allure.tag('STRINGS',
            'PARSING',
            'ALGORITHMS')
@allure.link(
    url='https://www.codewars.com/kata/6411b91a5e71b915d237332d',
    name='Source/Kata')
# pylint: enable=R0801
class ValidParenthesesTestCase(unittest.TestCase):
    """
    Testing valid_parentheses function
    """

    def test_valid_parentheses_true(self):
        """
        -1: Negative numbers cannot be square numbers
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Simple test for valid parentheses")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Should return True for valid parentheses.</p>")
        # pylint: enable=R0801
        test_data: tuple = (
            "()",
            "((()))",
            "()()()",
            "(()())()",
            "()(())((()))(())()")

        for test_str in test_data:
            with allure.step(f"Enter test string {test_data}"
                             f"and verify that the function returns True."):
                result: bool = valid_parentheses(test_str)
                print_log(test_data=test_data, result=result)
                self.assertTrue(result)

    def test_valid_parentheses_false(self):
        """
        0 is a square number
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Simple test for invalid parentheses")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Should return False for invalid parentheses</p>")
        # pylint: enable=R0801
        test_data: tuple = (
            ")(",
            "()()(",
            "((())",
            "())(()",
            ")()",
            ")")

        for test_str in test_data:
            with allure.step(f"Enter test string {test_data}"
                             f"and verify that the function returns False."):
                result: bool = valid_parentheses(test_str)
                print_log(test_data=test_data, result=result)
                self.assertFalse(result)

    def test_valid_parentheses_empty_string(self):
        """
        3 is not a square number
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Simple test for empty string.")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Should return True for empty strings.</p>")
        # pylint: enable=R0801
        with allure.step(f"Enter empty test string and verify"
                         f"that the function returns True."):
            result: bool = valid_parentheses('')
            print_log(test_data='', result=result)
            self.assertTrue(result)

    def test_valid_parentheses_large_valid(self):
        """
        Test valid_parentheses function with
        valid large string
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Test for valid large string")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Valid large test string</p>")
        # pylint: enable=R0801
        with (allure.step(f"Enter a large valid test string and verify"
                         f"that the function returns True.")):
            test_str: str = (f'()(()()()()(()())((()()())((((())(()))(()))((('
                             f')(())((()))((())()))(())(()()(())))())))')
            result: bool = valid_parentheses(test_str)
            print_log(test_str=test_str, result=result)
            self.assertTrue(result)

    def test_valid_parentheses_large_invalid(self):
        """
        Test valid_parentheses function with
        invalid large string
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Test for invalid large string")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Invalid large test string</p>")
        # pylint: enable=R0801
        with (allure.step(f"Enter a large invalid test string and verify"
                         f"that the function returns False.")):
            test_str: str = (f'(((())(()()(()()))(())())(((()(()))))()(()()(('
                             f'))))()()()(()())(()()(()()()(()()()((()())))))())()')
            result: bool = valid_parentheses(test_str)
            print_log(test_str=test_str, result=result)
            self.assertFalse(result)
