"""
Test for -> Closest elevator.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# Algorithms

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_8.closest_elevator.closest_elevator import elevator


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Closest elevator')
@allure.tag('FUNDAMENTALS',
            'ALGORITHMS')
@allure.link(
    url='https://www.codewars.com/kata/5c374b346a5d0f77af500a5a',
    name='Source/Kata')
# pylint: enable=R0801
class ClosestElevatorTestCase(unittest.TestCase):
    """Test elevator function."""

    @parameterized.expand([
        ((0, 1, 0), "left"),
        ((0, 1, 1), "right"),
        ((0, 1, 2), "right"),
        ((0, 0, 0), "right"),
        ((0, 2, 1), "right")])
    def test_elevator_basic(self, elevators, expected):
        """
        Testing 'elevator' function with various test data.

        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title("Testing elevator function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="'
            'https://www.codewars.com/users/myFirstCode/badges/large'
            '">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable=R0801
        with allure.step(f"Enter test data: {elevators} "
                         f"and verify the expected output: {expected}."):
            left, right, call = elevators
            result: str = elevator(left, right, call)
            print_log(expected=expected, left=left, right=right, call=call)
            message: str = f'elevators: {elevators}, result: {result}, expected: {expected}'
            self.assertEqual(expected, result, msg=message)
