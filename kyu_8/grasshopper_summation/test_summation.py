#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS LOOPS CONTROL FLOW BASIC LANGUAGE FEATURES

import unittest
import allure
from utils.log_func import print_log
from kyu_8.grasshopper_summation.summation import summation


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Control Flow")
@allure.sub_suite("Unit Tests")
@allure.feature("Loops")
@allure.story('Grasshopper - Summation')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class SummationTestCase(unittest.TestCase):
    """
    Testing summation function
    """

    def test_summation(self):
        """
        Testing summation function
        with various test inputs
        :return:
        """

        allure.dynamic.title("Testing 'summation' function")
        allure.dynamic.severity(allure.severity_level.CRITICAL)

        with allure.step("Enter number and verify the output"):

            data = [
                (1, 1),
                (8, 36),
                (22, 253),
                (100, 5050),
                (213, 22791)
            ]

            for d in data:

                num = d[0]
                expected = d[1]

                print_log(num=num, expected=expected)
                self.assertEqual(summation(num), expected)
