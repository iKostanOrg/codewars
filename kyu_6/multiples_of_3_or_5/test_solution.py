"""
Test for -> Multiples of 3 or 5
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

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
@allure.tag('ALGORITHMS',
            'MATHEMATICS',
            'NUMBERS')
@allure.link(
    url='https://www.codewars.com/kata/514b92a657cdc65150000006/train/python',
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
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing the 'solution' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        test_data: tuple = (
            (4, 3, 'Should return 3 for n=4'),
            (200, 9168, 'Should return 9168 for n=200'),
            (-1, 0, 'Should return 0 for n=-1'),
            (1291, 388935, 'Random test')
        )

        for td in test_data:
            number, expected, msg = td
            with allure.step(
                    f"Pass test data ({number}) and verify the output"):
                
                print_log(expected=expected, number=number, msg=msg)
                self.assertEqual(expected, solution(number), msg)
