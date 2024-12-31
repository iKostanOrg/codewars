"""
Test for -> 101 Dalmatians - squash the bugs, not the dogs!.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS ARRAYS DEBUGGING

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_8.dalmatians_101_squash_bugs.solution import how_many_dalmatians


# pylint: disable=R0801
@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('101 Dalmatians - squash the bugs, not the dogs!.')
@allure.tag('FUNDAMENTALS',
            'ARRAYS',
            'DEBUGGING')
@allure.link(
    url='https://www.codewars.com/kata/56f6919a6b88de18ff000b36',
    name='Source/Kata')
# pylint: enable=R0801
class HowManyDalmatiansTestCase(unittest.TestCase):
    """Test 'how_many_dalmatians' function."""

    @parameterized.expand([
        (26, "More than a handful!"),
        (8, "Hardly any"),
        (14, "More than a handful!"),
        (80, "Woah that's a lot of dogs!"),
        (100, "Woah that's a lot of dogs!"),
        (50, "More than a handful!"),
        (10, "Hardly any"),
        (101, "101 DALMATIONS!!!")])
    def test_how_many_dalmatians(self, number, expected):
        """
        Testing 'how_many_dalmatians' function with various test data.

        :param number:
        :param expected:
        :return:
        """
        # pylint: disable=R0801
        allure.dynamic.title(
            "Testing 'how_many_dalmatians' function.")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="'
            'https://www.codewars.com/users/myFirstCode/badges/large'
            '">'
            '<h3>Test Description:</h3>'
            "<p>"
            "Your friend has been out shopping for puppies "
            "(what a time to be alive!)... "
            "He arrives back with multiple dogs, and you simply "
            "do not know how to respond!"
            "</p>"
            "<p>"
            "By repairing the function provided, you will find out "
            "exactly how you should respond, depending on the number "
            "of dogs he has."
            "</p>"
            "<p>"
            "The number of dogs will always be a number and there "
            "will always be at least 1 dog."
            "</p>")
        # pylint: enable=R0801
        with allure.step(f"Enter a number (int): {number} "
                         f"and verify the expected output: {expected}."):
            result: str = how_many_dalmatians(number)
            print_log(number=number, expected=expected, result=result)
            self.assertEqual(result, expected)
