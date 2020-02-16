#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS NUMBERS STRINGS MATHEMATICS ALGORITHMS

import unittest
import allure
from kyu_8.holiday_vi_shark_pontoon.shark import shark


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite('Math')
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Holiday VI - Shark Pontoon')
@allure.tag('FUNDAMENTALS',
            'NUMBERS',
            'STRINGS',
            'MATHEMATICS',
            'ALGORITHMS')
@allure.link(url='https://www.codewars.com/kata/57e921d8b36340f1fd000059/train/python',
             name='Source/Kata')
class SharkTestCase(unittest.TestCase):
    """
    Testing shark function
    """
    def test_shark_alive_1(self):
        """
        Testing shark function -> positive
        :return:
        """

        allure.dynamic.title("Testing shark function (positive)")
        allure.dynamic.severity(allure.severity_level.NORMAL)

        with allure.step("Enter test data and verify the output"):
            self.assertEqual(shark(12, 50, 4, 8, True), "Alive!")

    def test_shark_alive_2(self):
        """
        Testing shark function -> positive
        :return:
        """

        allure.dynamic.title("Testing shark function (positive)")
        allure.dynamic.severity(allure.severity_level.NORMAL)

        with allure.step("Enter test data and verify the output"):
            self.assertEqual(shark(7, 55, 4, 16, True), "Alive!")

    def test_shark_bait(self):
        """
        Testing shark function -> negative
        :return:
        """

        allure.dynamic.title("Testing shark function (negative)")
        allure.dynamic.severity(allure.severity_level.NORMAL)

        with allure.step("Enter test data and verify the output"):
            self.assertEqual(shark(24, 0, 4, 8, True), "Shark Bait!")
