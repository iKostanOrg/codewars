"""
Solution for -> Find the in-between point.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS GEOMETRY MATHEMATICS ALGORITHMS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_6.find_the_in_between_point.solution import middle_point


# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Algorithms")
@allure.story('Find the in-between point')
@allure.tag('FUNDAMENTALS',
            'GEOMETRY',
            'MATHEMATICS',
            'ALGORITHMS')
@allure.link(
    url='https://www.codewars.com/kata/58a672d6426bf38be4000057',
    name='Source/Kata')
# pylint: enable-msg=R0801
class MiddlePointTestCase(unittest.TestCase):
    """Test 'middle_point' function."""

    @parameterized.expand([
        ((1, 2, 3, 4, 5, 6, 7, 8, 9), 2,
         "Wrong point!"),
        ((0, 2, 0, 6, -2, 8, 3, 0, 4), 3,
         "Wrong point!"),
        ((0.25, 0.50, 0.75, 3.25, -0.50, -0.25, 1.00, 0.25, 0.50), 3,
         "Wrong point!"),
        ((1, 0, 4, 5, 0, 6, -7, 0, 0), 1,
         "Wrong point!"),
        ((-1, 0, 2, -2, 4, -1, -3, 8, -4), 2,
         "Wrong point!")])
    def test_middle_point(self, coords, expected, err):
        """
        Test 'middle_point' function with various test data.

        :param coords:
        :param expected:
        :param err:
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'middle_point' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>"
            "Given three points that lie on a straight line in "
            "3-dimensional space:"
            "- (x1,y1,z1)<br>"
            "- (x2,y2,z2)<br>"
            "- (x3,y3,z3)"
            "</p>"
            "<p>"
            "Function should return 1, 2, or 3 to indicate which "
            "point is the in-between one."
            "</p>")
        # pylint: enable-msg=R0801
        result = middle_point(coords)
        with allure.step(f"Enter test data: {coords} "
                         f"and verify the expected output: {expected}."):
            print_log(coords=coords, expected=expected, result=result, err=err)
            self.assertEqual(expected, result)
