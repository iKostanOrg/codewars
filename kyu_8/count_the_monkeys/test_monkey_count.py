#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS ARRAYS FUNDAMENTALS RANGES BASIC LANGUAGE FEATURES LISTS DATA STRUCTURES

import allure
import unittest
from utils.log_func import print_log
from kyu_8.count_the_monkeys.monkey_count import monkey_count


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Count the Monkeys!')
@allure.tag('ALGORITHMS', 'ARRAYS', 'FUNDAMENTALS',
            'RANGES', 'BASIC LANGUAGE FEATURES',
            'LISTS' 'DATA STRUCTURES')
@allure.link(url='',
             name='Source/Kata')
class MonkeyCountTestCase(unittest.TestCase):
    """
    Testing monkey_count function
    """
    def test_monkey_count(self):
        """
        Testing monkey_count function

        You take your son to the forest to see the monkeys.
        You know that there are a certain number there (n),
        but your son is too young to just appreciate the full
        number, he has to start counting them from 1.

        As a good parent, you will sit and count with him.
        Given the number (n), populate an array with all
        numbers up to and including that number, but excluding
        zero.
        :return:
        """

        allure.dynamic.title("Testing monkey_count function")
        allure.dynamic.severity(allure.severity_level.NORMAL)

        with allure.step("Enter a number (int) and verify the output"):

            data = [
                (1, [1]),
                (5, [1, 2, 3, 4, 5]),
                (3, [1, 2, 3]),
                (9, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
                (10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                (20, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                      12, 13, 14, 15, 16, 17, 18, 19, 20])
            ]

            for n, expected in data:
                print_log(n=n, expected=expected)
                self.assertEqual(expected, monkey_count(n))
