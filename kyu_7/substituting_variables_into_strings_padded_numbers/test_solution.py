#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS STRINGS STRING FORMATTING FORMATTING ALGORITHMS

import unittest
import allure
from utils.log_func import print_log
from kyu_7.substituting_variables_into_strings_padded_numbers.solution import solution


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Substituting Variables Into Strings: Padded Numbers')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class SolutionTestCase(unittest.TestCase):
    """
    Testing 'solution' function
    """

    def test_solution(self):
        """
        Testing 'solution' function.

        The should return a formatted string.
        The return value should equal "Value is VALUE"
        where value is a 5 digit padded number.
        :return:
        """

        allure.dynamic.title("Testing 'solution' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Enter a number and verify the result"):

            test_data = [
                (0, 'Value is 00000'),
                (5, 'Value is 00005'),
                (109, 'Value is 00109'),
                (1204, 'Value is 01204'),
            ]

            for value, expected in test_data:
                print_log(expected=expected, value=value)
                self.assertEqual(expected, solution(value))
