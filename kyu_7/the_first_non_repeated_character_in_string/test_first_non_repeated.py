"""
Test for -> The First Non-Repeated Character In A String.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS ALGORITHMS STRINGS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_7.the_first_non_repeated_character_in_string.first_non_repeated \
    import first_non_repeated


# pylint: disable-msg=R0801
@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('The First Non Repeated Character In A String')
@allure.tag('FUNDAMENTALS',
            'ALGORITHMS',
            'STRINGS')
@allure.link(
    url='https://www.codewars.com/kata/570f6436b29c708a32000826',
    name='Source/Kata')
# pylint: enable-msg=R0801
class FirstNonRepeatedTestCase(unittest.TestCase):
    """Testing first_non_repeated function."""

    @parameterized.expand([
        ("test", 'e'),
        ("teeter", 'r'),
        ("1122321235121222", '5'),
        ('uqqmsmtnrhjooknjtmllkpuphirsi', None),
        ('ogmhrsoqiklqfmhgnpjsrikmnlpfj', None),
        ('knioolrpnutskmqmhqtriipjjushl', None),
        ('oirfqjmsrmnhlqgghplpsonkyfijk', 'y')])
    def test_first_non_repeated(self, s, expected):
        """
        Testing first_non_repeated function with various test data.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing first_non_repeated function with various inputs")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="'
            'https://www.codewars.com/users/myFirstCode/badges/large'
            '">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step(f"Enter test string: {s} "
                         f"and verify the expected output: {expected}."):
            print_log(s=s, expected=expected)
            self.assertEqual(expected, first_non_repeated(s))
