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
@allure.tag('FUNDAMENTALS',
            'LOOPS',
            'CONTROL FLOW',
            'BASIC LANGUAGE FEATURES')
@allure.link(url='https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python',
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
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Enter number and verify the output"):

            test_data = [
                (1, 1),
                (8, 36),
                (22, 253),
                (100, 5050),
                (213, 22791)
            ]

            for d in test_data:

                num = d[0]
                expected = d[1]

                print_log(num=num, expected=expected)
                self.assertEqual(summation(num), expected)
