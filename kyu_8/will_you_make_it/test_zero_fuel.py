#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS MATHEMATICS ALGORITHMS NUMBERS

import unittest
import allure
from kyu_8.will_you_make_it.zero_fuel import zero_fuel
from utils.log_func import print_log


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Math")
@allure.story('Will you make it?')
@allure.tag('FUNDAMENTALS', 'MATHEMATICS', 'ALGORITHMS', 'NUMBERS')
@allure.link(url='https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python',
             name='Source/Kata')
class ZeroFuelTestCase(unittest.TestCase):
    """
    Testing zero_fuel
    """

    def test_zero_fuel(self):
        allure.dynamic.title("Testing zero_fuel function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>You were camping with your friends far away from home, "
                                        "but when it's time to go back, you realize that you fuel "
                                        "is running out and the nearest pump is 50 miles away! You "
                                        "know that on average, your car runs on about 25 miles per "
                                        "gallon. There are 2 gallons left. Considering these factors, "
                                        "write a function that tells you if it is possible to get to "
                                        "the pump or not. Function should return true (1 in Prolog) if "
                                        "it is possible and false (0 in Prolog) if not. The input values "
                                        "are always positive.</p>")

        test_data = [
            ((50, 25, 2), True),
            ((100, 50, 1), False),
        ]

        for data, expected in test_data:
            actual_result = zero_fuel(data[0], data[1], data[2])
            with allure.step("Enter data ({}) and verify the "
                             "expected output ({}) vs actual result ({})".format(data,
                                                                                 expected,
                                                                                 actual_result)):
                print_log(data=data,
                          expected=expected,
                          result=actual_result)

                self.assertEqual(expected,
                                 actual_result)
