#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS, INTRODUCTION

import unittest
import allure
from utils.log_func import print_log
from kyu_8.multiply.multiply import multiply


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Math")
@allure.sub_suite("Unit Tests")
@allure.feature("Multiplication")
@allure.story('Multiply')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class MultiplyTestCase(unittest.TestCase):
    """
    Testing multiply function
    """

    def test_multiply(self):
        """
        Verify that multiply function
        returns correct result
        :return:
        """

        allure.dynamic.title("'multiply' function verification")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Assert (a * b) result"):
            a = 1
            b = 2
            expected = a * b

            print_log(a=a, b=b, expected=expected)

            self.assertEqual(expected,
                             multiply(a, b))
