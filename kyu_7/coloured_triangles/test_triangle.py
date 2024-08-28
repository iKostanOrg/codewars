"""
Test for -> Coloured Triangles

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# Logic Strings Algorithms

import unittest
import allure  # pylint: disable=import-error
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

    def test_triangle(self):
        """
        Basic test case
        :return:
        """

        with allure.step("Enter test string and verify the output"):
            test_data = [
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
