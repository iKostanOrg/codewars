"""
Testing for -> Calculator class

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS PARSING STRINGS EXPRESSIONS BASIC LANGUAGE FEATURES FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_3.calculator.calculator import Calculator


@allure.epic('3 kyu')
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Calculator')
@allure.tag('ALGORITHMS',
            'PARSING',
            'STRINGS',
            'EXPRESSIONS',
            'BASIC LANGUAGE FEATURES',
            'FUNDAMENTALS')
@allure.link(url='https://www.codewars.com/kata/5235c913397cbf2508000048/train/python',
             name='Source/Kata')
class CalculatorTestCase(unittest.TestCase):
    """
    Testing Calculator class
    """

    def test_calculator(self):
        """
        Testing Calculator class
        A simple calculator that given a string of operators '()', '+', '-', '*', '/'
        and numbers separated by spaces will return the value of that expression

        :return: None
        """

        allure.dynamic.title("Testing Calculator class")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>"
                                        "1. given a string of operators '(), +, -, *, /'"
                                        "and numbers separated by spaces<br/>"
                                        "2. the calculator should return the value of that expression"
                                        "</p>")

        test_data = (
            ('127', 127),
            ('2 + 3', 5),
            ('2 - 3 - 4', -5),
            ('10 * 5 / 2', 25),
            ('2 / 2 + 3 * 4 - 6', 7),
            ('2 + 3 * 4 / 3 - 6 / 3 * 3 + 8', 8),
            ('1.1 + 2.2 + 3.3', 6.6),
            ('1.1 * 2.2 * 3.3', 7.986000000000001),
            ('10 * 5 / 2', 25)
        )

        for string, expected in test_data:
            actual_result = Calculator().evaluate(string)
            print_log(string=string,
                      expected=expected,
                      actual_result=actual_result)

            with allure.step(f"Enter a test string ({string}), "
                             f"calculate the result ({actual_result}) and "
                             f"compare vs expected ({expected})"):

                self.assertEqual(expected,
                                 actual_result)
