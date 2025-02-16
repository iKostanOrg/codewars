"""
Test for -> Replace With Alphabet Position.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# STRINGS, FUNDAMENTALS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_6.replace_with_alphabet_position.solution \
    import alphabet_position


# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Replace With Alphabet Position')
@allure.tag('STRINGS', 'FUNDAMENTALS')
@allure.link(
    url='https://www.codewars.com/kata/546f922b54af40e1e90001da',
    name='Source/Kata')
# pylint: enable-msg=R0801
class AlphabetPositionTestCase(unittest.TestCase):
    """Testing 'alphabet_position' function."""

    @parameterized.expand([
        ("The sunset sets at twelve o' clock.",
         "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 \
15 3 12 15 3 11"),
        ("The narwhal bacons at midnight.",
         "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 \
7 8 20"),
        ('w\'p[9lKIQ7v%]{2W-P)j4rwttJ:R:"R,^%@fg8=o;e1:aJeTHQv,KDAk\
ZsKQq6j"ziwD[zT:P6%$rEH$^@',
         "23 16 12 11 9 17 22 23 16 10 18 23 20 20 10 18 18 6 7 15 \
5 1 10 5 20 8 17 22 11 4 1 11 26 19 11 17 17 10 26 9 23 4 26 20 16 18 5 8")
    ])
    def test_alphabet_position(self, string, expected):
        """
        Testing 'alphabet_position' function with various test data.

        Note: If anything in the text isn't a letter, ignore it and
        don't return it..
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing the 'alphabet_position' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>The 'alphabet_position' function should replace every letter"
            " with its position in the alphabet.</p>")
        # pylint: enable-msg=R0801
        result: str = alphabet_position(string)
        with allure.step(f"Enter test data: {string}, "
                         f"and verify the output ({result}) "
                         f"vs expected ({expected})"):
            print_log(string=string, result=result, expected=expected)
            self.assertEqual(expected, result)

    @parameterized.expand([
        ("", ""),
        ("123", ""),
        ("!@#$%^&*()", ""),
        ("a1!b", "1 2"),
        ("AbZ!", "1 2 26")
    ])
    def test_alphabet_position_edge_cases(self, string, expected):
        """
        Testing 'alphabet_position' function with various edge cases,
        including empty strings, numbers, special characters, and
        mixed alphanumeric input.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing the 'alphabet_position' with edge cases.")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing edge cases, including empty strings, numbers, "
            "special characters, and mixed alphanumeric input.</p>")
        # pylint: enable-msg=R0801
        result: str = alphabet_position(string)
        with allure.step(f"Enter test data: {string}, "
                         f"and verify the output ({result}) "
                         f"vs expected ({expected})"):
            print_log(string=string, result=result, expected=expected)
            self.assertEqual(expected, result)
