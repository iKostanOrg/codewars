"""
Test for -> calc method
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS MATHEMATICS NUMBERS EXPRESSIONS
# BASIC LANGUAGE FEATURES FUNDAMENTALS OPERATORS
# PARSING STRINGS

import unittest
import allure  # pylint: disable=import-error
from utils.log_func import print_log
from kyu_2.evaluate_mathematical_expression.evaluate import calc


# pylint: disable=R0801
@allure.epic('2 kyu')
@allure.parent_suite('Proficient')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Evaluate mathematical expression')
@allure.tag('ALGORITHMS',
            'MATHEMATICS',
            'NUMBERS',
            'EXPRESSIONS',
            'BASIC LANGUAGE FEATURES',
            'FUNDAMENTALS',
            'OPERATORS',
            'PARSING STRINGS')
@allure.link(
    url='https://www.codewars.com/kata/52a78825cdfc2cfc87000005',
    name='Source/Kata')
# pylint: enable=R0801
class CalcTestCase(unittest.TestCase):
    """
    Testing calc method
    """

    def test_calc(self):
        """
        Testing calc class
        Given a mathematical expression as a string you
        must return the result as a number.
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing calc function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>"
            "Given a mathematical expression as a string you must "
            "return the result as a number."
            "</p>")
        # pylint: enable=R0801
        test_data: tuple = (
            ["1 + 1", 2],
            ["8/16", 0.5],
            ["3 -(-1)", 4],
            ["2 + -2", 0],
            ["10- 2- -5", 13],
            ["(((10)))", 10],
            ["3 * 5", 15],
            ["-7 * -(6 / 3)", 14],
            ['2 + 3 * 4 / 3 - 6 / 3 * 3 + 8', 8],
            ['1 + 2 * 3 * 3 - 8', 11],
            ['1 + 2 * 3 * (5 - (3 - 1)) - 8', 11],
            ['-(-(-(-1)))', 1],
            ['(((((-1)))))', -1],
            ['58 / 40 - -45 * 13 * 35 - -19 / -71 + 60', 20536.1823943662],
            ['61 + 82 + -81 - -53 * 84 - -83 + -74 / 60', 4595.766666666666],
            ['-(94) * (36 / 64 + -(13)) - (41 - (((-(-15 - 58)))) - -23)', 1178.125],
            ['-(-91) - (92 - -2 / -(13)) / (-42 - -(((-(-90 - 30)))) * -53)', 91.014346478264],
            ['-(-93) / (-36 + 26 + -(18)) + (-7 * -(((-(-67 + -95)))) + -9)', 1121.6785714285713],
            ['-(-23) + (-4 * -13 + -(1)) - (-30 / (((-(57 + -20)))) + 85)', -11.810810810810807],
            ['(72) / (-82 - -93 * -(88)) + (-18 - -(((-(60 * 97)))) + -79)', -5917.00871037987],
            ['-(77) / (7 * -76 + (59)) + (98 / -(((-(-74 - -47)))) / -5)', 0.8887166236003445])

        for string, expected in test_data:

            actual_result = calc(string)
            print_log(string=string,
                      expected=expected,
                      actual_result=actual_result)

            with allure.step(f"Enter a test string ({string}), "
                             f"calculate the result ({actual_result}) and "
                             f"compare vs expected ({expected})"):
                self.assertEqual(expected,
                                 actual_result)

                
if __name__ == '__main__':
    unittest.main()
