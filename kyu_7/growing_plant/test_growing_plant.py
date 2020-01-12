#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS

import allure
import unittest
from utils.log_func import print_log
from kyu_7.growing_plant.growing_plant import growing_plant


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Calculation")
@allure.story('Simple Fun #74: Growing Plant')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class GrowingPlantTestCase(unittest.TestCase):
    """
    Testing growing_plant function
    """

    def test_growing_plant(self):
        """
        Testing growing_plant function

        Task

        Each day a plant is growing by upSpeed meters.
        Each night that plant's height decreases by downSpeed
        meters due to the lack of sun heat. Initially, plant
        is 0 meters tall. We plant the seed at the beginning
        of a day. We want to know when the height of the plant
        will reach a certain level.

        Example

        For upSpeed = 100, downSpeed = 10 and desiredHeight = 910,
        the output should be 10.

        For upSpeed = 10, downSpeed = 9 and desiredHeight = 4,
        the output should be 1. Because the plant reach to the desired
        height at day 1(10 meters).

        Input/Output

        [input] integer upSpeed
        A positive integer representing the daily growth.
        Constraints: 5 ≤ upSpeed ≤ 100.

        [input] integer downSpeed
        A positive integer representing the nightly decline.
        Constraints: 2 ≤ downSpeed < upSpeed.

        [input] integer desiredHeight
        A positive integer representing the threshold.
        Constraints: 4 ≤ desiredHeight ≤ 1000.

        [output] an integer

        The number of days that it will take for the plant to
        reach/pass desiredHeight (including the last day in the
        total count).
        """

        allure.dynamic.title('Testing growing_plant function')
        allure.dynamic.severity(allure.severity_level.NORMAL)

        with allure.step('Enter upSpeed, downSpeed and '
                         'desiredHeight and verify the output'):

            data = [
                ((100, 10, 910), 10),
                ((10, 9, 4), 1),
                ((5, 2, 0), 1),
                ((5, 2, 5), 1),
                ((5, 2, 6), 2),
            ]

            for input_data, expected in data:

                upSpeed = input_data[0]
                downSpeed = input_data[1]
                desiredHeight = input_data[2]

                print_log(input_data=input_data,
                          expected=expected)

                self.assertEqual(expected,
                                 growing_plant(upSpeed, downSpeed, desiredHeight))
