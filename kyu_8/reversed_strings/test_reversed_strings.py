#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS STRINGS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.reversed_strings.reversed_strings import solution


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Reversed Strings')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class ReversedStringsTestCase(unittest.TestCase):
    """
    Testing the solution for 'Reversed Strings' problem
    """

    def test_reversed_strings_empty(self):
        """
        Test with empty string
        :return:
        """

        allure.dynamic.title("Test with empty string")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Pass empty string and verify the output"):
            string = ''
            expected = ''

            print_log(string=string, expected=expected)

            self.assertEqual(solution(string), expected)

    def test_reversed_strings_one_char(self):
        """
        Test with one char only
        :return:
        """

        allure.dynamic.title("Test with one char only")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Pass one char string and verify the output"):
            string = 'h'
            expected = 'h'

            print_log(string=string, expected=expected)

            self.assertEqual(solution(string), expected)

    def test_reversed_strings(self):
        """
        Test with regular string
        :return:
        """

        allure.dynamic.title("Test with regular string")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Pass regular string and verify the output"):
            string = 'world'
            expected = 'dlrow'

            print_log(string=string, expected=expected)

            self.assertEqual(solution(string), expected)

        with allure.step("Pass regular string and verify the output"):
            string = 'hello'
            expected = 'olleh'

            print_log(string=string, expected=expected)

            self.assertEqual(solution(string), expected)
