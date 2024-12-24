"""
Test for -> Third Angle of a Triangle.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.third_angle_of_triangle.third_angle_of_triangle \
    import other_angle


# pylint: disable-msg=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Math")
@allure.sub_suite("Unit Tests")
@allure.feature("Calculation")
@allure.story('Third Angle of a Triangle')
@allure.tag('FUNDAMENTALS')
@allure.link(
    url='https://www.codewars.com/kata/5a023c426975981341000014',
    name='Source/Kata')
# pylint: enable-msg=R0801
class OtherAngleTestCase(unittest.TestCase):
    """Testing other_angle function."""

    def test_other_angle(self):
        """
        Testing other_angle function with various test data.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("You are given two angles -> find the 3rd.")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>You are given two angles (in degrees) of a triangle."
            "Find the 3rd.</p>")
        # pylint: enable-msg=R0801
        with allure.step("Enter values of two angles and return the 3rd"):
            a: int = 30
            b: int = 60
            expected: int = 90
            print_log(a=a, b=b, expected=expected)
            self.assertEqual(other_angle(a, b), expected)

        with allure.step("Enter values of two angles and return the 3rd"):
            a = 60
            b = 60
            expected = 60
            print_log(a=a, b=b, expected=expected)
            self.assertEqual(other_angle(a, b), expected)

        with allure.step("Enter values of two angles and return the 3rd"):
            a = 43
            b = 78
            expected = 59
            print_log(a=a, b=b, expected=expected)
            self.assertEqual(other_angle(a, b), expected)

        with allure.step("Enter values of two angles and return the 3rd"):
            a = 10
            b = 20
            expected = 150
            print_log(a=a, b=b, expected=expected)
            self.assertEqual(other_angle(a, b), expected)
