"""
Test for -> String incrementer
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS REGULAR EXPRESSIONS DECLARATIVE PROGRAMMING
# ADVANCED LANGUAGE FEATURES STRINGS PARSING ALGORITHMS

import unittest
import allure
from utils.log_func import print_log
from kyu_5.string_incrementer.string_incrementer \
    import increment_string


# pylint: disable-msg=R0801
@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('String incrementer')
@allure.tag('FUNDAMENTALS',
            'REGULAR EXPRESSIONS',
            'DECLARATIVE PROGRAMMING',
            'ADVANCED LANGUAGE FEATURES',
            'STRINGS PARSING',
            'ALGORITHMS')
@allure.link(
    url='https://www.codewars.com/kata/54a91a4883a7de5d7800009c',
    name='Source/Kata')
# pylint: enable-msg=R0801
class StringIncrementerTestCase(unittest.TestCase):
    """
    Testing increment_string function
    """

    def test_increment_string(self):
        """
        Testing a function named increment_string
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing increment_string function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>"
            "- If the string already ends with a number, the number "
            "should be incremented by 1.<br/>"
            "- If the string does not end with a number. the number 1 "
            "should be appended to the new string."
            "</p>")
        # pylint: enable-msg=R0801
        test_data: tuple = (
            ("foo", "foo1"),
            ("foobar001", "foobar002"),
            ("foobar1", "foobar2"),
            ("foobar00", "foobar01"),
            ("foobar99", "foobar100"),
            ("foobar099", "foobar100"),
            ("", "1"),
            ('009', '010'),
            ('^0000007', '^0000008'))

        for sting, expected in test_data:
            with allure.step("Enter test string and verify the output"):
                result = increment_string(sting)
                print_log(string=sting,
                          expected=expected,
                          result=result)
                self.assertEqual(expected, result)
