"""
Test for -> Human Readable Time
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS DATES/TIME MATHEMATICS NUMBERS

import unittest
import allure
from utils.log_func import print_log
from kyu_5.human_readable_time.make_readable import make_readable


# pylint: disable-msg=R0801
@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Math")
@allure.story('Human Readable Time')
@allure.tag('ALGORITHMS',
            'DATES/TIME',
            'MATHEMATICS',
            'NUMBERS')
@allure.link(url='https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python',
             name='Source/Kata')
# pylint: enable-msg=R0801
class MakeReadableTestCase(unittest.TestCase):
    """
    Testing make_readable function
    """

    def test_make_readable(self):
        """
        Testing make_readable function

        Write a function, which takes a non-negative integer
        (seconds) as input and returns the time in a human-readable
        format (HH:MM:SS)

        HH = hours, padded to 2 digits, range: 00 - 99
        MM = minutes, padded to 2 digits, range: 00 - 59
        SS = seconds, padded to 2 digits, range: 00 - 59

        The maximum time never exceeds 359999 (99:59:59)
        :return:
        """

        allure.dynamic.title("Testing make_readable function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")

        with allure.step("Enter test number and verify the output"):
            data = [
                (0, "00:00:00"),
                (5, "00:00:05"),
                (60, "00:01:00"),
                (86399, "23:59:59"),
                (359999, "99:59:59"),
            ]

            for seconds, expected in data:
                print_log(seconds=seconds, expected=expected)
                self.assertEqual(expected, make_readable(seconds))
