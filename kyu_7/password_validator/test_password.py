"""
Test for -> Password validator
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS REGULAR EXPRESSIONS DECLARATIVE PROGRAMMING
# ADVANCED LANGUAGE FEATURES STRINGS

import unittest
import allure
from utils.log_func import print_log
from kyu_7.password_validator.password import password

# pylint: disable-msg=R0801
@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Password validator')
@allure.tag('FUNDAMENTALS',
            'REGULAR EXPRESSIONS',
            'DECLARATIVE PROGRAMMING',
            'ADVANCED LANGUAGE FEATURES',
            'STRINGS')
@allure.link(
    url='https://www.codewars.com/kata/56a921fa8c5167d8e7000053/train/python',
    name='Source/Kata')
# pylint: enable-msg=R0801
class PasswordTestCase(unittest.TestCase):
    """
    Testing password function
    """

    def test_password(self):
        """
        Testing password function with various test inputs
        :return:
        """
        allure.dynamic.title("Testing password function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")

        with allure.step("Enter test string and verify the result"):
            test_data = [
                ("Abcd1234", True),
                ("Abcd123", False),
                ("abcd1234", False),
                ("AbcdefGhijKlmnopQRsTuvwxyZ1234567890", True),
                ("ABCD1234", False),
                (r"Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,", True),
                (r"!@#$%^&*()-_+={}[]|\:;?/>.<,", False),
                ("", False),
                (" aA1----", True),
                ("4aA1----", True),
            ]

            for string, expected in test_data:
                print_log(string=string, expected=expected)
                self.assertEqual(expected, password(string))
