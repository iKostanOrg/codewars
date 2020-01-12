#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS NUMBERS BASIC LANGUAGE FEATURES CONDITIONAL STATEMENTS CONTROL FLOW ALGORITHMS

import unittest
import allure
from utils.log_func import print_log
from kyu_7.sort_out_the_men_from_boys.men_from_boys import men_from_boys


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Sort Out The Men From Boys')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class MenFromBoysTestCase(unittest.TestCase):
    """
    Testing men_from_boys function
    """

    def test_men_from_boys(self):
        """
        Testing men_from_boys function with
        various test inputs

        Scenario
        Now that the competition gets tough it
        will Sort out the men from the boys .

        Men are the Even numbers and Boys are
        the odd !alt !alt

        Task
        Given an array/list [] of n integers ,
        Separate The even numbers from the odds ,
        or Separate the men from the boys !alt !alt

        Notes
        Return an array/list where Even numbers
        come first then odds.
        Since , Men are stronger than Boys ,
        Then Even numbers in ascending order
        While odds in descending.
        :return:
        """
        allure.dynamic.title('Testing men_from_boys function')
        allure.dynamic.severity(allure.severity_level.CRITICAL)

        with allure.step('Given an list of integers => '
                         'separate the even numbers from the odds'):
            data = [
                ([7, 3, 14, 17],
                 [14, 17, 7, 3]),
                ([2, 43, 95, 90, 37],
                 [2, 90, 95, 43, 37]),
                ([20, 33, 50, 34, 43, 46],
                 [20, 34, 46, 50, 43, 33]),
                ([82, 91, 72, 76, 76, 100, 85],
                 [72, 76, 82, 100, 91, 85]),
                ([2, 15, 17, 15, 2, 10, 10, 17, 1, 1],
                 [2, 10, 17, 15, 1]),
                ([-32, -39, -35, -41],
                 [-32, -35, -39, -41]),
                ([-64, -71, -63, -66, -65],
                 [-66, -64, -63, -65, -71]),
                ([-94, -99, -100, -99, -96, -99],
                 [-100, -96, -94, -99]),
                ([-53, -26, -53, -27, -49, -51, -14],
                 [-26, -14, -27, -49, -51, -53]),
                ([-17, -45, -15, -33, -85, -56, -86, -30],
                 [-86, -56, -30, -15, -17, -33, -45, -85]),
                ([12, 89, -38, -78],
                 [-78, -38, 12, 89]),
                ([2, -43, 95, -90, 37],
                 [-90, 2, 95, 37, -43]),
                ([82, -61, -87, -12, 21, 1],
                 [-12, 82, 21, 1, -61, -87]),
                ([63, -57, 76, -85, 88, 2, -28],
                 [-28, 2, 76, 88, 63, -57, -85]),
                ([49, 818, -282, 900, 928, 281, -282, -1],
                 [-282, 818, 900, 928, 281, 49, -1])
            ]

            for arr, expected in data:
                print_log(arr=arr, expected=expected)
                self.assertEqual(expected, men_from_boys(arr))
