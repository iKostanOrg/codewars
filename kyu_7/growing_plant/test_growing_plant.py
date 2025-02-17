"""
Test -> Simple Fun #74: Growing Plant.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_7.growing_plant.growing_plant import growing_plant


# pylint: disable-msg=R0801
@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Calculation")
@allure.story('Simple Fun #74: Growing Plant')
@allure.tag('ALGORITHMS')
@allure.link(
    url='https://www.codewars.com/kata/58941fec8afa3618c9000184',
    name='Source/Kata')
# pylint: enable-msg=R0801
class GrowingPlantTestCase(unittest.TestCase):
    """Testing growing_plant function."""

    @parameterized.expand([
        ((100, 10, 910), 10),
        ((10, 9, 4), 1),
        ((5, 2, 0), 1),
        ((5, 2, 5), 1),
        ((5, 2, 6), 2)])
    def test_growing_plant(self, input_data, expected):
        """
        Testing growing_plant function.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title('Testing growing_plant function')
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step('Enter upSpeed, downSpeed and '
                         'desiredHeight and verify the output.'):
            up_speed: int = input_data[0]
            down_speed: int = input_data[1]
            desired_height: int = input_data[2]
            print_log(input_data=input_data,
                      expected=expected)
            self.assertEqual(expected,
                             growing_plant(up_speed,
                                           down_speed,
                                           desired_height))
