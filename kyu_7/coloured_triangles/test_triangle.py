"""
Test for -> Coloured Triangles

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# Logic Strings Algorithms

import allure  # pylint: disable=import-error
import unittest
from utils.log_func import print_log
from kyu_7.coloured_triangles.solution_for_triangle import triangle


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Coloured Triangles')
@allure.tag('Logic',
            'Strings',
            'Algorithms')
@allure.link(url='',
             name='Source/Kata')
class TriangleTestCase(unittest.TestCase):
    """
    Testing triangle function
    """

    def test_basic(self):
        """
        Basic test case
        :return:
        """

        with allure.step("Test basic string and verify the output"):
            test_data = [
                ('GB', 'R'),
                ('RRR', 'R'),
                ('RGBG', 'B'),
                ('RBRGBRB', 'G'),
                ('RBRGBRBGGRRRBGBBBGG', 'G'),
                ('B', 'B'),
            ]

            for string, expected in test_data:
                print_log(string=string, expected=expected)
                self.assertEqual(expected, triangle(string))

    def test_random(self):
        """
        Advanced/random test case
        :return:
        """

        with allure.step("Test advanced string and verify the output"):
            test_data = [
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
                ('RRBRBRBBBBBRBRRBBBGBBGBGGGRGR', 'G'),
            ]

            for string, expected in test_data:
                result = triangle(string)
                print_log(string=string,
                          expected=expected,
                          result=result)
                self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
