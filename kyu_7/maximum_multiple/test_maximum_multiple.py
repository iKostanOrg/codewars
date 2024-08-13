#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import unittest
import allure
from utils.log_func import print_log
from kyu_7.maximum_multiple.maximum_multiple import max_multiple

# FUNDAMENTALS NUMBERS BASIC LANGUAGE FEATURES ARRAYS LOOPS CONTROL FLOW


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Control Flow")
@allure.story('Maximum Multiple')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class MaximumMultipleTestCase(unittest.TestCase):
    """
    Testing max_multiple function
    """

    def test_maximum_multiple(self):
        """
        Testing max_multiple function with
        various test data

        Given a Divisor and a Bound ,
        Find the largest integer N , Such That ,

        Conditions:
        1. N is divisible by divisor
        2. N is less than or equal to bound
        3. N is greater than 0.

        Notes:
        1. The parameters (divisor, bound)
            passed to the function are only positve values .
        2. It's guaranteed that a divisor is Found .
        :return:
        """

        allure.dynamic.title("Testing max_multiple function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Enter divisor, bound and verify the output"):

            data = [
                (2, 7, 6),
                (3, 10, 9),
                (7, 17, 14),
                (10, 50, 50),
                (37, 200, 185),
                (7, 100, 98),
                (37, 100, 74),
                (1, 13, 13),
                (1, 1, 1),
                (22, 9, 0),
                (43, 7, 0),
                (50, 7, 0)
            ]

            for divisor, bound, expected in data:

                print_log(divisor=divisor,
                          bound=bound,
                          expected=expected)

                self.assertEqual(expected,
                                 max_multiple(divisor,
                                              bound))
