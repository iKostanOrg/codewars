#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS

import allure
import unittest
from utils.log_func import print_log
from kyu_5.directions_reduction.directions_reduction import dirReduc


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Directions Reduction')
@allure.tag('FUNDAMENTALS')
@allure.link(url='https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python',
             name='Source/Kata')
class DirectionsReductionTestCase(unittest.TestCase):
    """
    Testing dirReduc function
    """

    def test_directions_reduction(self):
        """
        Test a function dirReduc which will take an array of
        strings and returns an array of strings with the needless
        directions removed (W<->E or S<->N side by side).

        The Haskell version takes a list of directions with
        data Direction = North | East | West | South.

        The Clojure version returns nil when the path is
        reduced to nothing.

        The Rust version takes a slice of enum Direction
        {NORTH, SOUTH, EAST, WEST}.
        :return:
        """

        allure.dynamic.title("Testing dirReduc function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p> Test a function dirReduc which will take an array of "
                                        "strings and returns an array of strings with the needless "
                                        "directions removed (W<->E or S<->N side by side).</p>")

        test_data = [
            (["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"],
            ['WEST']),
            (["NORTH", "WEST", "SOUTH", "EAST"],
            ["NORTH", "WEST", "SOUTH", "EAST"])
        ]

        for d in test_data:

            array = d[0]
            expected = d[1]
            result = dirReduc(array)

            with allure.step("Enter test data ({}) "
                             "and verify the output ({}) "
                             "vs expected ({})".format(array,
                                                       result,
                                                       expected)):

                print_log(array=array,
                          result=result,
                          expected=expected)

                self.assertListEqual(expected, result)
