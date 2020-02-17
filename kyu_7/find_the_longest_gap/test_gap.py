#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS REGULAR EXPRESSIONS DECLARATIVE PROGRAMMING ADVANCED LANGUAGE FEATURES STRINGS

import allure
import unittest
from utils.log_func import print_log
from kyu_7.find_the_longest_gap.gap import gap


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Advanced Language Features")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Find the longest gap!')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class GapTestCase(unittest.TestCase):
    """
    Testing gap function
    """

    def test_gap(self):
        """
        Testing gap function with various test inputs

        A binary gap within a positive number num is
        any sequence of consecutive zeros that is
        surrounded by ones at both ends in the binary
        representation of num.

        The gap function should return the length of
        its longest binary gap.

        The function should return 0 if num doesn't
        contain a binary gap.
        :return:
        """

        allure.dynamic.title("Testing gap function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Enter integer and assert the result"):

            data = [
                (9, 2),
                (529, 4),
                (20, 1),
                (15, 0),
            ]

            for num, expected in data:

                print_log(num=num,
                          expected=expected)

                self.assertEqual(expected,
                                 gap(num))
