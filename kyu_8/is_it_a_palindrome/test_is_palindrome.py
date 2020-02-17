#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.is_it_a_palindrome.is_palindrome import is_palindrome


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Is it a palindrome?')
@allure.tag('FUNDAMENTALS')
@allure.link(url='https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python',
             name='Source/Kata')
class IsPalindromeTestCase(unittest.TestCase):
    """
    Testing is_palindrome function
    """

    def test_is_palindrome(self):
        """
        Testing is_palindrome function
        with various test inputs

        The function should check if a
        given string (case insensitive)
        is a palindrome.
        """

        allure.dynamic.title("Testing is_palindrome function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Enter test string and verify the output"):

            test_data = [
                ('a', True),
                ('aba', True),
                ('Abba', True),
                ('malam', True),
                ('walter', False),
                ('kodok', True),
                ('Kasue', False),
                ('NdjXglGnYGKhQtuAcxNWFwVRZZDMrFmiOPMZsvr', False),
                ('XqmUTaAmrrYitgNwkCwaWdFYsEhfIeOohViba', False),
                ('ZtItThFBUPCSCbtcUfDwXzyajhRIWioUHpVzN', False),
                ('XqNeuBjbshHwqjoUNGHhVRolqxWRRWYYbN', False)
            ]

            for string, expected in test_data:
                print_log(string=string, expected=expected)
                self.assertEqual(expected, is_palindrome(string))
