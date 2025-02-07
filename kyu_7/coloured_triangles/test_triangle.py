"""
Test for -> Coloured Triangles.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# Logic Strings Algorithms

import unittest
import allure  # pylint: disable=import-error
from parameterized import parameterized
from utils.log_func import print_log
from kyu_7.coloured_triangles.solution_for_triangle import triangle


# pylint: disable-msg=R0801
@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Coloured Triangles')
@allure.tag('Logic',
            'Strings',
            'Algorithms')
@allure.link(
    url='https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111',
    name='Source/Kata')
# pylint: enable-msg=R0801
class TriangleTestCase(unittest.TestCase):
    """Testing triangle function."""

    @parameterized.expand([
        ('GB', 'R'),
        ('RRR', 'R'),
        ('RGBG', 'B'),
        ('RBRGBRB', 'G'),
        ('RBRGBRBGGRRRBGBBBGG', 'G'),
        ('B', 'B'),
        ('BGBGB', 'R'),
        ('BBRRBRGBRRBRGRRBGGRRBBGBGGRGGB', 'G'),
        ('RB', 'G'),
        ('GRBGRGBBRBRGRRGGGGRBRBRGGRB', 'B'),
        ('BBGRBGRRGGGRRBRBRBGRBGRRRBBBG', 'G'),
        ('RRBBRRGBRBGBRBRGBGGRBBBBRGGRGB', 'R'),
        ('GGBRGBBRBGRRGGGBGBGRGBGGRGRB', 'R'),
        ('BRBBGGRGBGGGBGRBRGRGRRBBGBR', 'G'),
        ('GBBRBRGGGGBRGGBBGGBGBRGRBGRGBB', 'G'),
        ('RRRBRRGRRGBGBBRGRGRGRB', 'B'),
        ('BRGGRBBBBGBRRRRBRBRRBGBGRBGB', 'B'),
        ('RRBRBRBBBBBRBRRBBBGBBGBGGGRGR', 'G')])
    def test_triangle(self, string, expected):
        """
        Basic test case.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Basic test case for triangle func.")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step(f"Enter test string: {string} "
                         f"and verify the output: {expected}"):
            result = triangle(string)
            print_log(string=string, expected=expected, result=result)
            self.assertEqual(expected, result)
