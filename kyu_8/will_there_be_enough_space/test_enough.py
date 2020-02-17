#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS NUMBERS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.will_there_be_enough_space.enough import enough


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Math")
@allure.sub_suite("Unit Tests")
@allure.feature("Calculation")
@allure.story('Will there be enough space?')
@allure.tag('FUNDAMENTALS', 'NUMBERS')
@allure.link(url='https://www.codewars.com/kata/5875b200d520904a04000003/train/python',
             name='Source/Kata')
class EnoughTestCase(unittest.TestCase):
    """
    Testing enough function
    """

    def test_enough(self):
        """
        Testing enough function
        with various test data

        If there is enough space, return 0,
        and if there isn't, return the number
        of passengers he can't take.
        :return:
        """

        allure.dynamic.title("STesting enough function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Enter test data and "
                         "verify the output"):
            test_data = [
                ((10, 5, 5), 0),
                ((100, 60, 50), 10),
                ((20, 5, 5), 0),
            ]

            for test_dat, expected in test_data:

                cap = test_dat[0]
                on = test_dat[1]
                wait = test_dat[2]

                print_log(cap=cap,
                          on=on,
                          wait=wait,
                          expected=expected)

                self.assertEqual(expected,
                                 enough(cap, on, wait))
