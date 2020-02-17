#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS MATHEMATICS NUMBERS

import unittest
import allure
from utils.log_func import print_log
from kyu_6.multiples_of_3_or_5.solution import solution


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Algorithms")
@allure.story('Multiples of 3 or 5')
@allure.tag('ALGORITHMS', 'MATHEMATICS', 'NUMBERS')
@allure.link(url='',
             name='Source/Kata')
class SolutionTestCase(unittest.TestCase):
    """
    Testing solution function
    """
    def test_solution(self):
        """
        Testing solution function

        If we list all the natural numbers below 10
        that are multiples of 3 or 5, we get 3, 5, 6 and 9.
        The sum of these multiples is 23.

        Finish the solution so that it returns the sum of
        all the multiples of 3 or 5 below the number passed in.

        Note: If the number is a multiple of both 3 and 5,
        only count it once.
        :return:
        """

        allure.dynamic.title("Testing the 'solution' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Pass test data and verify the output"):
            number = 10
            expected = 23
            print_log(expected=expected, number=number)
            self.assertEqual(expected, solution(number))
