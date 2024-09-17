"""
Test for -> A Rule of Divisibility by 13
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS

import unittest
import allure
from kyu_6.a_rule_of_divisibility_by_13.thirt import thirt
from utils.log_func import print_log


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Math")
@allure.story('A Rule of Divisibility by 13')
@allure.tag('FUNDAMENTALS')
@allure.link(url='https://www.codewars.com/kata/564057bc348c7200bd0000ff/train/python',
             name='Source/Kata')
class ThirtTestCase(unittest.TestCase):
    """
    Testing 'thirt' function
    """
    # pylint: disable-msg=R0801
    def test_thirt(self):
        """
        Testing 'thirt' function with various test data
        :return:
        """
        allure.dynamic.title("Testing 'thirt' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Test a function that processes sequence of operations "
            "on an integer n (>=0). 'thirt' should return the stationary"
            " number.</p>")
        # pylint: enable-msg=R0801
        test_data = (
            (1234567, 87),
            (321, 48),
            (8529, 79),
            (85299258, 31),
            (5634, 57),
            (1111111111, 71),
            (987654321, 30))

        for n, expected in test_data:
            actual_result = thirt(n)
            # pylint: disable-msg=R0801
            with allure.step(f"Enter a n ({n}) and verify the "
                             f"expected output ({expected}) vs "
                             f"actual result ({actual_result})"):

                print_log(n=n,
                          expected=expected,
                          result=actual_result)

                self.assertEqual(expected,
                                 actual_result)
            # pylint: enable-msg=R0801

if __name__ == '__main__':
    unittest.main()
    