"""
Test for -> Diophantine Equation.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS MATHEMATICS ALGORITHMS NUMBERS

import unittest
import pytest
import allure
from parameterized import parameterized
from kyu_5.diophantine_equation.solution import sol_equa


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature('Math')
@allure.story('Diophantine Equation')
@allure.tag('FUNDAMENTALS',
            'MATHEMATICS',
            'ALGORITHMS',
            'NUMBERS')
@allure.link(
    url='https://www.codewars.com/kata/554f76dca89983cc400000bb',
    name='Source/Kata')
@pytest.mark.skip(reason="The solution is not ready")
class SolutionTestCase(unittest.TestCase):
    """Testing sol_equa function."""

    @parameterized.expand([
        (5, [[3, 1]]),
        (12, [[4, 1]]),
        (13, [[7, 3]]),
        (16, [[4, 0]]),
        (17, [[9, 4]]),
        (20, [[6, 2]])])
    def test_solution_basic(self, num, expected):
        """
        Testing using basic test data.

        :return:
        """
        self.assertEqual(sol_equa(num), expected)

    @parameterized.expand([
        (9001, [[4501, 2250]]),
        (9004, [[2252, 1125]]),
        (9008, [[1128, 562]]),
        (9009, [[4505, 2252], [1503, 750], [647, 320],
                [505, 248], [415, 202], [353, 170],
                [225, 102], [153, 60], [135, 48],
                [103, 20], [97, 10], [95, 2]])])
    def test_solution_medium(self, num, expected):
        """
        Testing using medium test data.

        :return:
        """
        self.assertEqual(num, expected)

    @parameterized.expand([
        (900000, [[112502, 56249], [56254, 28123],
                  [37506, 18747], [22510, 11245],
                  [18762, 9369], [12518, 6241],
                  [11270, 5615], [7530, 3735],
                  [6286, 3107], [4550, 2225],
                  [3810, 1845], [2590, 1205],
                  [2350, 1075], [1650, 675],
                  [1430, 535], [1150, 325],
                  [1050, 225], [950, 25]]),
        (90004, [[22502, 11250]]),
        (90005, [[45003, 22501], [9003, 4499],
                 [981, 467], [309, 37]]),
        (90009, [[45005, 22502], [15003, 7500],
                 [5005, 2498],
                 [653, 290], [397, 130], [315, 48]])])
    def test_solution_big(self, num, expected):
        """
        Testing using big test data.

        :return:
        """
        self.assertEqual(num, expected)

    def test_solution_empty(self):
        """
        Testing using empty test data.

        :return:
        """
        self.assertEqual(sol_equa(90002), [])
