"""
Test for -> Valid Braces
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# Algorithms

import unittest
import allure
from utils.log_func import print_log
from kyu_6.valid_braces.valid_braces import valid_braces


# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Algorithms")
@allure.story('Valid Braces')
@allure.tag('FUNDAMENTALS',
            'ALGORITHMS')
@allure.link(
    url='https://www.codewars.com/kata/5277c8a221e209d3f6000b56',
    name='Source/Kata')
# pylint: enable-msg=R0801
class ValidBracesTestCase(unittest.TestCase):
    """
    Testing the 'valid_braces' function
    """
    def test_valid_braces(self):
        """
        Testing the 'valid_braces' function
        with various test data
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing the 'valid_braces' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        # pylint: disable=line-too-long
        with allure.step("Pass test data and verify the output"):
            data: tuple = (
                ("(){}[]", True),
                ("([{}])", True),
                ("(}", False),
                ("[(])", False),
                ("[({})](]", False),
                ("()", True),
                ("[]", True),
                ("[(])", False),
                ("{}", True),
                ("{}()[]", True),
                ("([{}])", True),
                ("([}{])", False),
                ("{}({})[]", True),
                ("(({{[[]]}}))", True),
                ("(((({{", False),
                (")(}{][", False),
                ("())({}}{()][][", False),
                ("{}()[]", True),
                ("([}{])", False),
                ("{}({})[]", True),
            )

            # pylint: enable=line-too-long
            for string, expected in data:
                actual = valid_braces(string)
                print_log(string=string, expected=expected, actual=actual)
                self.assertEqual(expected, actual)
