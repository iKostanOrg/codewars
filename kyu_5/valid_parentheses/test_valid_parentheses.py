#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS VALIDATION UTILITIES

import unittest
import allure
from kyu_5.valid_parentheses.valid_parentheses import valid_parentheses
from utils.log_func import print_log


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Validation")
@allure.story('Valid Parentheses')
@allure.tag('ALGORITHMS', 'VALIDATION', 'UTILITIES')
@allure.link(url='https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python',
             name='Source/Kata')
class ValidParenthesesTestCase(unittest.TestCase):
    """
    Testing valid_parentheses function
    """

    def test_valid_parentheses(self):
        """
        Test the function called that takes a string of parentheses,
        and determines if the order of the parentheses is valid.
        The function should return true if the string is valid,
        and false if it's invalid.

        Examples

        "()"              =>  true
        ")(()))"          =>  false
        "("               =>  false
        "(())((()())())"  =>  true
        :return:
        """

        allure.dynamic.title("Testing valid_parentheses function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Enter test string and verify the output"):
            test_data = [
                ("  (", False),
                (")test", False),
                ("", True),
                ("hi())(", False),
                ("hi(hi)()", True),
                ("()", True),
                (")(()))", False),
                ("(", False),
                ("(())((()())())", True),
            ]

            for string, expected in test_data:
                print_log(string=string,
                          expected=expected)
                self.assertEqual(expected,
                                 valid_parentheses(string))
