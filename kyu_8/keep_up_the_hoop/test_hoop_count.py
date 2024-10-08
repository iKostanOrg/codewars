"""
Test -> Keep up the hoop
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.keep_up_the_hoop.hoop_count import hoop_count


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Conditions")
@allure.story('Keep up the hoop')
@allure.tag('FUNDAMENTALS')
@allure.link(
    url='https://www.codewars.com/kata/55cb632c1a5d7b3ad0000145',
    name='Source/Kata')
# pylint: enable=R0801
class HoopCountTestCase(unittest.TestCase):
    """
    Testing hoop_count function
    """

    def test_hoop_count_positive(self):
        """
        Testing hoop_count function (positive)

        Alex just got a new hula hoop, he loves it but feels
        discouraged because his little brother is better than him

        Write a program where Alex can input (n) how many times
        the hoop goes round and it will return him an encouraging message

        - 10 or more hoops, return "Great, now move on to tricks".

        - Not 10 hoops, return "Keep at it until you get it".

        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title(
            "Testing hoop_count function (positive test case)")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable=R0801
        with allure.step("Enter n and verify the result"):
            n: int = 11
            expected: str = "Great, now move on to tricks"
            print_log(n=n, expected=expected)
            self.assertEqual(hoop_count(n), expected)

    def test_hoop_count_negative(self):
        """
        Testing hoop_count function (negative)
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title(
            "Testing hoop_count function (negative test case)")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable=R0801
        with allure.step("Enter n and verify the result"):
            n: int = 3
            expected: str = "Keep at it until you get it"
            print_log(n=n, expected=expected)
            self.assertEqual(hoop_count(n), expected)
